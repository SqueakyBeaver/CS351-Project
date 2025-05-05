import customtkinter as ctk

import tasks
import ui

class LoginPage(ctk.CTkFrame):
    def __init__(self, parent, db_conn, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.db_conn = db_conn
        self.login_task = tasks.Login(db_conn)

        self.username = ctk.StringVar()
        self.password = ctk.StringVar()

        self.grid_columnconfigure(0, weight=1)

        self.frame_label = ctk.CTkLabel(self, text="Login")
        self.frame_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.input_frame = ctk.CTkFrame(self, border_width=0, fg_color="transparent")
        self.input_frame.grid(row=1, column=0, padx=20, pady=(0, 20))

        self.username_label = ctk.CTkLabel(self.input_frame, text="Username")
        self.username_label.grid(row=0, column=0, padx=(20, 5))

        self.password_label = ctk.CTkLabel(self.input_frame, text="Password")
        self.password_label.grid(row=1, column=0, padx=(20, 5))

        self.username_field = ctk.CTkEntry(self.input_frame, textvariable=self.username)
        self.username_field.grid(row=0, column=1, padx=(5, 20))
        # Call submitInput() when the enter key is pressed
        self.username_field.bind("<Key-Return>", self.enterUsername)

        self.password_field = ctk.CTkEntry(
            self.input_frame, textvariable=self.password, show="*"
        )
        self.password_field.grid(row=1, column=1, padx=(5, 20))
        # Call submitInput() when the enter key is pressed
        self.password_field.bind("<Key-Return>", self.submitInput)

        self.submit_btn = ctk.CTkButton(self, text="Login", command=self.submitInput)
        self.submit_btn.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="ew")

        self.loginError = ctk.CTkLabel(self, text="")
        self.loginError.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

    def enterUsername(self, event=None):
        self.username_field.focus()

    def submitInput(self, event=None):
        login_good, username = self.login_task.runTask(
            self.username.get(),
            self.password.get(),
        )

        self.loginError.destroy()

        if not login_good:
            self.loginError = ctk.CTkLabel(
                self,
                text="Username or Password is incorrect",
                text_color="red",
            )
            self.loginError.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
            return

        main_page = ui.MainPage(self.master, self.db_conn, username)
        self.destroy()
        main_page.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")

