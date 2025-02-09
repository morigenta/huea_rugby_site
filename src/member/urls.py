from django.urls import path
from . import views

app_name = 'member'

urlpatterns = [
    path('', views.MemberListView.as_view(), name='list'),
    path('<int:pk>', views.MemberDetailView.as_view(), name='detail'),
]