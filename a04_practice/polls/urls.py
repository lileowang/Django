from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/detail', views.detail, name='detail'),
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('<int:pk>', views.ResultsView.as_view(), name='results'),
]
