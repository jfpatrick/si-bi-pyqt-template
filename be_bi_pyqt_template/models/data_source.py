from datetime import datetime

from PyQt5.QtCore import QObject, pyqtSlot

import pyjapc
from accwidgets.graph import UpdateSource, PointData

#########################################################################################
# Monkey-patch PyJAPC with papc - connect to simulated devices instead of real devices
# COMMENT OUT THESE LINES TO CONNECT WITH REAL DEVICES
from be_bi_pyqt_template.models.papc_setup.papc_devices import setup_papc_devices
pyjapc.PyJapc = setup_papc_devices()
#########################################################################################


class ExampleModel(QObject):
    """
        This class acts as model for the SpinBoxes below the plots.
        It connects to JAPC and performs GET and SET operations.
        Functions decorated with the @pyqtSlot decorator can
        be connected to signals coming from the View. In general, no direct call
        from the View to the Model should ever happen.
        You can see how the signals and the slots are connected in the
        ExampleWidget class.
    """
    def __init__(self):
        super(QObject, self).__init__()
        self.japc = pyjapc.PyJapc()
        self.japc.setSelector("LHC.USER.ALL")

    def get_amplitude_sin(self):
        # Replace TEST_DEVICE/Settings#amplitude_sin with your device-property-field of interest
        return self.japc.getParam("TEST_DEVICE/Settings#amplitude_sin")

    def get_period_sin(self):
        # Replace TEST_DEVICE/Settings#period_sin with your device-property-field of interest
        return self.japc.getParam("TEST_DEVICE/Settings#period_sin")

    def get_amplitude_cos(self):
        # Replace TEST_DEVICE/Settings#amplitude_cos with your device-property-field of interest
        return self.japc.getParam("TEST_DEVICE/Settings#amplitude_cos")

    def get_period_cos(self):
        # Replace TEST_DEVICE/Settings#period_cos with your device-property-field of interest
        return self.japc.getParam("TEST_DEVICE/Settings#period_cos")

    @pyqtSlot(int)
    def set_amplitude_sin(self, value):
        # Replace TEST_DEVICE/Settings#amplitude_sin with your device-property-field of interest
        self.japc.setParam("TEST_DEVICE/Settings#amplitude_sin", value)

    @pyqtSlot(int)
    def set_period_sin(self, value):
        # Replace TEST_DEVICE/Settings#period_sin with your device-property-field of interest
        self.japc.setParam("TEST_DEVICE/Settings#period_sin", value)

    @pyqtSlot(int)
    def set_amplitude_cos(self, value):
        # Replace TEST_DEVICE/Settings#amplitude_cos with your device-property-field of interest
        self.japc.setParam("TEST_DEVICE/Settings#amplitude_cos", value)

    @pyqtSlot(int)
    def set_period_cos(self, value):
        # Replace TEST_DEVICE/Settings#period_cos with your device-property-field of interest
        self.japc.setParam("TEST_DEVICE/Settings#period_cos", value)


class DeviceTimingSource(UpdateSource):
    """
        This class acts as a Timing model for the plots.
        It subscribes to JAPC and emits a new timing value
        every time it receives new data.

        Emitted signals can be in turn picked up by the View.
        In this specific case, the 'sig_new_timestamp' signal
        can be understood by accwidgets' Plot classes.
        Always check the documentation to make sure which signal
        names are understood by the target classes.
    """
    def __init__(self, parameter_name, selector):
        super().__init__()
        self.japc = pyjapc.PyJapc()
        self.japc.setSelector(timingSelector=selector)
        self.japc.subscribeParam(parameter_name, self._new_value_received)
        self.japc.startSubscriptions()

    def _new_value_received(self, _, value) -> None:
        """ Callback for JAPC, emitting the signal 'sig_new_timestamp' """
        self.sig_new_timestamp.emit(datetime.now().timestamp())


class SinglePointSource(UpdateSource):
    """
        This class acts as a Data model for the plots.
        It subscribes to JAPC and emits a new PointData value
        every time it receives new data.

        Emitted signals can be in turn picked up by the View.
        In this specific case, the 'sig_new_data' signal
        can be understood by accwidgets' Plot classes.
        Always check the documentation to make sure which signal
        names are understood by the target classes.
    """
    def __init__(self, parameter_name, selector):
        super().__init__()
        self.parameter_name = parameter_name
        self.selector = selector
        self.japc = pyjapc.PyJapc()
        self.japc.setSelector(timingSelector=selector)
        self.japc.subscribeParam(parameter_name, self._create_new_value)
        self.japc.startSubscriptions()

    def _create_new_value(self, _, value) -> None:
        """ Callback for JAPC, emitting the signal 'sig_new_data' """
        new_data = PointData(
            x=datetime.now().timestamp(),
            y=float(value)
        )
        self.sig_new_data[PointData].emit(new_data)
