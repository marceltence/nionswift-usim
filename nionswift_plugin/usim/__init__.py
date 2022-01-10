from nion.utils import Registry
from nion.instrumentation import HardwareSource

from . import InstrumentDevice
from . import CameraDevice
from . import ScanDevice
from . import InstrumentPanel

# Marcel Tencé
# Instrument is already created by orsay-instrumentation exists
# If not create instrument here.
#

def run():
    #
    # Swift works fine with only one instrument_controller!.
    instrument = HardwareSource.HardwareSourceManager().get_instrument_by_id("usim_stem_controller")
    if instrument is None:
        instrument = InstrumentDevice.Instrument("usim_stem_controller")
        Registry.register_component(instrument, {"instrument_controller", "stem_controller"})
        CameraDevice.run(instrument)
        ScanDevice.run(instrument)
        InstrumentPanel.run(instrument)
    if instrument is not None:
        CameraDevice.run(instrument)
        ScanDevice.run(instrument)
        InstrumentPanel.run(instrument)
