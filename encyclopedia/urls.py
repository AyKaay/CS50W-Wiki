from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entry/<str:title>/", views.entry_page, name="entry_page"),
    path("wiki/<str:title>/", views.entry_page, name="entry_page"),
    path("search/", views.search, name="search"),
    path("new_page/<str:title>", views.new_page, name="new_page"),
    path("new_page/", views.create_entry, name="new_page"),
    path('edit/<str:title>/', views.edit_entry, name='edit_entry'),
    path("random/", views.random_entry, name="random_entry"),
    path("about_page/", views.about_page, name="about_page"),
]
