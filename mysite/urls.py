"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('common.urls', namespace='common')),
    path('rooms/', include('rooms.urls', namespace='rooms')),
    path('users/', include('users.urls', namespace='users')),
    path('reservations/', include('reservations.urls', namespace='reservations')),
    path('reviews/', include('reviews.urls', namespace='reviews')),
    path('lists/', include('lists.urls', namespace='lists')),
    path('conversations/', include('conversations.urls', namespace='conversations')),
    path(os.environ.get('ADMIN'), admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
