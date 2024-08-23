"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from drf_yasg import openapi
from django.contrib import admin
from drf_yasg.views import get_schema_view
from django.urls import path, include, re_path

from .views import root_view

schema_view = get_schema_view(
   openapi.Info(
      title="Library API",
      default_version='v1',
      description="API for managing books in a library",
   ),
   public=True,
)

urlpatterns = [
    # application admin
    path('admin/', admin.site.urls),
    # documentation
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # base
    path('', root_view, name='root'),

    # application library
    path('', include("apps.library.urls", namespace="book")),
    path('', include("apps.accounts.urls", namespace="account")),
]
