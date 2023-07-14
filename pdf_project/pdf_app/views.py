from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from reportlab.pdfgen import canvas


class PDFView(View):
    def get(self, request):
        data = {
            'nombre': 'Juan',
            'apellido': 'Pérez',
            'edad': 25
        }

        template = get_template('pdf_app/template.html')
        html = template.render(data)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="archivo.pdf"'

        p = canvas.Canvas(response)

        p.setFont("Helvetica", 12)
        p.drawString(100, 700, "Información Personal")
        p.drawString(100, 650, "Nombre: {}".format(data['nombre']))
        p.drawString(100, 600, "Apellido: {}".format(data['apellido']))
        p.drawString(100, 550, "Edad: {}".format(data['edad']))

        p.showPage()
        p.save()

        return response
