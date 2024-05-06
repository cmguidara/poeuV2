from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'paginas/index.html'

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'

class ContatoView(TemplateView):
    template_name = 'paginas/contato.html'
