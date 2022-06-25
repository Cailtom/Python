import time, turtle, sys
import datetime as dt

# Titulo e Configurações
turtle.title('Horas em tempo REAL')
turtle.bgcolor('#0ff')
Tela = turtle.Screen()
Tela.setup(height=130, width=300)

# Conteudos de exibição
estiloHoras = turtle.Turtle()
estiloHoras.color('#333333')
estiloHoras.goto(-90, -25) # Posição do tempo

estiloBorda = turtle.Turtle()
estiloBorda.pensize(4) #Largura da borda
estiloBorda.color('#333333')
estiloBorda.penup()
estiloBorda.goto(-100, -30) #Posição das bordas
estiloBorda.pendown()

# Chamada das horas
segundos = dt.datetime.now().second
minutos = dt.datetime.now().minute
horas = dt.datetime.now().hour

for i in range(2):
    estiloBorda.forward(210)
    estiloBorda.left(90)
    estiloBorda.forward(70)
    estiloBorda.left(90)

estiloBorda.hideturtle()

while True:
    estiloHoras.hideturtle()
    estiloHoras.clear()

    estiloHoras.write(
        str(horas).zfill(2)

        + ":" + str(minutos).zfill(2) + ":"
        + str(segundos).zfill(2),

        font=('Arial Narrow', 35, 'bold')
    )

    time.sleep(1)
    segundos += 1

    if segundos == 60:
        segundos = 0
        minutos += 1

    if minutos == 60:
        minutos = 0
        horas += 1

    if horas == 13:
        horas = 1

