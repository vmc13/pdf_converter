from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def GeneratePDF(lista):
    try:
        nome_pdf = input('Informe o nome do PDF: ')
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 720
        for nome,idade in lista.items():
            x -= 20
            pdf.drawString(247,x, f'{nome} : {idade}')
        pdf.setTitle(nome_pdf)
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(245,750, 'Lista de Convidados')
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(245,724, 'Nome e idade')
        pdf.save()
        print(f'{nome_pdf}.pdf criado com sucesso!')
    except:
        print(f'Erro ao gerar {nome_pdf}.pdf')

lista = {'Rafaela': '19', 'Jose': '15', 'Maria': '22','Eduardo':'24'}

GeneratePDF(lista)