from django.contrib import admin
from django.urls import path, include
from app import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('catalog/', include('goods.urls')),
    path('user/', include('users.urls')),
    path('cart/', include('carts.urls')),
    path('orders/', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns+=[path('__debug__/', include('debug_toolbar.urls'))]
    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
