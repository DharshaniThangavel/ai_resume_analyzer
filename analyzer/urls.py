from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_resume, name='upload_resume'),
    path('report/<int:report_id>/', views.view_report, name='view_report'),
    path('history/', views.history_view, name='history'),  # <--- Added history route
]