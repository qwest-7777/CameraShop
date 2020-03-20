from django.urls import path
from .views import *
from . import views


app_name='camera'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:pk>/', views.category, name='category'),
    path('camera/<int:pk>/', views.camera_detail, name='camera_detail'),
    path('shops/', views.shops, name='shops'),
    path('delivery/', views.delivery, name='delivery'),
    path('payment/', views.payment, name='payment'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('feedback/', views.feedback, name='feedback'),
    path('signup/', views.signup, name='signup'),

]

api_url_patterns = [
	path("api/v1/store/camera/", CameraListView.as_view()),
    path("api/v1/store/camera/<id>/", DetailListView.as_view()),
    path("api/v1/store/characteristic/<camera>/", CharacteristicListView.as_view()),
    path("api/v1/store/shortdefenition/", ShortDefenitionListView.as_view()),
    path("api/v1/store/shortdefenitionimage/", ShortDefenitionImageListView.as_view()),
    path("api/v1/store/category/", CategoryListView.as_view()),
    path("api/v1/store/category/<id>/", CategoryDetailListView.as_view()),
    path("api/v1/store/filter/", FilterListView.as_view()),
    path("api/v1/store/filter/detail", FilterDetailListView.as_view()),
]

urlpatterns += api_url_patterns