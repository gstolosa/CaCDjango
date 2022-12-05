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
    # Path de autenticación
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )
