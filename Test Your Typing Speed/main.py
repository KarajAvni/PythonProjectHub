import tkinter as tk
import random
import time

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.sentences = [
            "Programming is fun and rewarding.",
            "Hello, World! This is a typing speed test.",
            "Practice makes perfect.",
            "Python is a powerful programming language.",
        ]

        self.current_sentence = ""
        self.start_time = 0

        self.label_sentence = tk.Label(root, text="")
        self.label_sentence.pack(pady=10)

        self.entry_input = tk.Entry(root)
        self.entry_input.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Typing Test", command=self.start_typing_test)
        self.start_button.pack(pady=10)

    def start_typing_test(self):
        self.current_sentence = random.choice(self.sentences)
        self.label_sentence.config(text=self.current_sentence)
        self.start_time = time.time()
        self.start_button.config(state=tk.DISABLED)
        self.entry_input.delete(0, tk.END)
        self.entry_input.config(state=tk.NORMAL)
        self.root.bind("<Return>", self.check_typing)

    def check_typing(self, event):
        user_input = self.entry_input.get().strip()
        if user_input == self.current_sentence:
            elapsed_time = time.time() - self.start_time
            words_per_minute = int((len(self.current_sentence.split()) / elapsed_time) * 60)
            result_message = f"Typing speed: {words_per_minute} words per minute!"
            self.label_sentence.config(text=result_message)
        else:
            self.label_sentence.config(text="Incorrect! Try again.")

        self.root.unbind("<Return>")
        self.start_button.config(state=tk.NORMAL)
        self.entry_input.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()

