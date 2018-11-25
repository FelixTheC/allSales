from collections import Counter
from datetime import datetime
import re
import pandas as pd
from bokeh.models import ColumnDataSource, HoverTool
from django.shortcuts import render
from bokeh.embed import components
from bokeh.transform import dodge
from bokeh.plotting import figure, output_file, show
from rma.models import Refurbisment
from warranty.models import Warranty
from collar.models import Vasdevice


def test_statistic(request):
    refurbishments = Refurbisment.objects.filter(parcel_received__year=datetime.today().year)
    last_year_refurbishments = Refurbisment.objects.filter(parcel_received__year=datetime.today().year-1)

    this_year_countries = [r.country for r in refurbishments if not r.country.isdigit() and 'test' not in r.country]
    last_year_countries = [r.country for r in last_year_refurbishments if not r.country.isdigit() and 'test' not in r.country]

    count_countries = Counter(this_year_countries)
    last_year_count_countries = Counter(last_year_countries)

    this_year_data = {
        'countries': [key for key in count_countries.keys()],
        'values': [value for value in count_countries.values()],
    }

    last_year_data = {
        'countries': [key for key in last_year_count_countries.keys()],
        'values': [value for value in last_year_count_countries.values()],
    }

    source = ColumnDataSource(data=this_year_data)
    last_year_source = ColumnDataSource(data=last_year_data)

    plot = figure(x_range=[keys for keys in count_countries.keys()], plot_width=1200, plot_height=400,
                  title='Refurbishments by countries for ' + str(datetime.today().year))

    plot.vbar(x='countries', width=0.5,
              top='values', color="firebrick", source=source)

    plot.xaxis.major_label_orientation = 1

    plot.add_tools(HoverTool(tooltips=[('Value', '@values'), ]))

    last_year_plot = figure(x_range=[keys for keys in last_year_count_countries.keys()], plot_width=1200, plot_height=400,
                  title='Refurbishments by countries for ' + str(datetime.today().year-1))

    last_year_plot.vbar(x='countries', width=0.5, bottom=0,
              top='values', color='firebrick', source=last_year_source)

    last_year_plot.xaxis.major_label_orientation = 1

    last_year_plot.add_tools(HoverTool(tooltips=[('Value', '@values'), ]))

    script, div = components(plot)
    last_year_script, last_year_div = components(last_year_plot)

    context = {
        'bokeh_div': div,
        'bokeh_script': script,
        'last_div': last_year_div,
        'last_script': last_year_script,
    }

    return render(request, 'statistic.html', context)


def warranty_statistic(request):
    warranties = Warranty.objects.filter(date__year__gte='2016')
    warrantie_dict = dict()
    vas_devices = dict()
    what = ['warranty', 'shipped']

    test = [([c.producttype for c in w.customer_collar.all()], w.date_delivery, w.date_collar_failure) for w in warranties]

    df = pd.DataFrame(test, columns=['prodType', 'deliveryDate', 'dateFailure'])
    prodType = df['prodType']
    types_list = []
    for i in prodType:
        for p in i:
            types_list.append(p.name)

    warrantie_dict = Counter(types_list)

    for key, values in warrantie_dict.items():
        vas_devices[key] = len(Vasdevice.objects.filter(producttype__name=key).filter(shippingdate__year__gte=2016))

    data = {
        'devices': [keys for keys, items in warrantie_dict.items()],
        'warranty': [items for keys, items in warrantie_dict.items()],
        'shipped': [items for keys, items in vas_devices.items()],
    }

    source = ColumnDataSource(data=data)

    plot = figure(x_range=[keys for keys, items in warrantie_dict.items()], plot_width=1200, plot_height=400,
                  title='Warranties by Collar-Types since 01.01.2017')

    plot.vbar_stack(what, x='devices', width=0.5, color=['firebrick', 'blue'],
                    source=source, legend=(what[0], what[1]))

    plot.add_tools(HoverTool(tooltips=[("Shippings", "@shipped"), ("Warranty", "@warranty")]))

    plot.xaxis.major_label_orientation = 1

    script, div = components(plot)
    context = {
        'bokeh_div': div,
        'bokeh_script': script,
    }
    return render(request, 'statistic.html', context)


