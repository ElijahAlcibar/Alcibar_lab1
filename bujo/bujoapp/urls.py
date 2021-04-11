from django.urls import path

from .views import (
	HomePageView, ProfilePageView, KeyPageView, ThisWeekPageView, TodayPageView,
	ChangeNicknameView, ChangeBioView, AddKeyView, AddThisWeekView, 
	EditThisWeekView, DeleteThisWeekView, DoneThisWeekView, AddTodayView, 
	EditTodayView, DeleteTodayView, DoneTodayView
)

urlpatterns = [
	path('home', HomePageView, name='home'),
	path('profile', ProfilePageView.as_view(), name='profile'),
	path('key', KeyPageView.as_view(), name='key'),
	path('this_week', ThisWeekPageView.as_view(), name='this_week'),
	path('today', TodayPageView.as_view(), name='today'),

	path('nickname_change', ChangeNicknameView, name="nickname_change"),
	path('bio_change', ChangeBioView, name="bio_change"),
	
	path('add_key', AddKeyView, name="add_key"),

	path('add_task_this_week', AddThisWeekView, name="add_task_this_week"),
	path('edit_task_this_week/<str:pk>/', EditThisWeekView, name="edit_task_this_week"),
	path('delete_task_this_week/<str:pk>/', DeleteThisWeekView, name="delete_task_this_week"),
	path('done_task_this_week/<str:pk>/', DoneThisWeekView, name="done_task_this_week"),

	path('add_task_today', AddTodayView, name="add_task_today"),
	path('edit_task_today/<str:pk>/', EditTodayView, name="edit_task_today"),
	path('delete_task_today/<str:pk>/', DeleteTodayView, name="delete_task_today"),
	path('done_task_today/<str:pk>/', DoneTodayView, name="done_task_today"),
]
