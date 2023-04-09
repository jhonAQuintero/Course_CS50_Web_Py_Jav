from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry_page, name="title"),
    path("search", views.search_page, name="search"),
    path('create-page', views.form_create_page, name='create-page'),
    path('wiki/edit/<str:title>', views.form_edit_page, name='edit-page'),
    path('rdn-entry', views.random_page, name='rdn-page')
]
