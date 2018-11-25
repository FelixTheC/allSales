from django.views.generic import TemplateView
import importlib
from .settings import INSTALLED_APPS


class MainView(TemplateView):
    template_name = 'allOverview.html'

    def get_routes(self):
        routes = []
        apps = [i for i in INSTALLED_APPS if 'django' not in i]
        classes = []
        for m in [importlib.import_module(f'{i}.models') for i in apps if 'models' in importlib.import_module(i).__dict__]:
            dic = m.__dict__
            for k, v in enumerate(dic):
                if '__' not in v:
                    classes.append(v)
        for m in [importlib.import_module(f'{i}.models') for i in apps if 'models' in importlib.import_module(i).__dict__]:
            dic = m.__dict__
            routes.append([dic[i] for i in classes if i in dic and hasattr(dic[i], 'get_main_root')])
        return [i[0] for i in routes if len(i) > 0]

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['routes'] = self.get_routes()
        return context