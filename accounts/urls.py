from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import EditProfile, Login, Register, ResetPass, ResetPassDone, RestPassComplate, RestPassConfirm, SearchUser, UserProfile, Explore

app_name = 'accounts'

urlpatterns = [
    path('search/', SearchUser.as_view(), name='search'),
    path('reset/', ResetPass.as_view(), name='reset'),
    path('resetdone/', ResetPassDone.as_view(), name='resetdone'),
    path('resetdoneconfirm/<uidb64>/<token>',
         RestPassConfirm.as_view(), name='resetdoneconfirm'),
    path('resetdonecomplete/', RestPassComplate.as_view(),
         name='resetdonecomplete'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('explore/', Explore.as_view(), name='explore'),
    path('search/', SearchUser.as_view(), name='search'),
    path('<str:user>/', UserProfile.as_view(), name='profile'),
    path('<str:user>/edit/', EditProfile.as_view(), name='editprofile'),

]
