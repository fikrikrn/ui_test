import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

appWidt, appHeight = 600, 700

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("User Form")
        self.geometry(f"{appWidt}x{appHeight}")

        # Nama
        self.nameLabel = ctk.CTkLabel(self, text="Name")
        self.nameLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.nameEntry = ctk.CTkEntry(self, placeholder_text="Enter Your Name")
        self.nameEntry.grid(row=0, column=1, padx=20, pady=20, columnspan=3, sticky="ew")

        # Umur
        self.ageLabel = ctk.CTkLabel(self, text="Age")
        self.ageLabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.ageEntry = ctk.CTkEntry(self, placeholder_text="99")
        self.ageEntry.grid(row=1, column=1, padx=20, pady=20, columnspan=3, sticky="ew")

        # Gender
        self.genderLabel = ctk.CTkLabel(self, text="Gender")
        self.genderLabel.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        # Gender RadioButton
        self.genderVar = ctk.StringVar(value="Prefer/not to say")
        self.maleRadioButton = ctk.CTkRadioButton(self, text="Male", variable=self.genderVar, value="He is")
        self.maleRadioButton.grid(row=2, column=1, padx=20, pady=20, sticky="ew")

        self.femaleRadioButton = ctk.CTkRadioButton(self, text="Female", variable=self.genderVar, value="She is")
        self.femaleRadioButton.grid(row=2, column=2, padx=20, pady=20, sticky="ew")

        self.noneRadioButton = ctk.CTkRadioButton(self, text="Prefer not to say", variable=self.genderVar, value="They are")
        self.noneRadioButton.grid(row=2, column=3, padx=20, pady=20, sticky="ew")

        # Choice Label
        self.choiceLabel = ctk.CTkLabel(self, text="Choice")
        self.choiceLabel.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

        # Choice Check Box
        self.choice1Var = ctk.BooleanVar()
        self.choice1 = ctk.CTkCheckBox(self, text="Jokowi", variable=self.choice1Var, onvalue=True, offvalue=False)
        self.choice1.grid(row=3, column=1, padx=20, pady=20, sticky="ew")

        self.choice2Var = ctk.BooleanVar()
        self.choice2 = ctk.CTkCheckBox(self, text="Prabowo", variable=self.choice2Var, onvalue=True, offvalue=False)
        self.choice2.grid(row=3, column=2, padx=20, pady=20, sticky="ew")

        # Occupation Label
        self.occupationLabel = ctk.CTkLabel(self, text="Occupation")
        self.occupationLabel.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

        # Occupation Combo box
        self.occupationOptionMenu = ctk.CTkOptionMenu(self, values=["Student", "Professional"])
        self.occupationOptionMenu.grid(row=4, column=1, padx=20, pady=20, columnspan=2, sticky="ew")

        # Generate Button
        self.generateButton = ctk.CTkButton(self, text="Generate Result", command=self.generate_result)
        self.generateButton.grid(row=5, column=1, columnspan=2, padx=20, pady=20, sticky="ew")

        # Output Textbox 
        self.outputText = ctk.CTkTextbox(self, width=200, height=100)
        self.outputText.grid(row=6, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")

    def generate_result(self):
        # Mengambil nilai dari form
        name = self.nameEntry.get()
        age = self.ageEntry.get()
        gender = self.genderVar.get()
        occupation = self.occupationOptionMenu.get()

        # Mendapatkan pilihan checkbox
        choices = []
        if self.choice1Var.get():
            choices.append("Jokowa")
        if self.choice2Var.get():
            choices.append("Awikwok")

        # Menampilkan hasil di Textbox
        result = f"Name: {name}\nAge: {age}\nGender: {gender}\nOccupation: {occupation}\nChoices: {', '.join(choices)}"
        self.outputText.delete("1.0", "end") 
        self.outputText.insert("1.0", result)  

if __name__ == "__main__":
    app = App()
    app.mainloop()
