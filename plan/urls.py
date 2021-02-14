from django.urls import path
from . import views


urlpatterns = [
    path('plan/', views.goals_main,name='plan-main'),
    path('plan/day-<str:username>', views.ShowDays.as_view(),name='plan-day'),
    path('plan/day-<str:username>/add', views.CreateDays.as_view(),name='day-add'),
    path('plan/day-<str:username>/<int:pk>', views.DayDetailView.as_view(),name='day-detail'),
    path('plan/day-<str:username>/<int:pk>/delete', views.DayGoalDeleteView.as_view(),name='day-detail-delete'),
]

