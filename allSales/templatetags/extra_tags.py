from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='find_word')
@stringfilter
def find_word(value, arg):
    if arg in value:
        return True
    else:
        return False


@register.filter(name='check_box_name')
@stringfilter
def check_box_name(value):
    box_name = len(value.strip().split('-')[0])
    print(value[0])
    if box_name < 2:
        if value[0] != '0':
            return 'B00' + value
        else:
            return 'B' + value
    elif 2 <= box_name < 3:
        if value[0] != '0':
            return 'B0' + value
        else:
            return 'B' + value
    else:
        return 'B' + value


@register.filter(name='string_to_list')
@stringfilter
def string_to_list(value):
    liste = value.split('$')
    return liste


@register.filter(name='cut_string')
@stringfilter
def cut_string(value):
    new_string = ''.join(value.split('/')[2:])
    return new_string


@register.filter(name='find_and_replace')
@stringfilter
def find_and_replace(value, arg):
    if value is not None:
        return value.replace('$', arg)
    else:
        return value


@register.filter(name='replace_whitespace')
@stringfilter
def replace_whitespace(value, arg):
    if value is not None:
        return value.replace(' ', arg)
    else:
        return value


@register.filter(name='replace_with_empty')
@stringfilter
def replace_with_empty(value, arg):
    if value is not None:
        return value.replace(arg, '')
    else:
        return value


@register.filter(name='split_by_space_return_second')
@stringfilter
def split_by_space_return_second(value):
    if value is not None:
        try:
            return value.split(' ')[2]
        except:
            return value
    else:
        return value


@register.filter(name='split_by_arg')
@stringfilter
def split_by_arg(value, arg):
    if value is not None:
        try:
            return value.split(arg)
        except:
            return value
    else:
        return value


@register.filter(name='get_index')
def get_index(value, arg):
    try:
        return value[arg]
    except IndexError:
        return value[0]


@register.filter(name='get_value_by_key')
def get_value_by_key(value, arg):
    try:
        return value[arg]
    except KeyError:
        return ''


@register.filter(name='truncate_word')
def truncate_word(value, arg):
    nums = arg * -1
    return str(value)[nums:]


@register.filter(name='semicolontobr')
def semicolontobr(value):
    try:
        val = value.replace(';', ';<br>')
    except AttributeError:
        val = value
    return val


#@TODO find a name
@register.filter(name='tmp')
def tmp(value, arg=';'):
    try:
        val = value.split(arg)
        counter = 0
        new_list = []
        for i in val:
            if counter % 4 == 0 and counter != 0:
                new_list.append(f'<br>{i.strip()}')
            else:
                new_list.append(i.strip())
            counter += 1
        arg += ' '
        val = arg.join(new_list)
    except AttributeError:
        val = value
    return val