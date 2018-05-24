from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics import renderPDF
from IronAgileWebApp.models import *
from IronAgileWebApp.views.api import *
from django.contrib.staticfiles.storage import staticfiles_storage

from rest_framework.reverse import reverse

from IronWebAgile.ironAgileWeb.settings import STATICFILES_DIRS


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
    p.setFont("Helvetica", 20)
    p.drawString(20, 800, "Invitation pour l'événement : "+evenement.titre)
    p.line(0, 750, 900, 750)
    p.setFont("Helvetica", 20)
    p.drawString(100, 700, "adresse : "+evenement.adresse)
    p.drawString(100, 650, "date : "+str(evenement.date))
    p.drawString(100, 600, "ville : " + evenement.ville)
    p.drawString(100, 550, "Code Postal : " + evenement.codePostal)
    p.drawString(100, 500, "heure : " + str(evenement.heure))
    p.drawImage(STATICFILES_DIRS[0] + 'windev.jpg', 300, 0, width=300, height=600)
    d = Drawing(400, 400, transform=[300. / w, 0, 0, 300. / h, 0, 0])
    d.add(qrw)

    renderPDF.draw(d, p, 1, 1)

    p.showPage()
    p.save()
    return response
