from django.urls import path
from webapp import views


app_name = 'webapp'

urlpatterns = (
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('blog/', views.LBlogView.as_view(), name='blog'),
    path('blog/<int:pk>/', views.DetailBlogView.as_view(), name='blog_detail'),
    path('contact/', views.contact, name='contact'),
)

