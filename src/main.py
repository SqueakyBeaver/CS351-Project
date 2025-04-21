import ui
import dbcfg
import customtkinter as ctk
import tasks
import sys

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

# TODO: When login UI is implemented, we should start there
ui.customerReportWidget(app, tasks.CustomerReport(dbcfg.db_conn))

app.mainloop()

