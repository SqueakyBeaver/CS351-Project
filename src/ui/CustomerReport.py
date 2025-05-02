import customtkinter as ctk
from CTkTable import CTkTable

import tasks


class CustomerReportWidget(ctk.CTkFrame):
    res_widget: ctk.CTkFrame | ctk.CTkLabel

    def __init__(self, ctk_app, task: tasks.CustomerReport):
        super().__init__(ctk_app)

        self.task = task

        self.cust_name = ctk.StringVar()

        self.widget_label = ctk.CTkLabel(self, text="Get Customer's total quoted price")
        self.widget_label.grid(row=0, column=0, padx=10, pady=(0, 10), sticky="ew")

        self.input_frame = ctk.CTkFrame(self, border_width=0, fg_color="transparent")
        self.input_frame.grid(row=1, column=0, padx=10, pady=(0, 10))

        self.input_label = ctk.CTkLabel(self.input_frame, text="Customer name")
        self.input_label.grid(row=0, column=0, padx=(10, 5))

        self.input_field = ctk.CTkEntry(self.input_frame, textvariable=self.cust_name)
        self.input_field.grid(row=0, column=1, padx=(5, 10))
        # Call submitInput() when the enter key is pressed
        self.input_field.bind("<Key-Return>", self.submitInput)

        self.submit_btn = ctk.CTkButton(
            self, text="Generate Report", command=self.submitInput
        )
        self.submit_btn.grid(row=2, column=0, padx=10, pady=(0, 10))

        self.res_widget = None

    def submitInput(self, event=None):
        customer_info = self.task.runTask(self.cust_name.get())

        if not customer_info:
            self.res_widget = ctk.CTkLabel(
                self,
                text=f"No orders found for {self.cust_name.get() or 'customer'}",
                text_color="red",
            )
            self.res_widget.grid(row=3, column=0)
            return

        self.res_widget = ctk.CTkFrame(self)

        title = ctk.CTkLabel(self.res_widget, text=f"Report for {customer_info.name}")
        title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # | # of items ordered | Total Quoted Price | # Orders | Balance | Credit limit |
        table = CTkTable(
            self.res_widget,
            values=[
                ("# of Items ordered", "# of Orders", "Balance", "Credit Limit"),
                (
                    customer_info.total_ordered,
                    customer_info.num_orders,
                    customer_info.balance,
                    customer_info.credit_limit,
                ),
            ],
        )
        table.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        total_qp = ctk.CTkLabel(
            self.res_widget,
            text=f"The total quoted price is ${customer_info.total_quoted_price:,.2f}",
        )
        total_qp.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.res_widget.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
