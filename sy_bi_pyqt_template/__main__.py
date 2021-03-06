"""
For reference, see:
https://acc-py.web.cern.ch/gitlab/bisw-python/pyqt-tutorial/docs/stable/2-project-structure.html#project-name-main-py
"""

import os
import sys
import logging

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget
from accwidgets.app_frame import ApplicationFrame
from accwidgets.timing_bar._model import TimingBarModel, TimingBarDomain

# Import the View from the widgets folder
from sy_bi_pyqt_template.widgets.main_widget import MainWidget

# Import the constants
from sy_bi_pyqt_template.constants import APPLICATION_NAME, AUTHOR, EMAIL


def main():
    """
        Application's entry point.
        It creates a QApplication and an ApplicationFrame to wrap your GUI.
        Then loads your GUI into the main window and shows it, entering the event loop.
    """
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    # Instantiate the QApplication
    app = QApplication(sys.argv)

    try:
        # Instantiate the ApplicationFrame
        window = ApplicationFrame(use_timing_bar=True, use_log_console=True)

        #logger = getLogger()
        logging.info("Starting up {}...".format(APPLICATION_NAME))

        # Set the Timing Widget (the one on the top-left corner of the frame) to read data from one accelerator.
        # For the example, we set SPS
        window.timing_bar.model = TimingBarModel(domain=TimingBarDomain.SPS)

        # Make the log console start closed
        window.log_console.console.toggleExpandedMode()

        # Instantiate your GUI (here the MainWidget class)
        main_widget = MainWidget(parent=window)

        # Add the main widget to the window
        window.setCentralWidget(main_widget)

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
    
