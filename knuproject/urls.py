"""knuproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import url
from django.views.generic import TemplateView

from knu.dash_apps.finished_apps import plotly_apps    # pylint: disable=unused-import
from knu.dash_apps.finished_apps import dash_apps      # pylint: disable=unused-import
from knu.dash_apps.finished_apps import bootstrap_app  # pylint: disable=unused-import

from django_plotly_dash.views import add_to_session
from knu import views


urlpatterns = [
    path('knu/', include('knu.urls')),
    path('', include('knu.urls')),
    path('member/', include('django.contrib.auth.urls')),
    path('member/', include('member.urls')),
    path('admin/', admin.site.urls),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),

]
