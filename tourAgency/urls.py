from django.urls import path

from . import views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('', views.HotelsView.as_view(), name='main'),
    path('myorders/', views.MyOrdersView.as_view(), name='my_orders'),
    path('<slug:slug>/', views.HotelDetailView.as_view(), name='hotel_detail'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),
    path('order/<slug:slug>/', views.OrderView.as_view(), name='order'),
    path('myorders/', views.MyOrdersView.as_view(), name='my_orders'),

]