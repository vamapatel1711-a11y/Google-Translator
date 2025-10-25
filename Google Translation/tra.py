import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

def translate_text():
    try:
        src_lang = source_lang_combo.get()
        dest_lang = target_lang_combo.get()
        text_to_translate = input_text.get("1.0", tk.END).strip()

        if not text_to_translate:
            messagebox.showwarning("Input Error", "Please enter text to translate!")
            return

        translated = GoogleTranslator(source=src_lang, target=dest_lang).translate(text_to_translate)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror("Error", f"Translation failed!\n\n{e}")

root = tk.Tk()
root.title("🌍 Google Translator (Python 3.13 Compatible)")
root.geometry("600x450")
root.config(bg="#f5f5f5")

title_label = tk.Label(root, text="Google Translator", font=("Arial", 20, "bold"), bg="#f5f5f5", fg="#2c2c2c")
title_label.pack(pady=10)

frame = tk.Frame(root, bg="#f5f5f5")
frame.pack(pady=5)

languages = [
    "auto", "en", "hi", "gu", "fr", "es", "de", "zh-cn", "ja", "ru", "ar", "it", "ko", "ta", "mr", "bn"
]

source_lang_combo = ttk.Combobox(frame, values=languages, width=20)
source_lang_combo.set("auto")  
source_lang_combo.grid(row=0, column=0, padx=10)

target_lang_combo = ttk.Combobox(frame, values=languages, width=20)
target_lang_combo.set("hi")  
target_lang_combo.grid(row=0, column=1, padx=10)

tk.Label(root, text="Enter text:", bg="#f5f5f5", font=("Arial", 12)).pack()
input_text = tk.Text(root, height=6, width=60)
input_text.pack(pady=5)

translate_button = tk.Button(root, text="Translate", font=("Arial", 12, "bold"), bg="#0078D7", fg="white",
                             command=translate_text, relief=tk.RAISED, cursor="hand2")
translate_button.pack(pady=10)

tk.Label(root, text="Translated text:", bg="#f5f5f5", font=("Arial", 12)).pack()
output_text = tk.Text(root, height=6, width=60)
output_text.pack(pady=5)

root.mainloop()
