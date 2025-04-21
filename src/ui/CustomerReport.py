import dataclasses as dc

from PySide6 import QtCore, QtWidgets

from tasks import CustomerReport

# To run: use the command py -3 src/UI/example.py


class CustomerReportWidget(QtWidgets.QWidget):
    def __init__(self, db_conn, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.task = CustomerReport(db_conn)

        self._text = QtWidgets.QLabel("Generate customer report")
        self._text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self._input = QtWidgets.QLineEdit(parent=self)
        self._input.returnPressed.connect(self.submitInput)

        self._button = QtWidgets.QPushButton("Get report")
        self._button.clicked.connect(self.submitInput)

        self._input_layout = QtWidgets.QFormLayout()
        self._input_layout.addRow("Customer Name: ", self._input)
        self._input_layout.addWidget(self._button)

        self._res_table_label = QtWidgets.QLabel("Items Ordered By Customer")
        self._res_table_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self._res_table = QtWidgets.QTableView()
        self._res_table.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents
        )

        self._res_total_price = QtWidgets.QLabel(
            "Total Quoted Price for all items Customer ordered: $xxx.xx"
        )
        self._res_total_price.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self._res_layout = QtWidgets.QVBoxLayout()
        self._res_layout.addWidget(self._res_table_label)
        self._res_layout.addWidget(self._res_table)
        self._res_layout.addSpacerItem(QtWidgets.QSpacerItem(10, 20))
        self._res_layout.addWidget(self._res_total_price)

        self._layout = QtWidgets.QVBoxLayout()
        self._layout.addWidget(self._text)
        self._layout.addLayout(self._input_layout)
        self._layout.addSpacerItem(QtWidgets.QSpacerItem(10, 20))

        self.setLayout(self._layout)

    @QtCore.Slot()
    def submitInput(self):
        items, total_price = self.task.runTask(self._input.text())

        if not items or not total_price:
            self._layout.removeItem(self._res_layout)
            return

        model = self.TableModel(items)

        self._res_table.setModel(model)
        self._res_table.show()
        self._res_table.adjustSize()
        self._layout.addLayout(self._res_layout)

        self.adjustSize()
        self.window().adjustSize()

    class TableModel(QtCore.QAbstractTableModel):
        def __init__(self, data, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self._data = data

        def data(self, index, role):
            if role == QtCore.Qt.ItemDataRole.DisplayRole:
                return dc.astuple(self._data[index.row()])[index.column()]

        def headerData(self, section, orientation, role):
            labels = [
                "Item Description",
                "Individual Price",
                "Number Ordered",
                "Quoted Price",
            ]
            if (
                orientation == QtCore.Qt.Orientation.Horizontal
                and role == QtCore.Qt.ItemDataRole.DisplayRole
            ):
                return labels[section]

            return super().headerData(section, orientation, role)

        def rowCount(self, index):
            return len(self._data)

        def columnCount(self, index):
            return len(dc.astuple(self._data[0]))
