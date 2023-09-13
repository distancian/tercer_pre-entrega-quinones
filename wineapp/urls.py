"""
URL configuration for wineapp project.

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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wine_app/', include('wine_app.urls')),
    # path('agrega-cliente/<nombre>/<apellido>/<dni>/<mail>', cliente),
    # path('agrega-producto/<bodega>/<etiqueta>/<precio>', producto),
    # path('agrega-vendedor/<nombre>/<apellido>/<legajo>', vendedor),
    # path('listar_clientes', listar_clientes),
    # path('listar_productos', listar_productos),
    # path('listar_vendedores', listar_vendedores),

]
