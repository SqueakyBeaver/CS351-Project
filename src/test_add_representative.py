import sys
from PySide6 import QtWidgets
import dbcfg

from ui.AddRepresentativeWidget import AddRepresentativeWidget

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = AddRepresentativeWidget(dbcfg.db_conn)
    window.show()

    sys.exit(app.exec())
