import tkinter as tk

class DisappearingTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disappearing Text App")

        self.text_var = tk.StringVar()
        self.text_var.set("Type something...")

        self.text_entry = tk.Entry(root, textvariable=self.text_var)
        self.text_entry.pack(pady=10)

        submit_button = tk.Button(root, text="Submit", command=self.submit_text)
        submit_button.pack()

        self.root.after(3000, self.vanish_text)  # Set the time (in milliseconds)

    def submit_text(self):
        submitted_text = self.text_var.get()
        print(f"Submitted Text: {submitted_text}")

    def vanish_text(self):
        self.text_var.set("")
        self.root.after(3000, self.vanish_text)  # Restart the timer

if __name__ == "__main__":
    root = tk.Tk()
    app = DisappearingTextApp(root)
    root.mainloop()
