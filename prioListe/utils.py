from django.core.exceptions import FieldError
from staff.models import Staff
import re


def get_choices():
    # choices in a seperated funtion to change it easier
    STATUS_CHOICES = (
        ('', ''),
        ('Test', 'Test'),
        ('Fertig', 'Fertig'),
        ('Löschen', 'Löschen'),
        ('Vertrieb', 'Vertrieb'),
        ('Produktion', 'Produktion'),
        ('Bearbeitung', 'Bearbeitung'),
    )
    return STATUS_CHOICES

STAFFCHOICESONE = set()
for staff in Staff.objects.all():
    STAFFCHOICESONE.add((staff.initialies, staff.name))

STAFFCHOICESTWO = set()
STAFFCHOICESTWO.add(('', ''))
for staff in Staff.objects.all():
    STAFFCHOICESTWO.add((staff.initialies, staff.name))


def check_for_update(queryset):
    try:
        for object in queryset:
            time_in_weeks = (object.finished_until - object.created_at) / 7
            object.time_in_weeks = time_in_weeks.days
            object.save()
    except:
        pass


def check_form_and_db(form, queryset):
    """
    get data from(bevor it was saved) and get data from current object
    check if there are changes between them
    :param form:
    :param queryset:
    :return: boolean update
    """
    update = False
    if queryset.box != form.instance.box:
        update = True
    elif queryset.customer != form.instance.customer:
        update = True
    elif queryset.hardware != form.instance.hardware:
        update = True
    elif queryset.created_at != form.instance.created_at:
        update = True
    elif queryset.status != form.instance.status:
        update = False
    elif queryset.finished_until != form.instance.finished_until:
        update = True
    elif queryset.optional_status != form.instance.optional_status:
        update = False
    elif queryset.finished_until != form.instance.finished_until:
        update = True
    elif queryset.staff != form.instance.staff:
        update = True
    elif queryset.time_in_weeks != int(form.instance.time_in_weeks):
        update = True
    elif queryset.remark != form.instance.remark:
        update = True
    elif queryset.production_remark != form.instance.production_remark:
        update = False

    return update


def update_time_in_weeks(date1, date2):
    days = (date2 - date1).days
    if days > 7:
        return days / 7
    else:
        return days

COLORS = {
    'Fertig': '#33cc00',
    'Test': '#99ff99',
    'Bearbeitung': '#ffff00',
    'Produktion': '#ffffcc',
    'Vertrieb': '#ff99ff',
    'Löschen': '#ffffff'
}


def searching(model, search_string, *args, **kwargs):
    '''
    usage e.g.:
        t = searching(ModelName, search_string, 'Foo', 'Bar', **kwargs)
        tmp = ModelName.objects.none()
            for i in t:
                tmp = i | tmp #merge Querysets
    :param model: Django Modelobject
    :param search_string: self explaning
    :param args: datatypes that should be excluded
    :param kwargs: can contain exlude or exact as key with a list of values containing the field name/-s
    :return: list of querysets gte 1
    '''
    types = [field.get_internal_type() for field in model._meta.get_fields()]
    names = [f.name for f in [field for field in model._meta.get_fields()]]
    field_name_dict = dict(zip(names, types))
    excat_fields = []
    foreignKeyFields = None
    special_filter = None

    if kwargs:
        try:
            foreignKeyFields = kwargs['foreignKeyFields']
        except KeyError:
            pass
        try:
            special_filter = kwargs['filter']
        except KeyError:
            pass
        try:
            field_name_dict = remove_items_dict(field_name_dict, kwargs['exclude'])
        except KeyError:
            pass
        try:
            excat_fields = kwargs['exact']
        except KeyError:
            pass
        # to use following e.g. in function call:
        # data = {'exclude': liste['foo', ]}
        # searching(modelname, searchstring, kwargs=data)
        try:
            if 'exclude' in kwargs['kwargs']:
                field_name_dict = remove_items_dict(field_name_dict, kwargs['kwargs']['exclude'])
            elif 'exact' in kwargs:
                excat_fields = kwargs['exact']
        except KeyError:
            pass

    if args:
        field_name_dict = remove_items_dict(field_name_dict, args)

    if special_filter is not None:
        tmp = model.objects.filter(**{special_filter[0]: special_filter[1]})
    else:
        tmp = model.objects.all()
    liste = []
    for key, value in field_name_dict.items():

        if value != 'ForeignKey' and value != 'ManyToManyField':
            if key in excat_fields:
                filter = f'{key}__iexact'
                if len(tmp.filter(**{filter: search_string})) > 0:
                    liste.append(tmp.filter(**{filter: search_string}))
            else:
                filter = f'{key}__icontains'
                if len(tmp.filter(**{filter: search_string})) > 0:
                    liste.append(tmp.filter(**{filter: search_string}))
        elif value == 'ManyToManyField' and key == 'customer_collar':
            filter = f'{key}__serialno__icontains'
            if len(tmp.filter(**{filter: search_string})) > 0:
                liste.append(tmp.filter(**{filter: search_string}))
        else:
            filter = f'{key}__pk__iexact'
            if len(tmp.filter(**{filter: search_string})) > 0:
                liste.append(tmp.filter(**{filter: search_string}))
            else:
                if foreignKeyFields is not None:
                    for keyfield in foreignKeyFields:
                        filter = f'{key}__{keyfield}__icontains'
                        try:
                            if len(tmp.filter(**{filter: search_string})) > 0:
                                liste.append(tmp.filter(**{filter: search_string}))
                        except FieldError:
                            pass
                else:
                    filter = f'{key}__name__icontains'
                    if len(tmp.filter(**{filter: search_string})) > 0:
                        liste.append(tmp.filter(**{filter: search_string}))
    return liste


def remove_items_dict(dictionary, keys):
    '''
    Remove items from dictonary
    :param dictionary:
    :param keys:
    :return:
    '''
    return {key: value for key, value in dictionary.items() if key not in keys and value not in keys}


def move_ids_from_remark_to_ids(text):
    '''
    extract ids from allready existing production_remark to new field ids
    :param text:
    :return: ids as string seperated by ;
    '''
    range_ids = re.findall(r'[0-9]*-[0-9]*', text)
    tmp_string = '; '.join(range_ids)

    tmp = re.sub(r'[0-9]*-[0-9]*', '', text)
    id_list = list(filter(lambda x: len(x) > 4, filter(None, re.findall(r'[\d]*', tmp))))
    new_string = '; '.join(id_list)
    return f'{new_string}; {tmp_string}'


def filter_ids(obj, id):
    '''

    :param id:
    :return:
    '''
    queryset = obj.objects.all().only('pk', 'ids')
    for i in queryset:
        if i.ids is not None:
            if '-' in i.ids:
                x = i.ids.split('; ')
                x = list(filter(lambda x: '-' in x, x))
                for ids in x:
                    if int(ids.split('-')[0]) > int(id) or int(id) < int(ids.split('-')[1]):
                        return i.pk
                else:
                    if id in i.ids:
                        return i.pk
                    else:
                        return None
            else:
                if id in i.ids:
                    return i.pk
    return None

