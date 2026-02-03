import customtkinter as ctk

class Task123App:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title("Task123")
        self.app.geometry("600x400")

        label = ctk.CTkLabel(
            self.app,
            text="Welcome to Task123"
        )
        label.pack(pady=20)

        self.energy = ctk.CTkSlider(
            self.app,
            from_=1,
            to=10
        )
        self.energy.pack(pady=10)

        btn = ctk.CTkButton(
            self.app,
            text="What should I do?",
            command=self.suggest
        )
        btn.pack(pady=10)

    def suggest(self):
        print("Energy:", self.energy.get())

    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    Task123App().run()
