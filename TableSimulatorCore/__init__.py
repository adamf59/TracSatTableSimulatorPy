"""
Thruster Map
                1 (+)
                ^
            |-------|
            |       |
         0<-|       |->2 (+)
            |-------|
                V
                3

"""
from TableSimulatorCore.ControllerBridge import ControllerBridge
from TableSimulatorCore.SimulationDriver import SimulationDriver

SIMULATION_TIME_INTERVAL_DEFAULT = 0.1
"""
Controls how "granular" the simulation is, a lower number means more data-points in a given time window.
This is how much time will pass during one sample.
"""

SIMULATION_SAMPLES_DEFAULT = 10
"""

"""

THRUSTER_OUTPUT_NEWTONS = 1
"""
Set to the expected output of the thrusters in newtons.
"""

VEHICLE_MASS = 1
"""
Mass of the CubeSat in question
"""

if __name__ == '__main__':

    print("=== Table Simulator ===")

    print("Simulation Options:")
    print(" - Total Samples: " + str(SIMULATION_SAMPLES_DEFAULT) + " samples [DEFAULT]")
    print(" - Simulation Interval: " + str(SIMULATION_TIME_INTERVAL_DEFAULT) + " sec/sample [DEFAULT]")
    print(" - Total Time Simulated: " + str(SIMULATION_SAMPLES_DEFAULT * SIMULATION_TIME_INTERVAL_DEFAULT) + " sec [DEFAULT]")

    simulation_driver = SimulationDriver(SIMULATION_SAMPLES_DEFAULT, SIMULATION_TIME_INTERVAL_DEFAULT)
    simulation_driver.start()
    simulation_driver.acquire_thread_lock()
