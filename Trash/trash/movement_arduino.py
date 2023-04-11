# This file contains functions to handle low level movement commands to the arduino
# Thanks to Elliott for getting the initial version of this working

import sys
import time
from pymata4 import pymata4


class BoardManager():

    def __init__(self, board_id = 1):
        self.__board = pymata4.Pymata4(arduino_instance_id = board_id)
        pass

    # takses list of pin numbers and sets them to digital output mode
    # pins: list        - list of valid arduino digital pin numbers (integers) for a given board
    def activate_pins_for_output(self, pins: list) -> None:
        for pin in pins:
            self.__board.set_pin_mode_digital_output(pin)
        pass
    # takes list of pin numbers and sets them to pulse-width modulation (pwm) output mode
    # pins: list        - list of valid arduino digital pin numbers (integers) for a given board
    def activate_pins_for_pwm(self, pins: list) -> None:
        for pin in pins:
            self.__board.set_pin_mode_pwm_output(pin)
        pass

    # takes a list of analog pins and sets them to analog input mode 
    # pins: list        - list of valid arduino analog pin numbers (integers) for a given board
    def activate_pins_for_analog_input(self, pins: list) -> None:
        for pin in pins:
            self.__board.set_pin_mode_analog_input(pin, callback = None, differential = 1)
        pass

    def set_stepper_direction(self, direction_pin: int, direction: int):
        self.__board.digital_write(direction_pin, direction)
        pass

    # custom pwm method for rotating stepper, executes one step for the given pin
    # pin: int        - valid arduino digital pin number which has been set to digital output mode
    def step(self, pwm_pin: int):
        self.__board.digital_write(pwm_pin, 1)
        self.__board.digital_write(pwm_pin, 0)
        pass

    # pass off method for rotating stepper (not implemented)
    # pin: int        - valid arduino digital pin number which has been set to pwm output mode
    # direction: int        - valid arduino digital pin number which has been set to digital output
    def rotate_stepper_express(self, pin: int, direction: int):
        # not implemented
        pass
    
    # read analog and return value
    # pin: int        - valid arduino digital pin number which has been set to analog input mode
    def read_analog_pin(self, pin :int) -> int:
        analog_list = self.__board.analog_read(pin)
        return analog_list[0]
    
    # call before calling del in this object
    def release_board(self):
        self.__board.shutdown()