from django.views.generic import TemplateView
from webapp.forms import ProcessForm

class IndexView(TemplateView):
    template_name = 'webapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProcessForm()
        return context