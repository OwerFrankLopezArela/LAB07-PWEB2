from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from easy_pdf.rendering import render_to_pdf_response


class PDFView(View):
    def get(self, request):
        data = {
            'nombre': 'Ower',
            'apellido': 'Lopez',
            'edad': 18
        }
        pdf = render_to_pdf_response('pdf_app/template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
    
