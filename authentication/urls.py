from django.urls import path
from .views import register, login_user, login_flutter, logout_user, show_all_user, show_user_loggedin

app_name = 'authentication'

urlpatterns = [
  path('register/', register, name='register'),
  path('login/', login_user, name='login'), 
  path('login-flutter/', login_flutter, name='login-flutter'), # login flutter
  path('logout/', logout_user, name='logout'),
  path('show-all-user/json/', show_all_user, name='show-all-user'),
  path('show-user-loggedin/json/', show_user_loggedin, name='show-user-loggedin')
]