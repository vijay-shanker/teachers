from django.urls import path 
from school.views import SchoolListView, SchoolView

app_name="school"

urlpatterns = [
    path('/<int:pk>/', SchoolView.as_view(),  name="schools"),
    path('/list/', SchoolListView.as_view(),  name="schools")
]
