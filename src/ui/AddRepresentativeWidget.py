from PySide6 import QtCore, QtWidgets
from tasks.AddRepresentative import AddRepresentative

class AddRepresentativeWidget(QtWidgets.QWidget):
    def __init__(self, db_conn, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.task = AddRepresentative(db_conn)

        self.inputs = {
            "RepNum": QtWidgets.QLineEdit(),
            "First Name": QtWidgets.QLineEdit(),
            "Last Name": QtWidgets.QLineEdit(),
            "Street": QtWidgets.QLineEdit(),
            "City": QtWidgets.QLineEdit(),
            "State": QtWidgets.QLineEdit(),
            "Postal Code": QtWidgets.QLineEdit(),
            "Commission": QtWidgets.QLineEdit(),
            "Rate": QtWidgets.QLineEdit(),
        }

        form_layout = QtWidgets.QFormLayout()
        for label, widget in self.inputs.items():
            form_layout.addRow(label, widget)

        self.submit_button = QtWidgets.QPushButton("Add Representative")
        self.submit_button.clicked.connect(self.submitInput)

        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    @QtCore.Slot()
    def submitInput(self):
        values = []
        for widget in self.inputs.values():
            values.append(widget.text())

        try:
            self.task.runTask(*values)
            QtWidgets.QMessageBox.information(self, "Success", "Representative added!")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"Failed to add representative: {str(e)}")
