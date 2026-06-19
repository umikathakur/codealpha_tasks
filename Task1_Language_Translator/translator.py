from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

# Function to translate text
def translate_text():
    try:
        text = input_text.get("1.0", END).strip()
        target = language_var.get()

        translated = GoogleTranslator(
            source='auto',
            target=target
        ).translate(text)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        output_text.delete("1.0", END)
        output_text.insert(END, f"Error: {e}")

# Main Window
root = Tk()
root.title("Language Translator")
root.geometry("600x450")

# Heading
heading = Label(
    root,
    text="Language Translator",
    font=("Arial", 18, "bold")
)
heading.pack(pady=10)

# Input Label
Label(root, text="Enter Text:", font=("Arial", 12)).pack()

# Input Text Box
input_text = Text(root, height=6, width=60)
input_text.pack(pady=5)

# Language Selection
Label(root, text="Select Language:", font=("Arial", 12)).pack()

language_var = StringVar()
language_dropdown = ttk.Combobox(
    root,
    textvariable=language_var,
    width=20
)

language_dropdown['values'] = (
    "hi",
    "fr",
    "es",
    "de",
    "ja"
)

language_dropdown.current(0)
language_dropdown.pack(pady=5)

# Translate Button
translate_button = Button(
    root,
    text="Translate",
    command=translate_text,
    font=("Arial", 12)
)
translate_button.pack(pady=10)

# Output Label
Label(root, text="Translated Text:", font=("Arial", 12)).pack()

# Output Text Box
output_text = Text(root, height=6, width=60)
output_text.pack(pady=5)

root.mainloop()