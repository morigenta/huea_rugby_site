from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='list'),  # ニュース一覧
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='detail'),  # 個別の記事
]