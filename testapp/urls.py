from django.urls import path
from testapp import views


urlpatterns = [
    path('love/', views.page_count),
    path('form1/', views.regform, name='Registration Form'),
]