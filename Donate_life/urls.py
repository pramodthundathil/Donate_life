from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

import Home
from Home import urls
import Products
from Products import urls
from Adminaction import urls
import Adminaction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(Home.urls)),
    path("products/",include(Products.urls)),
    path("Adminaction/",include(Adminaction.urls))
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
