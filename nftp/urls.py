
from django.urls import path
from . import views

urlpatterns = [
    path('diaper/', views.DiaperList.as_view(), name='Diaper_list'),
    path('diapercomment/', views.DiaperCommentList.as_view(), name='Diaper_Comment_list'),
]
