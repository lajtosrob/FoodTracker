from django.urls import path
from .views import FoodDetail, FoodList, ImageDetail, ImageList, UserDetail, UserList, index, kaloriatabla

from . import views

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('SMILE.html', views.SMILE, name='SMILE'),
    path('BMI.html', views.BMI, name='BMI'),
    path('BMR.html', views.BMR, name='BMR'),
    path('BMR szuk.html', views.BMR_szuk, name='BMR_szuk'),
    path('index.html', views.index, name='index'),
    path('kaloriatabla.html', views.kaloriatabla, name='kaloriatabla'),
    path('', views.food_list, name='food_list'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('profile/weight', views.weight_log_view, name='weight_log'),
    path('profile/weight/delete/<int:weight_id>', views.weight_log_delete, name='weight_log_delete'),

    path('food/list', views.food_list_view, name='food_list'),
    path('food/add', views.food_add_view, name='food_add'),
    path('food/foodlog', views.food_log_view, name='food_log'),
    path('food/foodlog/delete/<int:food_id>', views.food_log_delete, name='food_log_delete'),
    path('food/<str:food_id>', views.food_details_view, name='food_details'),

    path('categories', views.categories_view, name='categories_view'),
    path('categories/<str:category_name>', views.category_details_view, name='category_details_view'),

    path('food/', FoodList.as_view()),
    path('food/<int:pk>/', FoodDetail.as_view()),
    
    path('image/', ImageList.as_view()),
    path('image/<int:pk>/', ImageDetail.as_view()),

    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
    path('szexkalóriatáblázat.html', views.szexkaloriatablazat, name='szexkaloriatablazat'),
    path('forum.html', views.forum, name='forum'),
    

]
