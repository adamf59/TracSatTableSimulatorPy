# This file should match what is on the PYNQ Board. It is platform-independent (works in sim or real life)

# Called repetitively to do stuff:
from TableSimulatorCore import ControllerBridge


def update(controller_bridge: ControllerBridge):
    controller_bridge.set_thruster_state(1, True)
    controller_bridge.set_thruster_state(2, True)
    controller_bridge.set_thruster_state(0, True)
