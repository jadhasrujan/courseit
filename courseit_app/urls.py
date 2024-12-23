from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('programs/', views.programs, name='programs'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('login/', views.user_login, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.logout_user, name='logout'),
    path('course_info/<int:course_id>/', views.course_info, name='course_info'),
    path('course_instructor/<int:course_id>/', views.course_instruct, name='course_instructor'),

]