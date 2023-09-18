import os, sys
dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

import tkinter as tk
import subprocess
from tkinter import PhotoImage


def executarJogoSnake():
    subprocess.run('data/executaveis/snake', shell=True)

def executarJogoSpace():
    subprocess.run('data/executaveis/space', shell=True)
janela = tk.Tk()
janela.title("Projeto de Programação I - UPE Garanhuns")

imagemFundo = PhotoImage(file="data/images/p1.png")


fundoLabel = tk.Label(janela, image=imagemFundo)
fundoLabel.place(x=0, y=0, relwidth=1, relheight=1)

frameBotao = tk.Frame(janela)
frameBotao.pack(expand=True, fill='x')

estiloBotao = {'borderwidth': 2, 'relief': 'raised', 'bg': 'lightblue', 'fg': 'black', 'font': ('Helvetica', 12)}

botaoExecutarJogoSnake = tk.Button(frameBotao, text="JOGAR-SNAKE", command=executarJogoSnake, **estiloBotao)
botaoExecutarJogoSpaceInvaders = tk.Button(frameBotao, text="JOGAR-SPACE", command=executarJogoSpace, **estiloBotao)

botaoExecutarJogoSnake.pack(side='left',padx=10)
botaoExecutarJogoSpaceInvaders.pack(side='right', padx=10)

janela.mainloop()




