from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),

    path('fetch_user_stats/', views.fetch_user_stats, name='fetch_user_stats'),
    path('stats/<str:username>/', views.user_stats, name='user_stats'),

    path('visualization/demo/', views.demo_visualization, name='demo_visualization'),
    path('visualization/options/<str:username>/', views.visualization_options, name='visualization_options'),
    path('visualization/start/<str:username>/', views.start_visualization, name='start_visualization'),
    #path('visualization/loading/<int:visualization_id>/', views.loading_visualization, name='loading_visualization'),
    path('visualization/result/<str:username>/<int:visualization_id>/', views.visualization_result, name='visualization_result'),

    path('account/', views.account, name='account'),

    path('about/', views.about, name='about'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', views.register, name='register'),
]