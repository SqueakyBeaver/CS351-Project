import sys
import ui
import dbcfg

from PySide6 import QtWidgets

if not dbcfg.db_conn.is_connected():
    print("ERROR: Database not connected/configured properly")
    exit(-1)

# Create the main application
# This should only be done once per application,
# so it should be in main.py
app = QtWidgets.QApplication(sys.argv)

# Create a window
window = QtWidgets.QMainWindow()

window.setWindowTitle("CS 351 Group 9")

# Add our example widget to the window
cust_report = ui.CustomerReportWidget(dbcfg.db_conn)

window.setCentralWidget(cust_report)

# Make the window show up
window.show()

# run the app
app.exec()
