
from django.urls import path
from . import views

urlpatterns = [
    path('diaper/', views.DiaperList.as_view(), name='Diaper_list'),
    path('diaperdetail/<int:pk>', views.DiaperDetail.as_view(), name='Diaper_Details'),






    path('diapercomment/', views.DiaperCommentList.as_view(), name='Diaper_Comments_list'),
    path('diapercomment/<int:pk>', views.DiaperCommentDetail.as_view(), name='Diaper_Comment_detail'),








    path('bottle/', views.BottleList.as_view(), name='Bottle_list'),
    path('bottlecomment/', views.BottleCommentList.as_view(), name='Bottle_Comments_list'),
    path('bottlecomment/<int:pk>', views.BottleCommentDetail.as_view(), name='Bottle_Comment_detail'),

    path('bottlenipple/', views.BNList.as_view(), name='Bottle_Nipple_list'),
    path('bottlenipple/<int:pk>', views.BNListDetail.as_view(), name='Bottle_Nipple_detail'),
    path('bncomment/', views.BNCommentList.as_view(), name='Bottle_Nipple_Comments_list'),
    path('bncomment/<int:pk>', views.BNCommentDetail.as_view(), name='Bottle_Nipple_Comment_detail'),
]
