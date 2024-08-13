"""
URL configuration for travel_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from travel_app.views import DestinationListCreate
# from django.conf import settings
# from django.conf.urls.static import static
#
# router = DefaultRouter()
# router.register(r'destinations', DestinationViewSet)
# urlpatterns = [
#                   path('admin/', admin.site.urls),
#                   path('', include('travel_app.urls')),
# \
#                  # path('api/', include('router.urls')),
#               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# tourist_destinations/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('travel_app.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

