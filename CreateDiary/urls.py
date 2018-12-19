from django.urls import path
from . import views 

urlpatterns=[
            path('',views.CreateDiaryUserView,name='CreateDiayUserView'),
            path('Home',views.CreateDiaryUserView,name='CreateDiaryUserView'),
            path('Login',views.SUserLoginFormView,name='SUserLoginFormView'),
            path('Profile/<slug:slug>',views.ViewProfile,name='ViewProfile'),
            path('NewEntry/<slug:slug>',views.NewEntryView,name='NewEntryView'),
            path('Features',views.ViewFeatures,name='ViewFeatures'),
            path('Privacy',views.ViewPrivacy,name='ViewPrivacy'),
            path('AboutUs',views.ViewAboutUs,name='ViewAboutUs'),
            path('SaporaInc',views.ViewSaporaInc,name='ViewSaporaInc'),
            path('User/<slug:slug>',views.Display,name='Display'),
            path('Diary/<slug:slug>/<int:pk>',views.ViewDiary,name='ViewDiary'),
]