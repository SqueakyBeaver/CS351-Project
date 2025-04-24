import sys

import customtkinter as ctk

import dbcfg
import tasks
import ui

if not dbcfg.db_conn.is_connected():
    print("ERROR: Database not connected/configured properly")
    exit(-1)

# Dark mode is not detected on linux ;-;
if sys.platform.startswith("linux"):
    ctk.set_appearance_mode("dark")


# Create the main application
# This should only be done once per application,
# so it should be in main.py
app = ctk.CTk()
app.title("Example Window")
app.geometry("1280x720")

# TODO: Make separate login page that opens first,
# then "main" page that holds all the other tasks

# Initialize a widget class. The first arg will be the parent of the widget (currently `app`)
# The other args are up to you, but one should be the task associated with the widget
customer_report_widget = ui.CustomerReportWidget(
    app, tasks.CustomerReport(dbcfg.db_conn)
)
# Place the widget on the window's "grid"
customer_report_widget.grid(row=0, column=0, padx=20, pady=20, sticky="w")

example_widget = ui.ExampleWidget(app, tasks.BaseTask)
example_widget.grid(row=0, column=2, padx=20, pady=20, sticky="e")

app.mainloop()
