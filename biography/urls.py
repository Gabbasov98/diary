from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='home'),
    path('diary/', views.ShowDailyView.as_view(),name='diary'),
    path('diary/<int:pk>', views.DailyDetailView.as_view(),name='diary-detail'),
    path('diary/<int:pk>/update', views.UpdateDailyView.as_view(),name='diary-update'),
    path('diary/<int:pk>/delete', views.DeleteDiaryView.as_view(),name='diary-delete'),
    path('diary/add', views.CreateDailyView.as_view(),name='diary-add'),
]