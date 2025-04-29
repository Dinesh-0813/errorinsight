# main.py

import tkinter as tk
from tkinter import scrolledtext, messagebox
from error_parser import suggest_fix

def analyze_error():
    error_log = error_text.get("1.0", tk.END).strip()
    if not error_log:
        messagebox.showwarning("Warning", "Please enter an error log first.")
        return

    suggestions = suggest_fix(error_log)
    result_text.config(state='normal')
    result_text.delete("1.0", tk.END)
    for s in suggestions:
        result_text.insert(tk.END, "- " + s + "\n")
    result_text.config(state='disabled')

app = tk.Tk()
app.title("ErrorInsight – Python Error Fixer GUI")
app.geometry("700x500")
app.resizable(False, False)

tk.Label(app, text="Paste Python Error Log:", font=("Arial", 12)).pack(pady=5)
error_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, height=10, font=("Courier", 10))
error_text.pack(padx=10, pady=5, fill="both")

tk.Button(app, text="Analyze Error", command=analyze_error, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=10)

tk.Label(app, text="Suggestions:", font=("Arial", 12)).pack()
result_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, height=8, font=("Courier", 10), state='disabled', bg="#f0f0f0")
result_text.pack(padx=10, pady=5, fill="both")

app.mainloop()
