from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='questions'),
    path('<int:question_id>/', views.detail, name='questions_detail'),
    path('<int:question_id>/vote', views.vote, name='questions_vote'),
]
