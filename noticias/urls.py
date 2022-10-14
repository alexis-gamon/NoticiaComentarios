from django.urls import path, include

from .views import NoticiasListView, NoticiasTemplateView, NoticiasPageDetail, NoticiasPagesCreate, NoticiasPageUpdate, NoticiasPageDelete, ComentariosCreateView
#from .views import homeTemplateView, noticiasTemplateView, NoticiasListView, NoticiasPageDetail, NoticiasPagesCreate, NoticiasPageUpdate, NoticiasPageDelete


urlpatterns = [

    ##path('',homeTemplateView.as_view(), name='home'),
  #  path('Noticias/',NoticiasTemplateView.as_view(), name='Noticias'),
    path('Noticias/',NoticiasTemplateView.as_view(), name='Noticias'),
    path('', NoticiasListView.as_view(), name='lista_noticias'),
### Detalle
    path('<int:pk>/', NoticiasPageDetail.as_view(), name='noticia_detalle'),
### Crear
    path('nuevo/', NoticiasPagesCreate.as_view(), name="noticia_nueva"),
### Modificar


    path('<int:pk>/editar/', NoticiasPageUpdate.as_view(), name="noticia_editar"),

### Borrar 
    path('<int:pk>/eliminar/', NoticiasPageDelete.as_view(), name="noticia_eliminar"),




    path('<int:pk>/Comentario/',ComentariosCreateView.as_view(), name='Comentario'),


]