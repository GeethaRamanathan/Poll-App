from django.urls import path
from . import views

app_name = "poll"

urlpatterns = [
    path('',views.PollListView.as_view(),name="poll_list"),
    path('<int:pk>/',views.PollDetailView.as_view(),name="poll_detail"),
    path('vote/<int:question_id>/',views.vote,name="vote"),
    path('result/<int:pk>/',views.PollResultView.as_view(),name="poll_result"),
    ]