"""pro_mod URL Configuration

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
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addtopic/',views.create_topic,name="create_topic"),
    path('add_webpage/',views.create_web,name="add_webpage"),
    path('display_topic/',views.display_topic,name="display_topic"),
   # path('display_topic/<id>',views.display_topic,name="display_topic"),
    path('display_web/',views.display_webpage,name="display_webpage"),
   # path('display_web/<webid>',views.display_webpage,name="display_webpage"),
    #path('search_web/',views.search_webpage,name="search_web"),
    path('disp_img/<id>',views.disp_img,name="disp_image"),
    path('topic_form/',views.topic_modelform,name="topicmodel_form"),
    path('webform/',views.webform,name="webform"),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
