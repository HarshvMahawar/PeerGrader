# peer_grading_app/urls.py

from django.urls import path
from .views import create_assignment, instructor_view
from .views import instructor_home_view, create_rubrics

urlpatterns = [
    path('instructor_home/', instructor_home_view, name='instructor_home'),
    path('create_assignment/', create_assignment, name='create_assignment'),
    path('create_rubrics/<int:assignment_id>/', create_rubrics, name='create_rubrics'),
]
