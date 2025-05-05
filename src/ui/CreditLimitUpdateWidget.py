import customtkinter as ctk

import tasks


class CreditLimitUpdateWidget(ctk.CTkFrame):
    res_widget: ctk.CTkLabel

    def __init__(self, ctk_app, task: tasks.CreditLimitUpdate):
        super().__init__(ctk_app)

        self.task = task
        self.res_widget: ctk.CTkLabel = None

        self.cust_name = ctk.StringVar()
        self.new_limit = ctk.StringVar()

        self.widget_label = ctk.CTkLabel(self, text="Update Customer Credit Limit")
        self.widget_label.grid(row=0, column=0, padx=10, pady=(0, 10), sticky="ew")

        self.input_frame = ctk.CTkFrame(self, border_width=0, fg_color="transparent")
        self.input_frame.grid(row=1, column=0, padx=10, pady=(0, 10))

        self.name_label = ctk.CTkLabel(self.input_frame, text="Customer Name")
        self.name_label.grid(row=0, column=0, padx=(10, 5))

        self.name_field = ctk.CTkEntry(self.input_frame, textvariable=self.cust_name)
        self.name_field.grid(row=0, column=1, padx=(5, 10), pady=10)
        self.name_field.bind("<Key-Return>", lambda _: self.new_limit_field.focus())

        self.new_limit_label = ctk.CTkLabel(self.input_frame, text="New Credit Limit")
        self.new_limit_label.grid(row=1, column=0, padx=(10, 5))

        self.new_limit_field = ctk.CTkEntry(
            self.input_frame, textvariable=self.new_limit
        )
        self.new_limit_field.grid(row=1, column=1, padx=(5, 10), pady=10)
        self.new_limit_field.bind("<Key-Return>", self.submitInput)

        self.submit_btn = ctk.CTkButton(
            self, text="Generate Report", command=self.submitInput
        )
        self.submit_btn.grid(row=2, column=0, padx=10, pady=(0, 10), columnspan=2)

    def submitInput(self, event=None):
        if not self.cust_name.get() or not self.new_limit.get():
            self.res_widget = ctk.CTkLabel(
                self,
                text="You must enter both a customer name and a new credit limit!",
                text_color="red",
            )
            self.res_widget.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

        try:
            old_limit, new_limit = self.task.runTask(
                self.cust_name.get(), float(self.new_limit.get())
            )

            if old_limit is None or new_limit is None:
                print(old_limit, new_limit)
                self.res_widget = ctk.CTkLabel(
                    self, text="Customer does not exist", text_color="red"
                )
            else:
                self.res_widget = ctk.CTkLabel(
                    self,
                    text=f"Updated {self.cust_name.get()}'s credit"
                    f"limit from {old_limit} to {new_limit}.",
                )

            self.res_widget.grid(row=3, column=0, padx=10, pady=10)
        except Exception as e:
            self.res_widget = ctk.CTkLabel(
                self,
                text="There was an error while retrieving a report on all representatives.\n"
                "Perhaps your data is malformed??"
                f"Here's an error for debugging: {e}",
                text_color="red",
            )

            self.res_widget.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
