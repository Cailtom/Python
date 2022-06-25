from tkinter import *
from tkinter import messagebox
from pytube import YouTube

# root
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Cailton - 2022")

imagem_Fundo = Canvas(root, bg="blue", height=100, width=400)
imagem_bg = PhotoImage(file="fundo_1.png")
background_root = Label(root, image=imagem_bg)
background_root.place(x = 0, y = -60, relwidth=1, relheight=1)

# Colocar o link
link = StringVar()

Label(
    root, text="Coloque o link aqui:", font=("Helvetica", 15, "italic"), border=0, bd=0
).place(x=170, y=180)

aceitar_link = Entry(
    root, width=70, textvariable=link).place(x=35, y=210)

# Função para baixar o vídeo
def Baixar():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()

    Label(
        root, text="BAIXADO!", font=("arial", 15), bg="#00bfff",  border=8
    ).place(x = 200, y = 240)

Button(
    root, text="BAIXAR", font=("arial", 15, "bold"), bg="#333333", bd=0,
    padx=2, command=Baixar
).place(x = 200, y = 240)

imagem_Fundo.pack()
root.mainloop()