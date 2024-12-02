from fpdf import FPDF

projeto = input("Digite o nome do projeto: ")
horas_estimadas = input("Digite o total de horas estimadas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo = input("Digite o prazo de entrega: ")

valor_total = float(horas_estimadas) * float(valor_hora)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.image("template.png", x=0, y=0)

pdf.text(115,145,projeto)
pdf.text(115,160,horas_estimadas)
pdf.text(115,175,valor_hora)
pdf.text(115,190,prazo)
pdf.text(115,205,str(valor_total))

pdf.output("Orcamento.pdf")
print("Orçamento gerado com sucesso!")