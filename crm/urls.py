from django.urls import path

from crm import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('search/', views.SearchResultView.as_view(), name='search'),

]
