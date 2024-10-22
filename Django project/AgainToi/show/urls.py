from django.urls import path
from .views import all_profiles_list, add_host, add_photographer, add_camera_operator, add_dancer, add_singer, add_show_profile

urlpatterns = [
    path('profiles/', all_profiles_list, name='all_profiles_list'),
    path('add-host/', add_host, name='add_host'),
    path('add-photographer/', add_photographer, name='add_photographer'),
    path('add-camera-operator/', add_camera_operator, name='add_camera_operator'),
    path('add-dancer/', add_dancer, name='add_dancer'),
    path('add-singer/', add_singer, name='add_singer'),
    path('add-show-profile/', add_show_profile, name='add_show_profile'),
]
