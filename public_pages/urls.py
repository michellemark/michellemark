"""
@Copyright Michelle Mark 2018
@author Michelle Mark

"""
from django.urls import path

from . import views


urlpatterns = [
    path('contact/', views.ContactMeView.as_view(), name='contact-form'),
    path('permute/', views.PermuteView.as_view(), name='permute-form'),
    path('projects', views.ProjectsView.as_view(), name="projects_main"),
    path('simple-grocery-list', views.SimpleGroceryListView.as_view(), name="simple_grocery_list"),
    path('thanks/', views.ContactMeThanksView.as_view(), name='contact-form-thanks'),
    path('', views.HomeView.as_view(), name='home'),
]
