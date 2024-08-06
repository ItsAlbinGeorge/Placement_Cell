from django.urls import path
from . import views
urlpatterns=[
    path('',views.login,name='login',),
    path('register/',views.register,name='register'),
    path('verify_otp/',views.verify_otp,name='verify_otp'),
    path('profile/',views.profile,name='profile'),
    path('joblisting/',views.joblisting,name='joblisting'),
    path('about/',views.about,name='about'),
    path('privacy/',views.privacy,name='privacy'),
    path('support/',views.support,name='support'),
    path('terms/',views.terms,name='terms'),
    path('update/',views.update,name='update'),
    path('company/<int:company_id>/',views.company,name='company'),
    path('logout/',views.logout,name='logout'),
]