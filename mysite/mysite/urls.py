"""
URL configuration for mysite project.

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
from django.contrib import admin
from django.urls import path
# import your views like the following
from project.views  import home, about, contact_us, Custom_Order
from django.conf import settings
from django.conf.urls.static import static #import static setting you just added
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
    path('contact/',contact_us),
    path('Custom_Order/', Custom_Order, name="Custom_Order")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # add the part after plus sign (+)
