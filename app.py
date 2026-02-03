import customtkinter as ctk
from datetime import datetime, timedelta

from backend.models import Task
from backend.ai_engine import suggest_next_task

class Task123App:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title("Task123")
        self.app.geometry("700x500")

        # ----- SAMPLE TASKS (later from DB) -----
        self.tasks = [
            Task("Reply to client email", urgency=8, energy_required=3,
                 deadline=datetime.now() + timedelta(hours=3)),

            Task("Prepare presentation", urgency=7, energy_required=8,
                 deadline=datetime.now() + timedelta(days=1)),

            Task("Organize files", urgency=4, energy_required=2),
        ]

        # ===== UI =====

        title = ctk.CTkLabel(self.app, text="Task123 – What Should I Do?",
                             font=("Arial", 20))
        title.pack(pady=20)

        # Energy slider
        self.energy_label = ctk.CTkLabel(self.app, text="Your Energy: 5")
        self.energy_label.pack()

        self.energy = ctk.CTkSlider(self.app, from_=1, to=10,
                                    command=self.update_energy_label)
        self.energy.set(5)
        self.energy.pack(pady=10)

        # Suggest button
        btn = ctk.CTkButton(self.app, text="Tell Me What To Do",
                            command=self.show_suggestion)
        btn.pack(pady=10)

        # Result
        self.result = ctk.CTkLabel(self.app, text="", wraplength=500,
                                   font=("Arial", 16))
        self.result.pack(pady=20)

        # --- Add Task Section ---
        ctk.CTkLabel(self.app, text="Add Quick Task").pack(pady=5)

        self.new_title = ctk.CTkEntry(self.app, width=300,
                                      placeholder_text="Task title")
        self.new_title.pack(pady=5)

        self.new_urgency = ctk.CTkSlider(self.app, from_=1, to=10)
        self.new_urgency.set(5)
        self.new_urgency.pack()

        add_btn = ctk.CTkButton(self.app, text="Add Task",
                                command=self.add_task)
        add_btn.pack(pady=5)

    # ----------------------------

    def update_energy_label(self, value):
        self.energy_label.configure(
            text=f"Your Energy: {int(float(value))}"
        )

    def show_suggestion(self):
        user_energy = int(self.energy.get())

        task = suggest_next_task(self.tasks, user_energy)

        if task:
            text = f"👉 Next Best Task:\n\n{task.title}\n\n" \
                   f"Urgency: {task.urgency}/10\n" \
                   f"Energy needed: {task.energy_required}/10"

            if task.deadline:
                text += f"\nDeadline: {task.deadline.strftime('%Y-%m-%d %H:%M')}"

            self.result.configure(text=text)
        else:
            self.result.configure(text="No tasks available!")

    def add_task(self):
        title = self.new_title.get()
        if not title:
            return

        urgency = int(self.new_urgency.get())

        new_task = Task(
            title=title,
            urgency=urgency,
            energy_required=5
        )

        self.tasks.append(new_task)

        self.new_title.delete(0, "end")
        self.result.configure(text="Task added! Click suggest again.")

    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    Task123App().run()



if __name__ == "__main__":
    Task123App().run()
