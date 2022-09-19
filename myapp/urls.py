from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('/login/', LoginView.as_view(), name='login'),
    path('news/', NewsView.as_view(), name='news'),
    path('contacts/', ContactsList.as_view(), name='contacts'),
    path('courses_list/', CoursesList.as_view(), name='courses_list'),
    path('doc_site/', DocSiteList.as_view(), name='doc_site')

]
