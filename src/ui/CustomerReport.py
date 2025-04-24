import dataclasses

import customtkinter as ctk
from CTkTable import CTkTable

import tasks


class CustomerReportWidget(ctk.CTkFrame):
    def __init__(self, ctk_app, task: tasks.CustomerReport):
        super().__init__(ctk_app)

        self.task = task

        self.cust_name = ctk.StringVar()

        self.widget_label = ctk.CTkLabel(self, text="Get Customer's total quoted price")
        self.widget_label.grid(row=0, column=0, padx=20, pady=(0, 20), sticky="ew")

        self.input_frame = ctk.CTkFrame(self, border_width=0, fg_color="transparent")
        self.input_frame.grid(row=1, column=0, padx=20, pady=(0, 20))

        self.input_label = ctk.CTkLabel(self.input_frame, text="Customer name")
        self.input_label.grid(row=0, column=0, padx=(20, 5))

        self.input_field = ctk.CTkEntry(self.input_frame, textvariable=self.cust_name)
        self.input_field.grid(row=0, column=1, padx=(5, 20))
        # Call submitInput() when the enter key is pressed
        self.input_field.bind("<Key-Return>", self.submitInput)

        self.submit_btn = ctk.CTkButton(
            self, text="Generate Report", command=self.submitInput
        )
        self.submit_btn.grid(row=2, column=0, padx=20, pady=(0, 20))

        self.err_txt: ctk.CTkLabel = None
        self.res_table: CTkTable = None
        self.total_qp: ctk.CTkLabel = None

    def submitInput(self, event=None):
        items, total_price = self.task.runTask(self.cust_name.get())
        # Not necessary to do it here,
        # but I prefer to do any data operations before any ui operations
        items = [dataclasses.astuple(i) for i in items] or None

        # Cleanup widgets that will change
        # We have to check to make sure they exist
        # since we originally set them to None
        if self.res_table:
            self.res_table.destroy()

        if self.total_qp:
            self.total_qp.destroy()

        if self.err_txt:
            self.err_txt.destroy()

        if not items or not total_price:
            self.err_txt = ctk.CTkLabel(
                self,
                text=f"No orders found for {self.cust_name.get() or 'customer'}",
                text_color="red",
            )
            self.err_txt.grid(row=3, column=0)
            return

        self.res_table = CTkTable(
            self,
            values=[
                ("Item Description", "Item Price", "Aomunt Ordered", "Quoted Price")
            ]
            + items,
        )
        self.res_table.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

        self.total_qp = ctk.CTkLabel(
            self, text=f"The total quoted price is ${total_price}"
        )
        self.total_qp.grid(row=4, column=0, padx=20, pady=20, sticky="ew")
