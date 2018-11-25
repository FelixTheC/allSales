import os
from django.core.exceptions import ObjectDoesNotExist
from django.forms import formset_factory
from django.utils.datastructures import MultiValueDictKeyError
from allSales.settings import BASE_DIR
try:
    from django.urls import reverse
except:
    from django.core.urlresolvers import reverse
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from .forms import CreateForm
from .forms import UpdateSelectForm
from .forms import CheckProductionStatus
from .forms import BatterieSearchForm
from .forms import HardwareCreateForm
from .forms import BaseLinkFormSet
from .forms import Search_Everything
from .forms import UpdateSelectFormWithoutBoxNumber
from .forms import UpdateDoneForm
from .models import PriolisteAssignment
from .models import Shelf
from .models import ProductionTime
from .utils import check_form_and_db
from .utils import check_for_update
from .utils import filter_ids


def handle_uploaded_files(f, filepath, filename):
    if not os.path.isdir(BASE_DIR + '/media/media/' + filepath):
        os.mkdir(os.path.join(BASE_DIR + '/media/media/',  filepath + '/'))
        upload_file(f, filepath, filename)
    else:
        upload_file(f, filepath, filename)


def upload_file(f, filepath, filename):
    with open(BASE_DIR + '/media/media/' + filepath + '/' + filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()


class UpdateAssignment(UpdateView):
    """
    UpdateAssigment uses UpdateView class -> needs model, template_name and fields or form_class
    get_success_url: returns the user back to the list overview
    form_valid: will only executed if form is really valid and when it is, than it will check over
    'check_form_and_db' if an existing db_entry has changed in an specific way
    """
    model = PriolisteAssignment
    template_name = 'assignment_form.html'
    form_class = UpdateSelectForm
    ids = []

    def get_initial(self):
        if self.object.prod_rec_string is not None:
            file_list = self.object.prod_rec_string.split('$')
            try:
                if file_list[0] != '':
                    self.object.prod_rec_one = file_list[0]
                if file_list[1] != '':
                    self.object.prod_rec_two = file_list[1]
                if file_list[2] != '':
                    self.object.prod_rec_three = file_list[2]
                if file_list[3] != '':
                    self.object.prod_rec_four = file_list[3]
                if file_list[4] != '':
                    self.object.prod_rec_five = file_list[4]
                self.object.prod_rec_string = ''
            except IndexError:
                pass

    def post(self, request, *args, **kwargs):
        file = request.FILES.getlist('id_file')
        for f in file:
            lines = f.readlines()
            for line in lines:
                try:
                    id = line.decode('utf-8').split()[0].strip()
                    if str.isnumeric(id):
                        self.ids.append(id)
                except IndexError:
                    pass
            # else:
            #     raise ValueError('Wrong file or wrong file format, file must be a Config file')
        return super(UpdateAssignment, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('pListe:home')

    def form_valid(self, form):
        numbers = set([i for i in range(1, 1000)])
        forgiven_nums = set([obj.internal_progress_number for obj in PriolisteAssignment.objects.all()])
        if form.instance.changed != 'Löschen':
            form.instance.changed = check_form_and_db(form, PriolisteAssignment.objects.get(pk=form.instance.pk))
        if form.instance.internal_progress_number < 0:
            form.instance.internal_progress_number = list(numbers - forgiven_nums)[0]
        # if len(form.instance.ids) < 1:
        #     form.instance.ids = move_ids_from_remark_to_ids(form.instance.production_remark)
        if form.cleaned_data['id_file'] is not None:
            if form.instance.ids[0] == ';':
                form.instance.ids = '; '.join(self.ids) + ';'
            else:
                val = set(form.instance.ids.split(';')).union(set(self.ids))
                form.instance.ids = '; '.join(list(val)[1:]) + ';'
        else:
            if len(form.instance.ids) < 1:
                form.instance.ids = ';'
        self.ids = None
        return super(UpdateAssignment, self).form_valid(form)


class UpdateAssignmentWithoutBox(UpdateView):
    model = PriolisteAssignment
    template_name = 'assignment_form.html'
    form_class = UpdateSelectFormWithoutBoxNumber

    def get_initial(self):
        if self.object.prod_rec_string is not None:
            file_list = self.object.prod_rec_string.split('$')
            try:
                if file_list[0] != '':
                    self.object.prod_rec_one = file_list[0]
                if file_list[1] != '':
                    self.object.prod_rec_two = file_list[1]
                if file_list[2] != '':
                    self.object.prod_rec_three = file_list[2]
                if file_list[3] != '':
                    self.object.prod_rec_four = file_list[3]
                if file_list[4] != '':
                    self.object.prod_rec_five = file_list[4]
                self.object.prod_rec_string = ''
            except IndexError:
                pass

    def get_success_url(self):
        return reverse('pListe:home')

    def form_valid(self, form):
        form.instance.changed = check_form_and_db(form, PriolisteAssignment.objects.get(pk=form.instance.pk))
        return super(UpdateAssignmentWithoutBox, self).form_valid(form)


class UpdatedProduction(UpdateView):
    model = PriolisteAssignment
    template_name = 'checkProd.html'
    form_class = CheckProductionStatus

    def get_context_data(self, **kwargs):
        content = super(UpdatedProduction, self).get_context_data(**kwargs)
        content['obj'] = self.object
        content['shelf'] = Shelf.objects.filter(assignment=self.object)
        return content

    def post(self, request, *args, **kwargs):
        shelf_type = request.POST.get('shelf_type')
        nums_of_rows = request.POST.get('num_of_rows')
        shelf_string = ''
        try:
            for i in range(1, int(nums_of_rows) + 1):
                char = request.POST.getlist(shelf_type + '_shelf_char_' + str(i))
                nums = request.POST.getlist(shelf_type + '_shelf_num_' + str(i))
                if shelf_type == 'belt':
                    shelf_string += char[0] + nums[0] + ', '
                elif shelf_type == 'batterie':
                    shelf_string += char[1] + nums[1] + ', '
                else:
                    shelf_string += char[2] + nums[2] + ', '
            try:
                shelf_obj = Shelf.objects.get(assignment__pk=kwargs['pk'], shelf_type=shelf_type)
                shelf_obj.compartment = shelf_obj.compartment + shelf_string
                shelf_obj.save()
            except ObjectDoesNotExist:
                Shelf.objects.create(shelf_type=shelf_type,
                                     compartment=shelf_string,
                                     assignment=PriolisteAssignment.objects.get(pk=kwargs['pk'])
                                     )
        except ValueError:
            pass
        form = self.form_class(request.POST)
        if form.is_valid():
            assignment = PriolisteAssignment.objects.get(pk=kwargs['pk'])
            assignment.belt = True if request.POST.get('belt') == 'on' else False
            assignment.batterie = True if request.POST.get('batterie') == 'on' else False
            assignment.assembled = True if request.POST.get('assembled') == 'on' else False
            assignment.elektronic = True if request.POST.get('elektronic') == 'on' else False
            assignment.save()
            return redirect(reverse('pListe:home'))
        else:
            return super(UpdatedProduction, self).form_invalid(form)

    def get_success_url(self):
        return reverse('pListe:home')


class UpdateDoneAssignment(UpdateView):
    model = PriolisteAssignment
    form_class = UpdateDoneForm
    template_name = 'assignment_done_update_form.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateDoneAssignment, self).get_context_data(**kwargs)
        context['obj'] = self.object
        return context
    
    def form_valid(self, form):
        return super(UpdateDoneAssignment, self).form_valid(form)

    def get_success_url(self):
        return reverse('pListe:done')


def show_list(request):
    """
    get the data from db and the entries with status = 'Fertig'
    will be sorted out and delete instantly

    :param request:
    :return: request, template_name, context
    """
    check_for_update(PriolisteAssignment.objects.filter(changed=True))
    liste = PriolisteAssignment.objects.all().exclude(status='Löschen')
    #PriolisteAssignment.objects.filter(status='Löschen').delete()
    context = {
        'object_list': liste,
        'batterie_search': BatterieSearchForm,
        'prio_search': Search_Everything,

    }
    return render(request, template_name='assignment_list.html', context=context)


def show_finished_list(request):
    liste = PriolisteAssignment.objects.filter(status='Löschen')
    context = {
        'object_list': liste,
        'batterie_search': BatterieSearchForm,
        'prio_search': Search_Everything,
    }
    return render(request, template_name='assignment_done_list.html', context=context)


def update_box(request, pk):
    obj = PriolisteAssignment.objects.get(pk=pk)
    obj.has_box = True
    obj.save()
    return redirect('pListe:home')


def update_belt(request, pk, path):
    obj = PriolisteAssignment.objects.get(pk=pk)
    if obj.belt:
        obj.belt = False
    else:
        obj.belt = True
    obj.save()
    return redirect_to_where_i_was(request, path, obj.internal_progress_number)


def update_batterie(request, pk, path):
    obj = PriolisteAssignment.objects.get(pk=pk)
    if obj.batterie:
        obj.batterie = False
    else:
        obj.batterie = True
    obj.save()
    return redirect_to_where_i_was(request, path, obj.internal_progress_number)


def update_assembled(request, pk, path):
    obj = PriolisteAssignment.objects.get(pk=pk)
    if obj.assembled:
        obj.assembled = False
    else:
        obj.assembled = True
    obj.save()
    return redirect_to_where_i_was(request, path, obj.internal_progress_number)


def update_electronic(request, pk, path):
    obj = PriolisteAssignment.objects.get(pk=pk)
    if obj.elektronic:
        obj.elektronic = False
    else:
        obj.elektronic = True
    obj.save()
    return redirect_to_where_i_was(request, path, obj.internal_progress_number)


def update_batterie_shelf(request, pk):
    return update_shelf(request, pk, 'batterie')


def update_belt_shelf(request, pk):
    return update_shelf(request, pk, 'belt')


def update_electric_shelf(request, pk):
    return update_shelf(request, pk, 'electric')


def update_shelf(request, pk, shelf_type):
    if request.method != 'POST':
        object = Shelf.objects.filter(shelf_type=shelf_type).get(assignment__pk=pk)
        obj = PriolisteAssignment.objects.get(pk=pk)
        context = {
            'pk': pk,
            'object': object,
            'obj': obj,
            'shelf_type': shelf_type,
        }
        return render(request, 'update_shelf.html', context)
    else:
        shelf = request.POST['shelf']
        obj = Shelf.objects.filter(shelf_type=shelf_type).get(assignment__pk=pk)
        if obj.compartment != shelf:
            obj.compartment = shelf
            obj.save()
        return redirect(reverse('pListe:updateProduction', kwargs={
            'pk': pk,
        }))


def show_missing_belts(request):
    liste = PriolisteAssignment.objects.all().filter(belt=False)
    context = {
        'object_list': liste,
        'batterie_search': BatterieSearchForm,
        'prio_search': Search_Everything,
    }
    return render(request, template_name='assignment_list.html', context=context)


def show_missing_batteries(request):
    liste = PriolisteAssignment.objects.all().filter(batterie=False)
    context = {
        'object_list': liste,
        'batterie_search': BatterieSearchForm,
        'prio_search': Search_Everything,
    }
    return render(request, template_name='assignment_list.html', context=context)


def try_file(request, filename):
    try:
        handle_uploaded_files(request.FILES[filename],
                              request.POST['ordering_number'],
                              str(request.FILES[filename]))
        return '/media/' + request.POST['ordering_number'] + '/' +\
               str(request.FILES[filename])
    except MultiValueDictKeyError:
        return ''


def check_dropOffs(request):
    dropOffs = dict()
    for i in range(0, 5):
        try:
            dropOffs['externDropOff' + str(i)] = request.POST['form-' + str(i) + '-externDropOff']
        except MultiValueDictKeyError:
            dropOffs['externDropOff' + str(i)] = False
        try:
            dropOffs['droppOff' + str(i)] = request.POST['form-' + str(i) + '-droppOff']
        except MultiValueDictKeyError:
            dropOffs['droppOff' + str(i)] = False
    return dropOffs


def create_assignment_entry(request):
    """
    render the create form manually because the date fields in form must be checked in an specific way
    :param request:
    :return: request, template_name, context
    """
    numbers = set([i for i in range(1, 1000)])
    forgiven_nums = set([obj.internal_progress_number for obj in PriolisteAssignment.objects.all()])
    data = {'created_at': datetime.now(), 'finished_until': datetime.now()}
    uploaded_files = []
    form_class = CreateForm
    hardware_formset = formset_factory(HardwareCreateForm, formset=BaseLinkFormSet, min_num=1)
    if request.method == 'POST':
        dropOffs = check_dropOffs(request)
        data = {
            'form-TOTAL_FORMS': '5',
            'form-INITIAL_FORMS': '0',
            'form-MAX_NUM_FORMS': '',
            'form-0-number': request.POST['form-0-number'],
            'form-0-type': request.POST['form-0-type'],
            'form-0-batterie': request.POST['form-0-batterie'],
            'form-0-droppOff': dropOffs['droppOff0'],
            'form-0-externDropOff': dropOffs['externDropOff0'],
            'form-0-prodRecOne': uploaded_files.append(try_file(request, 'form-0-prodRecOne')),
            'form-0-addon': request.POST['form-0-addon'],
            'form-1-number': request.POST['form-1-number'],
            'form-1-type': request.POST['form-1-type'],
            'form-1-batterie': request.POST['form-1-batterie'],
            'form-1-droppOff': dropOffs['droppOff1'],
            'form-1-externDropOff': dropOffs['externDropOff1'],
            'form-1-prodRecOne': uploaded_files.append(try_file(request, 'form-1-prodRecOne')),
            'form-1-addon': request.POST['form-1-addon'],
            'form-2-number': request.POST['form-2-number'],
            'form-2-type': request.POST['form-2-type'],
            'form-2-batterie': request.POST['form-2-batterie'],
            'form-2-droppOff': dropOffs['droppOff2'],
            'form-2-externDropOff': dropOffs['externDropOff2'],
            'form-2-prodRecOne': uploaded_files.append(try_file(request, 'form-2-prodRecOne')),
            'form-2-addon': request.POST['form-2-addon'],
            'form-3-number': request.POST['form-3-number'],
            'form-3-type': request.POST['form-3-type'],
            'form-3-batterie': request.POST['form-3-batterie'],
            'form-3-droppOff': dropOffs['droppOff3'],
            'form-3-externDropOff': dropOffs['externDropOff3'],
            'form-3-prodRecOne': uploaded_files.append(try_file(request, 'form-3-prodRecOne')),
            'form-3-addon': request.POST['form-3-addon'],
            'form-4-number': request.POST['form-4-number'],
            'form-4-type': request.POST['form-4-type'],
            'form-4-batterie': request.POST['form-4-batterie'],
            'form-4-droppOff': dropOffs['droppOff4'],
            'form-4-externDropOff': dropOffs['externDropOff4'],
            'form-4-prodRecOne': uploaded_files.append(try_file(request, 'form-4-prodRecOne')),
            'form-4-addon': request.POST['form-4-addon'],
        }
        formset = hardware_formset(data)
        form = form_class(request.POST)
        hardware_string = ''
        for f in formset.cleaned_data:
            if f['number'] is not None:
                addon = ''
                if f['addon']:
                    addon += ' und ' + f['addon']
                if f['droppOff']:
                    hardware_string += str(f['number']) + 'x ' + str(f['type']) + ' ' + str(f['batterie']) +\
                                       ' mit DO ' + addon + '<br>'
                    if f['externDropOff']:
                        hardware_string += str(f['number']) + 'x ' + str(f['type']) + ' ' + str(f['batterie']) + \
                                       ' mit DO ' + addon + ' + externem DO <br>'
                elif f['externDropOff']:
                    hardware_string += str(f['number']) + 'x ' + str(f['type']) + ' ' + str(f['batterie']) +\
                                       ' + externem DO' + '<br>'
                elif f['addon']:
                    hardware_string += str(f['number']) + 'x ' + str(f['type']) + ' ' + str(f['batterie']) + addon + '<br>'
                else:
                    hardware_string += str(f['number']) + 'x ' + str(f['type']) + ' ' + str(f['batterie']) + '<br>'
        if form.is_valid():
            prod_rec_string = ''
            for _ in uploaded_files:
                prod_rec_string += _ + '$'
            created_at = datetime.today()
            time_in_weeks = ProductionTime.objects.get(enabled=True).time_in_weeks

            finished_until = created_at + timedelta(days=int(time_in_weeks)*7)

            #save the form first and then change the field values and save it again
            assignment = form.save()
            assignment.hardware = hardware_string
            assignment.created_at = created_at
            assignment.finished_until = finished_until
            assignment.prod_rec_string = prod_rec_string
            assignment.status = 'Vertrieb'
            assignment.internal_progress_number = list(numbers - forgiven_nums)[0]
            assignment.time_in_weeks = time_in_weeks
            assignment.save()
            return redirect(reverse('pListe:home'))
        else:
            return render(request, template_name='assignment_form.html', context={
                'form': CreateForm(initial=data),
                'form_errors': form.errors,
                'hardware_form': formset_factory(HardwareCreateForm, extra=5),
            })
    return render(request, template_name='assignment_form.html', context={
        'form': CreateForm(initial=data),
        'hardware_form': formset_factory(HardwareCreateForm, extra=5),
    })


def show_specifc_batterie_type(request, path):
    if request.method == 'POST':
        form = BatterieSearchForm(request.POST)
        if form.is_valid():
            batterie_type = form['batterie_type'].value()
            if batterie_type == '------':
                if 'missingbatteries' in path:
                    return redirect(reverse('pListe:batterie'))
                elif 'missingbelts' in path:
                    return redirect(reverse('pListe:belts'))
                elif 'prioListe_done' in path:
                    return redirect(reverse('pListe:done'))
                else:
                    return redirect(reverse('pListe:home'))
            else:
                if 'prioListe_done' in path:
                    liste = PriolisteAssignment.objects.filter(hardware__contains=batterie_type).filter(status='Löschen')
                else:
                    liste = PriolisteAssignment.objects.filter(hardware__contains=batterie_type).exclude(
                        status='Löschen')
            counter = []
            for col in liste:
                hardware = col.hardware.split(' ')
                counter.append(int(hardware[0].replace('x', '')))

            to_do = sum(counter)
            context = {
                'object_list': liste,
                'batterie_search': BatterieSearchForm,
                'prio_search': Search_Everything,
                'to_do': to_do
            }
            return render(request, template_name='assignment_list.html', context=context)
    else:
        redirect_main(request)


def search_form(request, path):
    if request.method == 'POST':
        form = Search_Everything(request.POST)
        if form.is_valid():
            search_string = form['to_search'].value()
            if search_string == '':
                if 'missingbatteries' in path:
                    return redirect(reverse('pListe:batterie'))
                elif 'missingbelts' in path:
                    return redirect(reverse('pListe:belts'))
                elif 'prioListe_done' in path:
                    return redirect(reverse('pListe:done'))
                else:
                    return redirect(reverse('pListe:home'))
            else:
                if '-' in search_string:
                    try:
                        founded_pk = filter_ids(PriolisteAssignment, search_string)
                    except ValueError:
                        founded_pk = None
                else:
                    founded_pk = None

                tmp = PriolisteAssignment.objects.filter(internal_progress_number__iexact=str(search_string))

                if 'prioListe_done' in path:
                    if len(tmp) < 1:
                        if founded_pk is not None:
                            tmp = PriolisteAssignment.objects.filter(pk=founded_pk).filter(status='Löschen')
                        tmp = tmp | PriolisteAssignment.objects.filter(ids__icontains=search_string).filter(status='Löschen')
                        if len(tmp) < 1:
                            tmp = PriolisteAssignment.objects.filter(customer__icontains=search_string).filter(status='Löschen')
                            if len(tmp) < 1:
                                tmp = PriolisteAssignment.objects.filter(status__icontains=search_string).filter(
                                    status='Löschen')
                                tmp2 = PriolisteAssignment.objects.filter(optional_status__icontains=search_string).\
                                    exclude(status__icontains=search_string).filter(status='Löschen')
                                if len(tmp) < 1 and len(tmp2) > 1:
                                    tmp = tmp2
                                else:
                                    tmp = tmp2.union(tmp)
                                if len(tmp) < 1:
                                    tmp = PriolisteAssignment.objects.filter(staff__iexact=search_string)
                                    if len(tmp) < 1:
                                        tmp = PriolisteAssignment.objects.filter(co_worker__icontains=search_string)
                                        if len(tmp) < 1:
                                            tmp = PriolisteAssignment.objects.filter(ordering_number__icontains=search_string)

                else:
                    if len(tmp) < 1:
                        if founded_pk is not None:
                            tmp = PriolisteAssignment.objects.filter(pk=founded_pk).exclude(status='Löschen')
                        tmp = tmp | PriolisteAssignment.objects.filter(ids__icontains=search_string).exclude(status='Löschen')
                        if len(tmp) < 1:
                            tmp = PriolisteAssignment.objects.filter(customer__icontains=search_string).exclude(status='Löschen')
                            if len(tmp) < 1:
                                tmp = PriolisteAssignment.objects.filter(status__icontains=search_string).exclude(
                                    status='Löschen')
                                tmp2 = PriolisteAssignment.objects.filter(optional_status__icontains=search_string).\
                                    exclude(status__icontains=search_string).exclude(status='Löschen')
                                if len(tmp) < 1 and len(tmp2) > 1:
                                    tmp = tmp2
                                else:
                                    tmp = tmp2.union(tmp)
                                if len(tmp) < 1:
                                    tmp = PriolisteAssignment.objects.filter(staff__iexact=search_string)
                                    if len(tmp) < 1:
                                        tmp = PriolisteAssignment.objects.filter(co_worker__icontains=search_string)
                                        if len(tmp) < 1:
                                            tmp = PriolisteAssignment.objects.filter(ordering_number__icontains=search_string)
                tmp = tmp | PriolisteAssignment.objects.filter(production_remark__icontains=search_string)
                context = {
                    'object_list': tmp,
                    'batterie_search': BatterieSearchForm,
                    'prio_search': Search_Everything,
                }
                if 'prioListe_done' not in path:
                    return render(request, template_name='assignment_list.html', context=context)
                else:
                    return render(request, template_name='assignment_done_list.html', context=context)
        else:
            if 'missingbatteries' in path:
                return redirect(reverse('pListe:batterie'))
            elif 'missingbelts' in path:
                return redirect(reverse('pListe:belts'))
            elif 'prioListe_done' in path:
                return redirect(reverse('pListe:done'))
            else:
                return redirect(reverse('pListe:home'))
    else:
        redirect_main(request)


def redirect_main(request):
    liste = PriolisteAssignment.objects.all().exclude(status='Löschen')
    context = {
        'object_list': liste,
        'batterie_search': BatterieSearchForm,
        'prio_search': Search_Everything,
    }
    return render(request, template_name='assignment_list.html', context=context)


def redirect_to_where_i_was(request, path, internal_progress_number):
    if 'missingbatteries' in path:
        response = redirect(reverse('pListe:batterie'))
        response['Location'] += '?obj=' + str(internal_progress_number)
        return response
    elif 'missingbelts' in path:
        response = redirect(reverse('pListe:belts'))
        response['Location'] += '?obj=' + str(internal_progress_number)
        return response
    else:
        response = redirect(reverse('pListe:home'))
        response['Location'] += '?obj=' + str(internal_progress_number)
        return response


def notice_about_delete(request, pk):
    if request.method == 'POST':
        obj = PriolisteAssignment.objects.get(pk=pk)
        obj.delete()
        return redirect(reverse('pListe:done'))
    else:
        obj = PriolisteAssignment.objects.get(pk=pk)
        context = {
            'obj': obj
        }
        return render(request, 'noticeAboutDelete.html', context)
