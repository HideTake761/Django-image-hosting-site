from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'), # urlとして'accounts:'は必要だが'timeline:'を書かなくていい理由。
    path('delete/<int:data_id>/', views.preview, name='delete'),
    path('create', views.create, name='create'),
    path('<int:num>', views.list, name='list'),
]
