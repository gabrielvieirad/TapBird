from main import *
from tkinter import *

janela = Tk()
janela.title('Tap Bird - Gabriel Vieira')

janela.geometry('400x224')
janela.resizable(0, 0)

# Dimensões da Janela
largura = 400
altura = 224

# Resolução do sistema
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()

# Posição janela

posx = largura_screen / 2 - largura / 2
posy = altura_screen / 2 - altura / 2

# Definição da geometria

janela.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

# Interação / visual do sistema

img2 = PhotoImage(file="imgs/definitivof.png")
label_img2 = Label(janela, image=img2).pack()

botao = Button(janela, text='Iniciar',
               highlightbackground='black',
               highlightthickness=3,
               bd=2,
               height=2,
               width=8,
               bg='#ffff63',
               fg='#353535',
               font=('verdana', 8, 'bold'),
               command=main)
botao.place(x=160, y=175)

janela.mainloop()
