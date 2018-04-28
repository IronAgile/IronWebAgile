from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics import renderPDF
from IronAgileWebApp.models import *
from IronAgileWebApp.views.api import *

from rest_framework.reverse import reverse

def generate_invitation(request, id):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invitation.pdf"'

    p = canvas.Canvas(response)
    evenement = Evenement.objects.get(id=id)
    concerner = Concerner.objects.get(fk_evenement=evenement, fk_userProfile=request.user)
    qrw = QrCodeWidget(reverse('concerner-detail', args=[concerner.id]))
    b = qrw.getBounds()
    w = b[2] - b[0]
    h = b[3] - b[1]


    p.drawString(30, 750, 'Invitation à : ' + evenement.__str__())
    p.drawString(30, 720, 'Veuillez conserver cette invitation ainsi que le QRCode')

    d = Drawing(400, 400, transform=[300. / w, 0, 0, 300. / h, 0, 0])
    d.add(qrw)

    renderPDF.draw(d, p, 1, 1)

    p.showPage()
    p.save()
    return response