import customtkinter as ctk
from tasks.AddRepresentative import AddRepresentative


class AddRepresentativeWidget(ctk.CTkFrame):
    def __init__(self, ctk_app, db_conn, *args, **kwargs):
        super().__init__(ctk_app, *args, **kwargs)

        self.task = AddRepresentative(db_conn)

        form_layout = ctk.CTkFrame(self, fg_color="transparent")

        self.inputs = [
            ("RepNum", ctk.StringVar(), ctk.CTkEntry(form_layout), 0, 0),
            ("First Name", ctk.StringVar(), ctk.CTkEntry(form_layout), 1, 0),
            ("Last Name", ctk.StringVar(), ctk.CTkEntry(form_layout), 1, 1),
            ("Street", ctk.StringVar(), ctk.CTkEntry(form_layout), 2, 0),
            ("City", ctk.StringVar(), ctk.CTkEntry(form_layout), 2, 1),
            ("State", ctk.StringVar(), ctk.CTkEntry(form_layout), 3, 0),
            ("Postal Code", ctk.StringVar(), ctk.CTkEntry(form_layout), 3, 1),
            ("Commission", ctk.StringVar(), ctk.CTkEntry(form_layout), 4, 0),
            ("Rate", ctk.StringVar(), ctk.CTkEntry(form_layout), 4, 1),
        ]

        for idx, (label, input_var, entry_widget, row, column) in enumerate(
            self.inputs
        ):
            label_widget = ctk.CTkLabel(form_layout, text=label)
            entry_widget.configure(textvariable=input_var)

            if idx < len(self.inputs) - 1:
                entry_widget.bind(
                    "<Key-Return>", self.nextWidget(self.inputs[idx + 1][2])
                )
            else:
                entry_widget.bind("<Key-Return>", self.submitInput)

            label_widget.grid(row=row, column=2 * column, padx=5, pady=10, sticky="ew")
            entry_widget.grid(
                row=row, column=2 * column + 1, padx=5, pady=10, sticky="ew"
            )

        self.task_label = ctk.CTkLabel(self, text="Add a representative")
        self.task_label.grid(
            row=0, column=0, columnspan=2, padx=20, pady=20, sticky="ew"
        )

        form_layout.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

        self.submit_button = ctk.CTkButton(
            self, text="Add Representative", command=self.submitInput
        )
        self.submit_button.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

    def nextWidget(self, widget: ctk.CTkEntry):
        def command() -> None:
            widget.focus()

        return command()

    def submitInput(self):
        values = []
        for _, input, _, _, _ in self.inputs:
            values.append(input.get())

        try:
            self.task.runTask(*values)
            self.res_label = ctk.CTkLabel(self, text="Representative added!")
            self.res_label.grid(
                row=3, column=0, padx=20, pady=20, sticky="ew", rowspan=2
            )
        except Exception as e:
            self.res_label = ctk.CTkLabel(
                self,
                text=f"Failed to add representative: {str(e)}",
                text_color="red",
                wraplength=40,
            )
            self.res_label.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
