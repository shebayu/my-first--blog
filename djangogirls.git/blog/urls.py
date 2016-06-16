from django.cong.urls impot url
from . import views

urlpatterns = [
    url(r'^$', views.post_list,name= 'post_list'),
    ]



