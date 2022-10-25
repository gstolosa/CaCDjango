from django.contrib import admin
from django.urls import path
from core import views as core_views
from products import views as products_views
from django.conf import settings

urlpatterns = [
    path('', core_views.home, name='home'),
    path('about_us/', core_views.about_us, name='about_us'),
    path('products/', products_views.products, name='products'),
    path('contact/', core_views.contact, name='contact'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )
