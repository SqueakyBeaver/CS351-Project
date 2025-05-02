import customtkinter as ctk

import tasks
import ui


class MainPage(ctk.CTkFrame):
    def __init__(self, parent, db_conn, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.db_conn = db_conn

        # self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)

        self.grid_rowconfigure(1, weight=1)

        left_side = ctk.CTkFrame(self)
        right_side = ctk.CTkFrame(self)

        self.add_rep_widget = ui.AddRepresentativeWidget(left_side, self.db_conn)
        self.add_rep_widget.grid(
            row=0, column=0, padx=10, pady=10, sticky="ns", rowspan=2
        )

        self.update_cred_widget = ui.CreditLimitUpdateWidget(
            left_side, tasks.CreditLimitUpdate(self.db_conn)
        )
        self.update_cred_widget.grid(row=3, column=0, padx=10, pady=10)

        self.customer_report_widget = ui.CustomerReportWidget(
            right_side, tasks.CustomerReport(self.db_conn)
        )
        self.customer_report_widget.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="ewns",
            columnspan=2,
            rowspan=1,
        )

        self.rep_report_widget = ui.RepReportWidget(
            right_side, tasks.RepresentativeReport(self.db_conn)
        )
        self.rep_report_widget.grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
            sticky="ewns",
            columnspan=2,
            rowspan=2,
        )

        left_side.grid(row=1, column=0, sticky="nw")
        right_side.grid(row=1, column=1, sticky="nw", columnspan=2)

        self.logout_button = ctk.CTkButton(
            self, text="logout", command=self.logoutClicked
        )
        self.logout_button.grid(row=0, column=2, padx=10, pady=10, sticky="e")

    def logoutClicked(self, event=None):
        # TODO: run logout task
        login_page = ui.LoginPage(self.master, self.db_conn)
        self.destroy()
        login_page.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")
