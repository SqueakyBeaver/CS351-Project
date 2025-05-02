import customtkinter as ctk


# See: https://customtkinter.tomschimansky.com/

class ExampleWidget(ctk.CTkFrame):
    def __init__(self, ctk_app, task):
        super().__init__(ctk_app)

        self.grid_columnconfigure(0, weight=1)

        self.label_txt = ["Hiiiiiiiii", "Okay I see how it is >:("]
        self.btn_txt = ["Go away", "Wait, no, come back!"]

        self.text = ctk.CTkLabel(self, text=self.label_txt[0])
        # For the `sticky` parameter: Tells which sides the widget will "cling" to
        # Possible values are any combination of n, e, s, w (north, east, south, west)
        self.text.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.btn = ctk.CTkButton(self, text=self.btn_txt[0], command=self.on_click)
        self.btn.grid(row=1, column=0, padx=20, pady=20)

    def on_click(self):
        # Use `cget()` to get the current value of a widget's attribute
        idx = int(self.text.cget("text") == self.label_txt[0])

        self.text.configure(text=self.label_txt[idx])
        self.btn.configure(text=self.btn_txt[idx])


if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Example Window")
    app.geometry("400x240")

    e = ExampleWidget(app, None)
    e.grid(row=0, column=0)

    app.mainloop()
