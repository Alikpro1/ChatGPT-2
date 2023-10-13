import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ChatGPT-2")
        self.minsize(800, 600)
        self.resizable(False, False)

        self.widgets = Widgets(self)


class Widgets:
    def __init__(self, root):
        super().__init__()
        self.root = root

        self.output_text = ctk.CTkTextbox(master=root,
                                          state='disabled', activate_scrollbars=False,
                                          width=500, height=250)
        self.output_text.place(relx=0.1, rely=0.1, anchor="center")

        self.button = ctk.CTkButton(master=root)
        self.button.pack(padx=20, pady=20)



if __name__ == "__main__":
    app = App()
    app.mainloop()