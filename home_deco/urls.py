from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from products import views as products_views
from contact import views as contact_views
from django.conf import settings

urlpatterns = [
    path('', core_views.home, name='home'),
    path('about/', core_views.about, name='about'),
    path('products/', products_views.products, name='products'),
    path('contact/', contact_views.contact, name='contact'),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    # Path de autenticación
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
=======
    path('administracion/', core_views.administracion, name='administracion'),
    path('administracion/indexcat', core_views.indexcat, name='indexcat'),
    path('administracion/crear_producto', core_views.ProductoView.as_view(), name='crear_producto'),
    path('administracion/editar_producto/<int:id_prod>/', core_views.prod_editar, name='prod_editar'),
    path('administracion/eliminar_producto/<int:id>/', core_views.prod_eliminar, name='prod_eliminar'),
    path('administracion/crear_categoria', core_views.CategoryView.as_view(), name='crear_categoria'),
    path('administracion/editar_categoria/<int:id_cat>/', core_views.cat_editar, name='cat_editar'),
    path('administracion/eliminar_categoria/<int:id>/', core_views.cat_eliminar, name='cat_eliminar'),

>>>>>>> form-ara
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )
