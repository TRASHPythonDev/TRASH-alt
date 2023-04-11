import pytest
import movement_arduino
from pymata4 import pymata4
from time import perf_counter


# the first three tests are sanity checks
# this test requires an arduino connected
@pytest.mark.arduino
@pytest.mark.sanity
@pytest.mark.slow
def test_board_instantiation_no_arguments_and_delete_base_library_function_sanity_check():
    testBoard = pymata4.Pymata4()
    testBoard.shutdown() 

# this test requires an arduino connected with FirmataExpress loaded and arduino_instance_id = 1
@pytest.mark.arduino
@pytest.mark.sanity
@pytest.mark.slow
def test_board_instantiation_with_arguments_and_delete_base_library_function_sanity_check():
    testBoard = pymata4.Pymata4(arduino_instance_id=1)
    testBoard.shutdown() 

# this test requires an arduino connected with FirmataExpress loaded and arduino_instance_id = 1
@pytest.mark.arduino
@pytest.mark.sanity
@pytest.mark.slow
def test_board_set_miltiple_pins_for_output_base_library_function_sanity_check():
    testBoard = pymata4.Pymata4(arduino_instance_id=1)
    try:
        pins = [3,4,5] # I expect that this test will work regardless of arduino board type
        for pin in pins:
            testBoard.set_pin_mode_digital_output(pin)
            pass
        pass
    except:
        pass
    testBoard.shutdown() 

# this test requires an arduino connected
@pytest.mark.arduino
@pytest.mark.slow
def test_board_instantiation_no_arguments_and_delete():
    testBoard2 = movement_arduino.BoardManager()
    testBoard2.release_board()

# this test requires an arduino connected with FirmataExpress loaded and arduino_instance_id = 1
@pytest.mark.arduino
@pytest.mark.slow
def test_board_instantiation_with_arguments_and_delete():
    testBoard2 = movement_arduino.BoardManager(1)
    testBoard2.release_board()

# this test requires an arduino connected with FirmataExpress loaded and arduino_instance_id = 1
@pytest.mark.arduino
@pytest.mark.slow
def test_board_set_multiple_pins_for_output():
    testBoard2 = movement_arduino.BoardManager(1)
    try:
        testBoard2.activate_pins_for_output([3,4,5]) # should work on most arduino boards
    except:
        pass
    testBoard2.release_board()

# this test requires an arduino connected with FirmataExpress loaded and arduino_instance_id = 1, and a nema 17 motorwith controller wired
@pytest.mark.arduino
@pytest.mark.slow
def test_board_rotate_stepper():
    testBoard2 = movement_arduino.BoardManager(1)
    try:
        testBoard2.activate_pins_for_output([22,2]) # should work on most arduino boards
        testBoard2.set_stepper_direction(22, 0)
    except:
        pass
    x = 0
    rate = 0.0001 # very fast, if it starst skipping steps your usb ports may be slow, or you're on windows
    time_of_last = perf_counter()
    while (x < 400): # one full rotation for a nema 17 motor
        if(perf_counter() - time_of_last > rate):
            time_of_last = perf_counter()
            testBoard2.step(2)
            x = x + 1     
        pass
    testBoard2.release_board()

