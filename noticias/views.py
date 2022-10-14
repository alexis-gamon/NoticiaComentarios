
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Noticias, Comentario
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin##obliga a que estes logeado para poder visualizar una vista
from django.core.exceptions import PermissionDenied##valida los permisos


class NoticiasListView(ListView):
    model = Noticias
    template_name = 'lista_Noticias.html'
    context_object_name = 'lista_noticias'

 

# Create your views here.
class NoticiasTemplateView(ListView):
    template_name = 'noticia.html'
    model = Noticias
    context_object_name = 'Todas_noticias'

class homeTemplateView(TemplateView):
    template_name = 'home.html'



class NoticiasPageDetail(LoginRequiredMixin, DetailView):
    template_name = 'noticia_detalle.html'
    model = Noticias
    context_object_name = 'noticia'

class NoticiasPageDetail(LoginRequiredMixin, DetailView):
    template_name = 'noticia_detalle.html'
    model = Noticias
    context_object_name = 'noticia'
    
    login_url = 'login'

   

class NoticiasPagesCreate(LoginRequiredMixin,CreateView):
    template_name = 'noticia_nueva.html'
    model = Noticias
    #fields = ('Titulo', 'autor', 'Descripcion')#tendremos que quitar el autor ya que lo valida la persona que esta creando la validadcion
    fields = ('Titulo', 'Descripcion')
    ##validacion de que tienes que estar logeado para poder crear una noticia
    login_url = 'login'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
        ##obligas a la persona que este logeada
        
    login_url = 'login'

class NoticiasPageUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'noticia_editar.html'
    model = Noticias
    fields = ('Titulo', 'Descripcion')
   # fields = ('Titulo', 'autor', 'Descripcion')

    success_url = reverse_lazy('Noticias')

    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.autor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class NoticiasPageDelete(LoginRequiredMixin, DeleteView):
    template_name = 'noticia_eliminar.html'
    model = Noticias
    success_url = reverse_lazy('Noticias')

    login_url = 'login'

class ComentariosCreateView(LoginRequiredMixin,CreateView):
    template_name = 'agregar_comentario.html'
    model = Comentario
    fields = ('comentario',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.noticia_id = self.kwargs['pk']
        return super().form_valid(form)
        ##obligas a la persona que este logeada

