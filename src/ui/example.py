from PySide6 import QtCore, QtWidgets
# To run: use the command py -3 src/UI/example.py


class ExampleWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hiiiiiiiiiiii :3", "Okay, bye then ;-;"]
        self.say = ["Go away >:(", "Wait, no come back!"]

        self.button = QtWidgets.QPushButton(self.say[0])
        self.text = QtWidgets.QLabel(
            self.hello[0],
        )
        self.text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.button.clicked.connect(self.clickButton)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.button)

        self.setLayout(layout)


    @QtCore.Slot()
    def clickButton(self):
        if self.text.text() == self.hello[0]:
            self.text.setText(self.hello[1])
            self.button.setText(self.say[1])
        else:
            self.text.setText(self.hello[0])
            self.button.setText(self.say[0])


# Only run this if this is the main file being run
# i.e. using `py -3 src.UI/example.py` will execute
# the code in this if statement
if __name__ == "__main__":
    import sys
    
    # Create the main application
    # This should only be done once per application,
    # so it should be in main.py
    app = QtWidgets.QApplication(sys.argv)

    # Create a window
    window = QtWidgets.QMainWindow()

    window.setWindowTitle("Example window")

    # Add our example widget to the window
    example = ExampleWidget()

    window.setCentralWidget(example)

    # Make the window show up
    window.show()

    # run the app
    app.exec()
