from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
from io import BytesIO
from xhtml2pdf import pisa

class PDFView(View):
    def get(self, request):
        template = get_template('pdf_app/pdf_template.html')
        context = {'nombre_variable': 'Hola, mundo!'}
        html = template.render(context)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        
        if not pdf.err:
            response = HttpResponse(response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="archivo.pdf"'
            return response

        return HttpResponse("Error al generar el PDF", status=500)
