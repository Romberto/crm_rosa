from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [

    path('', views.Main.as_view(), name="main"),
    path('new_case/', views.NewCase.as_view(), name="new_case"),
    path('my_case/', views.MyCase.as_view(), name="my_case"),
    path('more/<int:pk>', views.More.as_view(), name="more"),
    path('more/ajax-address/', views.ajax_address, name="ajax-address"),
    path('more/ajax-tags/', views.ajax_tags, name="ajax-tags"),
    path('more/ajax-comment/', views.ajax_comment, name="ajax-comment"),
    path('more/ajax-status/', views.ajax_status, name="ajax-status")

]
