import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Cadastro do aluno")
janela.geometry("400x350")  
janela.resizable(False, False)

# Frame principal
frame = tk.Frame(janela, padx=20, pady=20)
frame.pack(fill="both", expand=True)

# Título
titulo = tk.Label(frame, text="Cadastro de Aluno", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# Email
label_email = tk.Label(frame, text="E-mail:", font=("Arial", 10))
label_email.pack(anchor="w", pady=(10, 0))
entry_email = tk.Entry(frame, font=("Arial", 10), width=30)
entry_email.pack(pady=(0, 10))

# Senha
label_senha = tk.Label(frame, text="Senha:", font=("Arial", 10))
label_senha.pack(anchor="w", pady=(10, 0))
entry_senha = tk.Entry(frame, font=("Arial", 10), width=30, show="*")
entry_senha.pack(pady=(0, 10))

# Confirmação de Senha
label_conf_senha = tk.Label(frame, text="Confirmar Senha:", font=("Arial", 10))
label_conf_senha.pack(anchor="w", pady=(10, 0))
entry_conf_senha = tk.Entry(frame, font=("Arial", 10), width=30, show="*")
entry_conf_senha.pack(pady=(0, 20))

def cadastrar():
    email = entry_email.get()
    senha = entry_senha.get()
    conf_senha = entry_conf_senha.get()
    
    # Validações
    if not email or not senha or not conf_senha:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
        return
    
    if "@" not in email or "." not in email:
        messagebox.showerror("Erro", "E-mail inválido!")
        return
    
    if len(senha) < 6:
        messagebox.showerror("Erro", "Senha deve ter no mínimo 6 caracteres!")
        return
    
    if senha != conf_senha:
        messagebox.showerror("Erro", "As senhas não conferem!")
        return
    
    # Sucesso
    messagebox.showinfo("Sucesso", f"Aluno cadastrado com sucesso!\nE-mail: {email}")
    entry_email.delete(0, tk.END)
    entry_senha.delete(0, tk.END)
    entry_conf_senha.delete(0, tk.END)

def limpar():
    entry_email.delete(0, tk.END)
    entry_senha.delete(0, tk.END)
    entry_conf_senha.delete(0, tk.END)

# Botões
frame_botoes = tk.Frame(frame)
frame_botoes.pack(fill="x", pady=10)

btn_cadastrar = tk.Button(frame_botoes, text="Cadastrar", command=cadastrar, bg="#4CAF50", fg="white", font=("Arial", 10), width=10)
btn_cadastrar.pack(side="left", padx=5)

btn_limpar = tk.Button(frame_botoes, text="Limpar", command=limpar, bg="#2196F3", fg="white", font=("Arial", 10), width=10)
btn_limpar.pack(side="left", padx=5)

janela.mainloop()