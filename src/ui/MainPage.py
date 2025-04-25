import customtkinter as ctk

import tasks
import ui


class MainPage(ctk.CTkFrame):
    def __init__(self, parent, db_conn, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
       
        # self.configure(require_redraw=True, fg_color="transparent")
        # Initialize a widget class. The first arg will be the parent of the widget (currently `self`)
        # The other args are up to you, but one should be the task associated with the widget
        self.customer_report_widget = ui.CustomerReportWidget(
            self, tasks.CustomerReport(db_conn)
        )
        # Place the widget on the window's "grid"
        self.customer_report_widget.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        self.example_widget = ui.ExampleWidget(self, tasks.BaseTask)
        self.example_widget.grid(row=0, column=2, padx=20, pady=20, sticky="e")

