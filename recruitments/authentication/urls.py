from django.urls import path
from rest_framework import routers

from recruitments.authentication.views import RegisterView, LoginView

app_name = "authentication"
#
# router = routers.SimpleRouter()
# router.register('register', RegisterView.as_view(), basename='register')
# router.register('login', LoginView.as_view(), basename='login')
#
# urlpatterns = router.urls

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
]