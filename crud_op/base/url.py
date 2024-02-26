from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home' ),
    path('adduser',views.adduser,name='adduser'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('signup',views.signup,name='signup'),
    path('logout',views.signout,name='logout'),
    path('signin',views.signin,name='signin'),
    path('profile',views.profile,name='profile')
]