from TableSimulatorCore import SimulationDriver


class ControllerBridge:

    def __init__(self, sim_driver: SimulationDriver):
        self.sim_driver = sim_driver

    def set_thruster_state(self, thruster_no, new_state: bool):
        """
        AVAILABLE EVERYWHERE
        """
        self.sim_driver.thruster_state[thruster_no] = int(new_state)

    def get_velocity(self) -> ():
        """
        AVAILABLE EVERYWHERE
        """
        return self.sim_driver.simulator_velocity_x, self.sim_driver.simulator_velocity_y

    def get_position(self) -> ():
        """
        AVAILABLE EVERYWHERE
        """
        return self.sim_driver.simulator_position_x, self.sim_driver.simulator_position_y

    def get_acceleration(self) -> ():
        """
        AVAILABLE EVERYWHERE
        """
        return self.sim_driver.simulator_acceleration_x, self.sim_driver.simulator_acceleration_y

