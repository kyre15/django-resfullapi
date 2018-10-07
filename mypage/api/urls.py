from django.urls import path

from .views import postListView, postDetailView

urlpatterns = [
    path('', postListView.as_view()),
    path('<pk>', postDetailView.as_view()),

]
