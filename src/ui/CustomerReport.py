import customtkinter as ctk
from CTkTable import CTkTable
import dataclasses
import tasks


def customerReportWidget(ctk_app: ctk.CTk, task: tasks.CustomerReport):
    def submitInput():
        items, total_price = task.runTask(cust_name.get())

        if not items or not total_price:
            err_txt = ctk.CTkLabel(
                ctk_app,
                text=f"No orders found for {cust_name.get() or 'customer'}",
                text_color="red",
            )
            err_txt.grid(row=3, column=0)
            return

        res_table = CTkTable(
            ctk_app,
            values=[
                ("Item Description", "Item Price", "Aomunt Ordered", "Quoted Price")
            ]
            + [dataclasses.astuple(i) for i in items]
        )
        res_table.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

        total_qp = ctk.CTkLabel(ctk_app, text=f"The total quoted price is ${total_price}")
        total_qp.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

    cust_name = ctk.StringVar()

    widget_label = ctk.CTkLabel(ctk_app, text="Get Customer's total quoted price")
    widget_label.grid(row=0, column=0, padx=20, pady=(0, 20), sticky="ew")

    input_frame = ctk.CTkFrame(ctk_app, border_width=0, fg_color="transparent")
    input_frame.grid(row=1, column=0, padx=20, pady=(0, 20))

    input_label = ctk.CTkLabel(input_frame, text="Customer name")
    input_label.grid(row=0, column=0, padx=(20,5))

    input_field = ctk.CTkEntry(input_frame, textvariable=cust_name)
    input_field.grid(row=0, column=1, padx=(5,20))

    submit_btn = ctk.CTkButton(ctk_app, text="Generate Report", command=submitInput)
    submit_btn.grid(row=2, column=0, padx=20, pady=(0, 20))
