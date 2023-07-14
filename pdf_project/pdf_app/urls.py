from django.urls import path
from .views import PDFView

app_name = 'pdf_app'

urlpatterns = [
    path('pdf/', PDFView.as_view(), name='pdf'),
]
