import tkinter as tk
from tkinter import ttk, messagebox
import random


class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Caesar Cipher")
        self.root.geometry("700x600")
        self.root.configure(bg='#0a0a0a')

        print("App started!")  # Debug

        # Modern color palette
        self.colors = {
            'bg_dark': '#0a0a0a',
            'bg_panel': '#1a1a2e',
            'accent_blue': '#1a3a5f',
            'accent_magenta': '#ff00ff',
            'accent_purple': '#8a2be2',
            'accent_cyan': '#00ffff',
            'text_primary': '#ffffff',
            'text_secondary': '#b0b0b0',
        }

        # Create main widget first
        self.create_widgets()

    def create_widgets(self):
        print("Creating widgets...")  # Debug

        # Main container
        main_frame = tk.Frame(self.root, bg=self.colors['bg_panel'])
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Title
        title_label = tk.Label(main_frame, text="🔐 CAESAR CIPHER",
                               bg=self.colors['bg_panel'], fg=self.colors['accent_cyan'],
                               font=('Arial', 20, 'bold'))
        title_label.pack(pady=10)

        # Intro text
        intro_text = """Welcome! This is a simple encryption tool that shifts letters in your message.
Example: With shift 3, 'ABC' becomes 'DEF'"""

        intro_label = tk.Label(main_frame, text=intro_text,
                               bg=self.colors['bg_panel'], fg=self.colors['text_primary'],
                               font=('Arial', 10), justify='center')
        intro_label.pack(pady=10)

        # Input section
        input_frame = tk.Frame(main_frame, bg=self.colors['bg_panel'])
        input_frame.pack(fill='x', padx=10, pady=10)

        tk.Label(input_frame, text="📝 Input Text:",
                 bg=self.colors['bg_panel'], fg=self.colors['text_primary'],
                 font=('Arial', 11)).pack(anchor='w', pady=5)

        self.input_text = tk.Text(input_frame, height=4,
                                  bg=self.colors['bg_dark'], fg=self.colors['text_primary'],
                                  font=('Arial', 10), wrap='word',
                                  borderwidth=2, relief='sunken')
        self.input_text.pack(fill='x', pady=5)

        # Example button
        tk.Button(input_frame, text="Try Example",
                  bg=self.colors['accent_magenta'], fg='white',
                  font=('Arial', 9, 'bold'),
                  command=self.insert_example).pack(anchor='w', pady=5)

        # Shift section
        shift_frame = tk.Frame(main_frame, bg=self.colors['bg_panel'])
        shift_frame.pack(fill='x', padx=10, pady=10)

        tk.Label(shift_frame, text="🔧 Shift Value:",
                 bg=self.colors['bg_panel'], fg=self.colors['text_primary'],
                 font=('Arial', 11)).pack(anchor='w', pady=5)

        self.shift_var = tk.IntVar(value=3)

        # Scale and label
        scale_frame = tk.Frame(shift_frame, bg=self.colors['bg_panel'])
        scale_frame.pack(fill='x', pady=5)

        shift_scale = tk.Scale(scale_frame, from_=1, to=25, variable=self.shift_var,
                               orient='horizontal', length=400,
                               bg=self.colors['bg_panel'], fg=self.colors['text_primary'],
                               troughcolor=self.colors['accent_blue'])
        shift_scale.pack(side='left', fill='x', expand=True)

        self.shift_label = tk.Label(scale_frame, text="3",
                                    bg=self.colors['accent_purple'], fg='white',
                                    font=('Arial', 12, 'bold'), width=3)
        self.shift_label.pack(side='left', padx=10)

        shift_scale.configure(command=self.update_shift_label)

        # Buttons section
        button_frame = tk.Frame(main_frame, bg=self.colors['bg_panel'])
        button_frame.pack(fill='x', padx=10, pady=10)

        # Encrypt button
        encrypt_btn = tk.Button(button_frame, text="🚀 ENCRYPT",
                                bg=self.colors['accent_blue'], fg='white',
                                font=('Arial', 11, 'bold'), padx=20, pady=10,
                                command=self.encrypt)
        encrypt_btn.pack(side='left', padx=5, expand=True, fill='x')

        # Decrypt button
        decrypt_btn = tk.Button(button_frame, text="🔓 DECRYPT",
                                bg=self.colors['accent_purple'], fg='white',
                                font=('Arial', 11, 'bold'), padx=20, pady=10,
                                command=self.decrypt)
        decrypt_btn.pack(side='left', padx=5, expand=True, fill='x')

        # Clear button
        clear_btn = tk.Button(button_frame, text="🗑️ CLEAR",
                              bg=self.colors['accent_magenta'], fg='white',
                              font=('Arial', 11, 'bold'), padx=20, pady=10,
                              command=self.clear_text)
        clear_btn.pack(side='left', padx=5, expand=True, fill='x')

        # Output section
        output_frame = tk.Frame(main_frame, bg=self.colors['bg_panel'])
        output_frame.pack(fill='both', expand=True, padx=10, pady=10)

        tk.Label(output_frame, text="📤 Output Text:",
                 bg=self.colors['bg_panel'], fg=self.colors['text_primary'],
                 font=('Arial', 11)).pack(anchor='w', pady=5)

        self.output_text = tk.Text(output_frame, height=4,
                                   bg=self.colors['bg_dark'], fg=self.colors['text_primary'],
                                   font=('Arial', 10), wrap='word',
                                   state='disabled', borderwidth=2, relief='sunken')
        self.output_text.pack(fill='both', expand=True, pady=5)

        print("Widgets created successfully!")  # Debug

    def insert_example(self):
        examples = [
            "Hello! This is a secret message.",
            "Cryptography is fascinating!",
            "Julius Caesar used this cipher.",
            "Try encrypting your own text here!"
        ]
        example = random.choice(examples)
        self.input_text.delete("1.0", tk.END)
        self.input_text.insert("1.0", example)
        print("Example inserted!")  # Debug

    def update_shift_label(self, value):
        shift = int(float(value))
        self.shift_label.config(text=str(shift))
        print(f"Shift updated to: {shift}")  # Debug

    def caesar_cipher(self, text, shift, mode='encrypt'):
        result = ""

        for char in text:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                if mode == 'encrypt':
                    new_char = chr((ord(char) - start + shift) % 26 + start)
                else:
                    new_char = chr((ord(char) - start - shift) % 26 + start)
                result += new_char
            else:
                result += char

        return result

    def encrypt(self):
        print("Encrypt button clicked!")  # Debug
        input_text = self.input_text.get("1.0", tk.END).strip()
        if not input_text:
            messagebox.showwarning("Input Needed", "Please type a message to encrypt!")
            return

        shift = self.shift_var.get()
        encrypted_text = self.caesar_cipher(input_text, shift, 'encrypt')

        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", encrypted_text)
        self.output_text.config(state='disabled')

        messagebox.showinfo("Success!", "Your message has been encrypted! 🔒")

    def decrypt(self):
        print("Decrypt button clicked!")  # Debug
        input_text = self.input_text.get("1.0", tk.END).strip()
        if not input_text:
            messagebox.showwarning("Input Needed", "Please type a message to decrypt!")
            return

        shift = self.shift_var.get()
        decrypted_text = self.caesar_cipher(input_text, shift, 'decrypt')

        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", decrypted_text)
        self.output_text.config(state='disabled')

        messagebox.showinfo("Success!", "Your message has been decrypted! 🔓")

    def clear_text(self):
        print("Clear button clicked!")  # Debug
        self.input_text.delete("1.0", tk.END)
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state='disabled')


# Start the application
if __name__ == "__main__":
    print("Starting Caesar Cipher App...")
    root = tk.Tk()
    app = CaesarCipherApp(root)
    print("Running mainloop...")
    root.mainloop()
    print("App closed")