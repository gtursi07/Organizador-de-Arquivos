import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Tipos de arquivos e suas pastas correspondentes
extensoes = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Vídeos": [".mp4", ".avi", ".mov", ".mkv"],
    "Áudios": [".mp3", ".wav", ".flac"],
    "Compactados": [".zip", ".rar", ".7z"],
}

# Função para organizar os arquivos
def organizar_arquivos(pasta):
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)
        if os.path.isfile(caminho_arquivo):
            movido = False
            for pasta_tipo, tipos in extensoes.items():
                if any(arquivo.lower().endswith(ext) for ext in tipos):
                    pasta_destino = os.path.join(pasta, pasta_tipo)
                    os.makedirs(pasta_destino, exist_ok=True)
                    shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))
                    movido = True
                    break
            if not movido:
                pasta_destino = os.path.join(pasta, "Outros")
                os.makedirs(pasta_destino, exist_ok=True)
                shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))
    messagebox.showinfo("Sucesso", "Arquivos organizados com sucesso!")

# Função para escolher pasta
def escolher_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        organizar_arquivos(pasta)

# Configuração da interface
root = tk.Tk()
root.title("Organizador de Arquivos")
root.geometry("300x150")

label = tk.Label(root, text="Escolha a pasta para organizar:", font=("Arial", 12))
label.pack(pady=20)

btn_escolher = tk.Button(root, text="Selecionar Pasta", command=escolher_pasta, width=20)
btn_escolher.pack()

root.mainloop()
