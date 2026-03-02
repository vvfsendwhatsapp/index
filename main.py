import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import urllib.parse
import csv

# Funzione invio messaggio
def invia():
    numero = combo_numero.get().strip()
    messaggio = text_messaggio.get("1.0", tk.END).strip()
    if not numero:
        messagebox.showerror("Errore", "Seleziona un numero")
        return
    testo_codificato = urllib.parse.quote(messaggio)
    link = f"https://wa.me/{numero}?text={testo_codificato}"
    webbrowser.open(link)

# Legge rubrica CSV (opzionale)
numeri = []
try:
    with open("contacts.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row: numeri.append(row[0])
except FileNotFoundError:
    numeri = []

# Interfaccia grafica
root = tk.Tk()
root.title("WhatsApp Portable")
root.geometry("400x300")

tk.Label(root, text="Seleziona numero:").pack(pady=5)
combo_numero = ttk.Combobox(root, values=numeri, width=30)
combo_numero.pack()

tk.Label(root, text="Messaggio:").pack(pady=5)
text_messaggio = tk.Text(root, height=8, width=40)
text_messaggio.pack()

tk.Button(root, text="Invia WhatsApp", command=invia, bg="green", fg="white").pack(pady=10)

root.mainloop()
