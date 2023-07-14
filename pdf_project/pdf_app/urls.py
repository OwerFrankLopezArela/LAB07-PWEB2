from django.urls import path
from .views import PDFView, PDFDownloadView

app_name = 'pdf_app'

urlpatterns = [
    path('pdf/', PDFView.as_view(), name='pdf'),
    path('download/', PDFDownloadView.as_view(), name='download'),
]
