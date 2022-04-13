from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

nomes = ['caio', 'marcos', 'joao']

def mm2p(milimetros):
    return milimetros / 0.352777

cnv = canvas.Canvas("meu_pdf.pdf", pagesize=A4)

cnv.drawString(mm2p(100), mm2p(150), "Teste")

cnv.save()

