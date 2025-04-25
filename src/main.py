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

# Make the pages take up the entire window
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# TODO: Make login page that bring up the main page when logged in
# Also add logout button that does the opposite
main_page = ui.MainPage(app, dbcfg.db_conn)
main_page.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")


app.mainloop()
