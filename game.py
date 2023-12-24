import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz Game")
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Rome"],
                "answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                "answer": "Mars"
            },
            # Add more questions in a similar format
        ]
        self.score = 0
        self.current_question = 0

        self.label_question = tk.Label(root, text="", font=("Arial", 14))
        self.label_question.pack(pady=20)

        self.radio_var = tk.StringVar()
        self.radio_var.set("")

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", font=("Arial", 12),
                                variable=self.radio_var, value="",
                                command=self.check_answer)
            rb.pack()
            self.radio_buttons.append(rb)

        self.next_button = tk.Button(root, text="Next Question", command=self.next_question)
        self.next_button.pack(pady=20)

        self.update_question()

    def update_question(self):
        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            self.label_question.config(text=q["question"])
            for i in range(4):
                self.radio_buttons[i].config(text=q["options"][i], value=q["options"][i])
        else:
            messagebox.showinfo("Quiz Completed", f"Quiz completed!\nYour score: {self.score}/{len(self.questions)}")
            self.root.destroy()

    def check_answer(self):
        selected_answer = self.radio_var.get()
        correct_answer = self.questions[self.current_question]["answer"]
        if selected_answer == correct_answer:
            self.score += 1

    def next_question(self):
        self.current_question += 1
        self.radio_var.set("")
        self.check_answer()
        self.update_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
