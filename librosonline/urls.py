"""
URL configuration for librosonline project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', include('vistaprevia.urls')),
   #path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('contacto/', include('contacto.urls')),
    path('tienda/', include('tienda.urls')),
    path('usuario/', include('usuario.urls')),  
]  +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
