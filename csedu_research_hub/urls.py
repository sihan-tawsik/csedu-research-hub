"""csedu_research_hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from .settings import __version__, MEDIA_ROOT

urlpatterns = [
    re_path(r"^account", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path(f"api/{__version__}/auth/", include("rest_auth.urls")),
    path(
        f"api/{__version__}/auth/registration/", include("rest_auth.registration.urls")
    ),
    path(f"api/{__version__}/pdf/", include("pdf.urls")),
    path(f"api/{__version__}/profile/", include("accounts.urls")),
]

urlpatterns += [
    url(
        r"^media/(?P<path>.*)$",
        serve,
        {"document_root": MEDIA_ROOT, "show_indexes": True},
    )
] + staticfiles_urlpatterns()
