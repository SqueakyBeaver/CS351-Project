import customtkinter as ctk
from CTkTable import CTkTable

import tasks


class RepReportWidget(ctk.CTkFrame):
    res_widget: CTkTable | ctk.CTkLabel

    def __init__(self, ctk_app, task: tasks.RepresentativeReport):
        super().__init__(ctk_app)

        self.task = task

        self.res_widget = None

        self.grid_columnconfigure(0, weight=1)

        self.title_widget = ctk.CTkLabel(
            self, text="Generate a report on all representatives"
        )
        self.title_widget.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.btn = ctk.CTkButton(
            self, text="Show representative report", command=self.showReport
        )
        self.btn.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

    def showReport(self):
        # (RepNum, LastName, FirstName, num_customers, avg_bal)
        try:
            res: list[tuple] = self.task.runTask()

            self.res_widget = CTkTable(
                self,
                values=[
                    [
                        "Rep Number",
                        "First Name",
                        "Last Name",
                        "# of Customers",
                        "Avg. Customer Bal",
                    ]
                ]
                + res,
            )
            
            self.res_widget.grid(row=2, column=0, padx=10, pady=10)
            self.btn.configure(
                text="Hide representative report", command=self.hideReport
            )
        except Exception as e:
            self.res_widget = ctk.CTkLabel(
                self,
                text="There was an error while retrieving a report on all representatives.\n"
                "Perhaps your data is malformed??"
                f"Here's an error for debugging: {e}",
                text_color="red",
            )
            
            self.res_widget.grid(row=2, column=0, padx=10, pady=10)
            self.btn.configure(
                text="Hide representative report", command=self.hideReport
            )

    def hideReport(self):
        if self.res_widget:
            self.btn.configure(
                text="Show representative report", command=self.showReport
            )

            self.res_widget.destroy()
