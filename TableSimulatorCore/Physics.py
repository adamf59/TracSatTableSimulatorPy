import math

import TableSimulatorCore

# def get_position(initial_position: tuple = (0, 0), initial_velocity: tuple = (0, 0), time_step=0) -> ():
#     return initial_position[0] + (initial_velocity[0] * time_step), initial_position[1] + initial_velocity[1] * time_step
#
#
# def get_velocity(initial_velocity: tuple = (0, 0), acceleration: tuple = (0, 0), time_step=0) -> ():
#     return initial_velocity[0] + (acceleration[0] * time_step), initial_velocity[1] + (acceleration[1] * time_step)
#
#
# def get_velocity(initial_velocity: tuple = (0, 0), acceleration: tuple = (0, 0), displacement: tuple = (0, 0)) -> ():
#     return math.sqrt(pow(initial_velocity[0], 2) + (2 * acceleration[0] * displacement[0])), math.sqrt(pow(initial_velocity[1], 2) + (2 * acceleration[1] * displacement[1]))
#
#
# def get_position(initial_position: tuple = (0, 0), initial_velocity: tuple = (0, 0), acceleration: tuple = (0, 0), time_step=0) -> ():
#     return initial_position[0] + (initial_velocity[0] * time_step) + (0.5 * acceleration[0] * pow(time_step, 2)), initial_position[1] + (initial_velocity[1] * time_step) + (0.5 * acceleration[1] * pow(time_step, 2))
#


def thruster_state_to_acceleration_vectors(thruster_state, ) -> ():

    fx = (-thruster_state[0] * TableSimulatorCore.THRUSTER_OUTPUT_NEWTONS) + thruster_state[2] * TableSimulatorCore.THRUSTER_OUTPUT_NEWTONS
    fy = (-thruster_state[3] * TableSimulatorCore.THRUSTER_OUTPUT_NEWTONS) + thruster_state[1] * TableSimulatorCore.THRUSTER_OUTPUT_NEWTONS

    return fx / TableSimulatorCore.VEHICLE_MASS, fy / TableSimulatorCore.VEHICLE_MASS
