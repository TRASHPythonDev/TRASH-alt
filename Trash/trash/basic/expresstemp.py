from time import sleep
from pymata4 import pymata4

def func(board):
    board.set_pin_mode_stepper(400, [22,2])
    board.set_pin_mode_stepper(400, [23,3])

board = pymata4.Pymata4(arduino_instance_id = 1)
try:
    func(board)
    board.stepper_write(100, -800)
    board.stepper_write(100, -800)
    board.shutdown()
except KeyboardInterrupt:
    board.shutdown()

