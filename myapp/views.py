from tempfile import tempdir
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class IndexView(TemplateView):
    template_name: str = 'index.html'


class LoginView(TemplateView):
    template_name: str = 'login.html'


class NewsView(TemplateView):
    template_name: str = 'news.html'


class CoursesList(TemplateView):
    template_name: str = 'courses_list.html'


class ContactsList(TemplateView):
    template_name: str = 'contacts.html'


class DocSiteList(TemplateView):
    template_name: str = 'doc_site.html'
