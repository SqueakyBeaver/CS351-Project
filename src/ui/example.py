import customtkinter as ctk

# See: https://customtkinter.tomschimansky.com/

def exampleWidget(ctk_app: ctk.CTk):
    # Python allows for nested functions :)
    # Unfortunately, the functions need to be declared/defined before they're used
    # The same cannot be said for variables, apparently
    def on_click():
        idx = int(text.cget("text") == label_txt[0])

        text.configure(text=label_txt[idx])
        btn.configure(text=btn_txt[idx])

    label_txt = ["Hiiiiiiiii", "Okay I see how it is >:("]
    btn_txt = ["Go away", "Wait, no, come back!"]

    text = ctk.CTkLabel(ctk_app, text=label_txt[0])
    text.pack()

    btn = ctk.CTkButton(ctk_app, text=btn_txt[0], command=on_click)
    btn.pack(padx=20, pady=20)

if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Example Window")
    app.geometry("400x240")

    exampleWidget(app)

    app.mainloop()
