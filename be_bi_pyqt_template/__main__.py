"""
For reference, see:
https://acc-py.web.cern.ch/gitlab/bisw-python/pyqt-tutorial/docs/stable/2-project-structure.html#project-name-main-py
"""

import os
import sys
import logging

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget
from be_bi_application_frame import ApplicationFrame

# Import the View from the widgets folder
from be_bi_pyqt_template.widgets.main_widget import MainWidget

# Import the constants
from be_bi_pyqt_template.constants import APPLICATION_NAME, AUTHOR, EMAIL


def main():
    """
        Application's entry point.
        It creates a QApplication and an ApplicationFrame to wrap your GUI.
        Then loads your GUI into the main window and shows it, entering the event loop.
    """
    logging.info("Starting up {}...".format(APPLICATION_NAME))

    # Instantiate the QApplication
    app = QApplication(sys.argv)

    try:
        # Instantiate the ApplicationFrame
        window = ApplicationFrame()

        # Set the Timing Widget (the one on the top-left corner of the frame) to read data from one accelerator.
        # For the example, we set SPS
        window.timing_widget.accelerator = "SPS"

        # Instantiate your GUI (here the MainWidget class)
        main_widget = MainWidget(parent=window)

        # Add the main widget to the window
        window.setMainWidget(main_widget)

        # Apply small customizations to the application (window title, window icon...)
        icon_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'widgets/resources/images/CERN_logo.png')
        window.setWindowIcon(QIcon(icon_path))

        # Set the initial size of the window
        window.resize(800, 600)

        # Set the window title
        window.setWindowTitle(APPLICATION_NAME)

    except Exception as e:
        # First of all, log
        logging.exception(e)

        # If something goes wrong, shows a small QDialog with an error message and quits
        window = QWidget()
        dialog = QMessageBox(parent=window)
        dialog.critical(window,
                        "Error",
                        "An Exception occurred at startup:\n\n{}\n\n".format(e) +
                        "See the logs for more information, " +
                        "and please report this issue to {} ({})".format(AUTHOR, EMAIL))
        window.deleteLater()
        return

    # Enter the event loop by showing the window
    window.show()

    # Once left the event loop, terminates the application
    sys.exit(app.exec_())
    

# Compatibility with acc-py app    
if __name__ == "__main__":
    main()
    