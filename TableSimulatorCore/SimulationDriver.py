from threading import Thread

import TableSimulatorCore.ControllerBridge
import TableSimulatorCore
import Controller as ct
import Physics
import time
import matplotlib.pyplot as plt

class SimulationDriver:

    # Simulator State and Memory
    _simulator_position_hist_x = _simulator_position_hist_y = []
    simulator_position_x = simulator_position_y = 0

    _simulator_velocity_hist_x = _simulator_velocity_hist_y = []
    simulator_velocity_x = simulator_velocity_y = 0

    _simulator_acceleration_hist_x = _simulator_acceleration_hist_y = []
    simulator_acceleration_x = simulator_acceleration_y = 0

    thruster_state = [0, 0, 0, 0]

    def __init__(self, samples, interval):
        self.sim_thread = Thread(target=self.sim_thread_worker)
        self.controller_bridge = TableSimulatorCore.ControllerBridge(self)
        self.total_samples = samples
        self.sim_interval = interval

    def start(self):
        self.sim_thread.start()

    def sim_thread_worker(self):
        print("-> Simulation Starting!")
        sim_start_time = time.time()

        for i in range(self.total_samples):
            ct.update(self.controller_bridge)
            self.reevaluate_world()

        print("-> Simulation Finished in " + str(round(time.time() - sim_start_time, 5)) + " sec")
        print("- Final Position: sx= " + str(round(self.simulator_position_x, 5)) + " sy= " + str(round(self.simulator_position_y, 5)))
        print("- Final Velocity: vx= " + str(round(self.simulator_velocity_x, 5)) + " vy= " + str(round(self.simulator_velocity_y, 5)))

        fig = plt.figure()
        fig.suptitle('Table Simulation', fontsize=16)
        plt.xlabel('x position', fontsize=18)
        plt.ylabel('y position', fontsize=16)
        plt.plot(self._simulator_position_hist_x, self._simulator_position_hist_y, 'ro')

        # plt.axis([0, 6, 0, 20])
        plt.show()

    def acquire_thread_lock(self):
        self.sim_thread.join()

    def reevaluate_world(self):
        # Calculate world accelerations:
        new_world_ax, new_world_ay = Physics.thruster_state_to_acceleration_vectors(self.thruster_state)
        self.simulator_acceleration_x = new_world_ax
        self.simulator_acceleration_y = new_world_ay

        # Calculate world positions
        self.simulator_position_x = round(self.simulator_position_x + (self.simulator_velocity_x * self.sim_interval) + (0.5*new_world_ax*pow(self.sim_interval, 2)), 5)
        self.simulator_position_y = round(self.simulator_position_y + (self.simulator_velocity_y * self.sim_interval) + (0.5*new_world_ay*pow(self.sim_interval, 2)), 5)

        # Calculate world velocities
        self.simulator_velocity_x = round(self.simulator_velocity_x + (new_world_ax * self.sim_interval), 5)
        self.simulator_velocity_y = round(self.simulator_velocity_y + (new_world_ay * self.sim_interval), 5)


        # Save the state to memory
        print("value:")
        print(self.simulator_position_x)
        print("before:")
        print(self._simulator_position_hist_x)
        self._simulator_position_hist_x.append(self.simulator_position_x)
        print("after")
        print(self._simulator_position_hist_x)

        self._simulator_position_hist_y.append(self.simulator_position_y)
        self._simulator_velocity_hist_x.append(self.simulator_velocity_x)
        self._simulator_velocity_hist_y.append(self.simulator_velocity_y)
        self._simulator_acceleration_hist_x.append(self.simulator_acceleration_x)
        self._simulator_acceleration_hist_y.append(self.simulator_acceleration_y)

        print(self.simulator_position_x)
        # print(self._simulator_position_hist_x)