def remove_words(text):
    _ = ''
    if 'and' in text:
        text.replace('and', ',')
    elif '&' in text:
        text.replace('&', ',')
    else:
        _ = re.sub(r'[a-zA-Z@%$()-]+', '', string=text)
    return _.replace(' ', '').split(',')


def count_numbers_in_list(liste):
    counter = 0
    for element in liste:
        try:
            if int(element):
                counter += 1
        except ValueError:
            pass
    return counter


def delivery_statistics(request):
    years = list(set([i.shippingdate.year for i in Vasdevice.objects.only('shippingdate') if i.shippingdate is not None]))
    shippings = Vasdevice.objects.only('shippingdate').filter(shippingdate__year=sorted(years)[-1])
    last_year_shippings = Vasdevice.objects.only('shippingdate').filter(shippingdate__year=sorted(years)[-2])

    df_tmp = pd.DataFrame({
        'months': [i for i in range(1, 13)]
    })

    df_last = pd.DataFrame({
        'months': [i for i in range(1, 13)]
    })

    df_past_years = pd.DataFrame({
        'past_years': sorted(years)[1:]
    })

    for i in sorted(years):
        df_past_years.loc[df_past_years['past_years'] == i, 'value'] = len(Vasdevice.objects.filter(shippingdate__year=i))

    for i in range(1, 13):
        df_tmp.loc[df_tmp['months'] == i, 'value'] = len([data.shippingdate.month for data in shippings if data.shippingdate.month == i])
        df_tmp.loc[df_tmp['months'] == i, 'last_year_value'] = len([data.shippingdate.month for data in last_year_shippings if data.shippingdate.month == i])
        df_last.loc[df_last['months'] == i, 'value'] = len([data.shippingdate.month for data in last_year_shippings if data.shippingdate.month == i])

    source = ColumnDataSource(df_tmp)
    last_source = ColumnDataSource(df_last)
    past_years_source = ColumnDataSource(df_past_years)

    plot = figure(plot_width=1200, plot_height=350,
                  title=f'Shippings {sorted(years)[-1]} - {sorted(years)[-2]} in direct comparison ')

    plot.vbar(x=dodge('months', -0.25, range=plot.x_range), width=0.5,
              top='last_year_value', color='blue', source=source, legend=(str(sorted(years)[-2])))

    plot.vbar(x=dodge('months', 0.0, range=plot.x_range), width=0.5,
              top='value', color='firebrick', source=source, legend=(str(sorted(years)[-1])))

    plot.x_range.range_padding = 0.08
    plot.y_range.range_padding = 0.1

    plot_last = figure(plot_width=1200, plot_height=350,
                  title='Shippings last year')

    plot_last.vbar(x='months', width=0.5,
              top='value', color="firebrick", source=last_source)

    past_years_plot = figure(plot_width=1200, plot_height=350,
                  title='Shippings the last years')

    past_years_plot.line(x='past_years', y='value', line_width=2, source=past_years_source)

    plot.add_tools(HoverTool(tooltips=[(f'Year:{sorted(years)[-1]}', "@value"), (f'Year:{sorted(years)[-2]}', "@last_year_value"), ("Months", "@months")]))

    plot.legend.location = "top_left"
    plot.legend.orientation = "horizontal"

    plot_last.add_tools(HoverTool(tooltips=[("Value", "@value"), ("Months", "@months")]))
    past_years_plot.add_tools(HoverTool(tooltips=[("Value", "@value"), ("Year", "@past_years")]))

    script, div = components(plot)
    last_years_script, last_years_div = components(plot_last)
    past_years_script, past_years_div = components(past_years_plot)

    context = {
        'bokeh_div': div,
        'bokeh_script': script,
        'months': df_tmp['months'].tolist(),
        'value': df_tmp['value'].tolist(),
        'last_months': df_last['months'].tolist(),
        'last_value': df_last['value'].tolist(),
        'past_years': list(df_past_years['past_years']),
        'past_value': list(df_past_years['value']),
        'last_div': last_years_div,
        'last_script': last_years_script,
        'past_years_div': past_years_div,
        'past_years_script': past_years_script,

    }

    return render(request, 'statistic.html', context)
