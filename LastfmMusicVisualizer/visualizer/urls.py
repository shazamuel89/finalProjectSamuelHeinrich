from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('stats/loading/<str:username>/', views.loading_user_stats, name='loading_user_stats'),
    path('stats/<str:username>/', views.user_stats, name='user_stats'),

    path('visualization/options/<str:username>/', views.visualization_options, name='visualization_options'),
    path('visualization/loading/<int:visualization_id>/', views.loading_visualization, name='loading_visualization'),
    path('visualization/result/<int:visualization_id>/', views.visualization_result, name='visualization_result'),

    path('account/', views.account, name='account'),

    path('about/', views.about, name='about')
]