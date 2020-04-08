from django.urls import path
from .views import home, home_logout

urlpatterns = [
    path('', home, name='home'),
    path('logout/', home_logout, name='home_logout'),

]