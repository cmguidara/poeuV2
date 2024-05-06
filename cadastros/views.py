from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Empresa, Vaga

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django.shortcuts import get_object_or_404


# Create your views here.

#Views para criação de cadastros
class EmpresaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Empresa
    fields = ['cnpj', 'nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-empresas')

class VagaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Vaga
    fields = ['nome', 'descricao', 'link', 'empresa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):

        #Antes do super não foi criada a vaga

        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        #dDepois do super a vaga está criada

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Vagas"

        return context


#Views para alteração de cadastros

class EmpresaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Empresa
    fields = ['cnpj', 'nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-empresas')

class VagaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Vaga
    fields = ['nome', 'descricao', 'link', 'inativa', 'empresa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):

        #self.object = Vaga.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        self.object = get_object_or_404(Vaga, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Atualizar Vaga"
        return context



#Views para exclusão de cadastros

class EmpresaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Polo"
    model = Empresa
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-empresas')

class VagaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Polo"
    model = Vaga
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        #self.object = Vaga.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        self.object = get_object_or_404(Vaga, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


#Views para listar cadastros
class EmpresaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Empresa
    template_name = 'cadastros/listas/empresa.html'

class VagaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Vaga
    template_name = 'cadastros/listas/vaga.html'

    def get_queryset(self):
        self.object_list = Vaga.objects.filter(usuario=self.request.user)
        return self.object_list

class AlunoList(ListView):
    model = Vaga
    template_name = 'cadastros/listas/aluno.html'

class AnuncioList(ListView):
    model = Vaga
    fields = ['nome', 'descricao', 'link', 'empresa']
    template_name = 'cadastros/form.html'





