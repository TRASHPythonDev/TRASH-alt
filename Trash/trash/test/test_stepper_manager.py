# this file tests instantiation of SensorManager and all methods for this class

import pytest
import motor
from stepper_manager import StepperManager

def test_initialize_stepper_manager_add_stepper_retrieve():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22)
    new_stepper_manager.add_stepper(new_stepper)
    assert new_stepper_manager.get_if_id_in_use(new_stepper["motor id"])

def test_initialize_stepper_manager_add_stepper_remove():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22)
    new_stepper_manager.add_stepper(new_stepper)
    new_stepper_manager.remove_stepper(new_stepper["motor id"])
    assert new_stepper_manager.get_if_id_in_use(new_stepper["motor id"]) == False

def test_initialize_stepper_manager_add_stepper_remove_attempt_access_error_should_occur():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22)
    new_stepper_manager.add_stepper(new_stepper)
    new_stepper_manager.remove_stepper(new_stepper["motor id"])
    with pytest.raises(LookupError):
        new_stepper_manager.get_master_data_by_id(new_stepper["motor id"])

def test_initialize_stepper_manager_add_stepper_get_data_by_id():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22)
    new_stepper_manager.add_stepper(new_stepper)
    assert new_stepper_manager.get_master_data_by_id(new_stepper["motor id"])["pwm pin"] == new_stepper["pwm pin"]

def test_initialize_stepper_manager_add_stepper_get_data_by_name():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22, motor_name = "motor 1")
    new_stepper_manager.add_stepper(new_stepper)
    assert new_stepper_manager.get_master_data_by_name(new_stepper["motor name"])["pwm pin"] == new_stepper["pwm pin"]

def test_initialize_stepper_manager_add_stepper_get_data_by_invalid_name_should_throw_lookup_error():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22, motor_name = "motor 1")
    new_stepper_manager.add_stepper(new_stepper)
    with pytest.raises(LookupError):
        new_stepper_manager.get_master_data_by_name("motor 53")

def test_initialize_stepper_manager_add_stepper_is_ready_check():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22)
    new_stepper_manager.add_stepper(new_stepper)
    assert new_stepper_manager.get_if_id_in_ready_list(new_stepper["motor id"])

def test_initialize_stepper_manager_add_stepper_move_to_ready_invalid_id_should_throw_lookup_error():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22)
    new_stepper_manager.add_stepper(new_stepper)
    with pytest.raises(LookupError):
        new_stepper_manager.move_to_ready(new_stepper["motor id"] + 1)

def test_initialize_stepper_manager_add_stepper_move_to_ready_but_not_moving_should_throw_runtime_error():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22)
    new_stepper_manager.add_stepper(new_stepper)
    with pytest.raises(RuntimeError):
        new_stepper_manager.move_to_ready(new_stepper["motor id"])

def test_initialize_stepper_manager_add_two_steppers_is_ready_check():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22)
    new_stepper_manager.add_stepper(new_stepper)
    new_stepper2 = motor.create_motor(8, 3, 23)
    new_stepper_manager.add_stepper(new_stepper2)
    assert new_stepper_manager.get_ready_list_ids()[0] == new_stepper["motor id"]
    assert new_stepper_manager.get_ready_list_ids()[1] == new_stepper2["motor id"]

def test_initialize_stepper_manager_add_stepper_is_not_moving_check():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22)
    new_stepper_manager.add_stepper(new_stepper)
    assert new_stepper_manager.get_if_id_in_moving_list(new_stepper["motor id"]) == False

def test_initialize_stepper_manager_add_stepper_move_to_moving_check_is_not_ready():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22)
    new_stepper_manager.add_stepper(new_stepper)
    new_moving_data = motor.create_moving_data(7, 250)
    new_stepper_manager.move_to_moving(new_moving_data)
    assert new_stepper_manager.get_if_id_in_ready_list(new_stepper["motor id"]) == False

def test_initialize_stepper_manager_add_stepper_move_to_moving_check_is_moving():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22)
    new_stepper_manager.add_stepper(new_stepper)
    new_moving_data = motor.create_moving_data(7, 250)
    new_stepper_manager.move_to_moving(new_moving_data)
    assert new_stepper_manager.get_if_id_in_moving_list(new_stepper["motor id"])

def test_initialize_stepper_manager_add_stepper_move_to_moving_check_moving_data():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22)
    new_stepper_manager.add_stepper(new_stepper)
    new_moving_data = motor.create_moving_data(7, 250)
    new_stepper_manager.move_to_moving(new_moving_data)
    assert new_stepper_manager.get_moving_data_by_id(new_stepper["motor id"])["destination"] == 250

def test_initialize_stepper_manager_add_stepper_check_moving_data_should_throw_lookup_error():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22)
    new_stepper_manager.add_stepper(new_stepper)
    with pytest.raises(LookupError):
        new_stepper_manager.get_moving_data_by_id(new_stepper["motor id"])

def test_initialize_stepper_manager_add_stepper_move_to_moving_invalid_id_should_throw_lookup_error():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22)
    new_stepper_manager.add_stepper(new_stepper)
    new_moving_data = motor.create_moving_data(8, 250)
    with pytest.raises(LookupError):
        new_stepper_manager.move_to_moving(new_moving_data)

def test_initialize_stepper_manager_add_stepper_move_to_moving_attempt_again_should_throw_runtime_error():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22)
    new_stepper_manager.add_stepper(new_stepper)
    new_moving_data = motor.create_moving_data(7, 250)
    new_stepper_manager.move_to_moving(new_moving_data)
    with pytest.raises(RuntimeError):
        new_stepper_manager.move_to_moving(new_moving_data)

def test_initialize_stepper_manager_add_two_steppers_move_to_moving_check_is_moving():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22)
    new_stepper_manager.add_stepper(new_stepper)
    new_moving_data = motor.create_moving_data(7, 250)
    new_stepper_manager.move_to_moving(new_moving_data)
    new_stepper2 = motor.create_motor(8, 3, 23)
    new_stepper_manager.add_stepper(new_stepper2)
    new_moving_data2 = motor.create_moving_data(8, 300, 1)
    new_stepper_manager.move_to_moving(new_moving_data2)
    assert new_stepper_manager.get_moving_list_ids()[0] == new_stepper["motor id"]
    assert new_stepper_manager.get_moving_list_ids()[1] == new_stepper2["motor id"]

def test_initialize_stepper_manager_add_stepper_move_to_moving_and_back_to_ready_check_is_ready():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22)
    new_stepper_manager.add_stepper(new_stepper)
    new_moving_data = motor.create_moving_data(7, 250)
    new_stepper_manager.move_to_moving(new_moving_data)
    new_stepper_manager.move_to_ready(new_stepper["motor id"])
    assert new_stepper_manager.get_if_id_in_ready_list(new_stepper["motor id"])

def test_initialize_stepper_manager_add_stepper_move_to_moving_and_back_to_ready_check_is_not_moving():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22)
    new_stepper_manager.add_stepper(new_stepper)
    new_moving_data = motor.create_moving_data(7, 250)
    new_stepper_manager.move_to_moving(new_moving_data)
    new_stepper_manager.move_to_ready(new_stepper["motor id"])
    assert new_stepper_manager.get_if_id_in_moving_list(new_stepper["motor id"]) == False

def test_initialize_stepper_manager_add_two_steppers_move_to_moving_and_back_to_ready_check_is_ready():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22)
    new_stepper_manager.add_stepper(new_stepper)
    new_moving_data = motor.create_moving_data(7, 250)
    new_stepper_manager.move_to_moving(new_moving_data)
    new_stepper2 = motor.create_motor(8, 3, 23)
    new_stepper_manager.add_stepper(new_stepper2)
    new_moving_data2 = motor.create_moving_data(8, 300, 1)
    new_stepper_manager.move_to_moving(new_moving_data2)
    new_stepper_manager.move_to_ready(new_stepper["motor id"])
    new_stepper_manager.move_to_ready(new_stepper2["motor id"])
    assert new_stepper_manager.get_ready_list_ids()[0] == new_stepper["motor id"]
    assert new_stepper_manager.get_ready_list_ids()[1] == new_stepper2["motor id"]

def test_initialize_stepper_manager_add_stepper_with_custom_position_check_value_stored():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22, motor_position = 300)
    new_stepper_manager.add_stepper(new_stepper)
    assert new_stepper_manager.get_master_data_by_id(new_stepper["motor id"])["motor position"] == 300

def test_initialize_stepper_manager_add_stepper_with_custom_position_alter_and_check_value_stored():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22, motor_position = 300)
    new_stepper_manager.add_stepper(new_stepper)
    new_stepper_manager.set_motor_position_by_id(new_stepper["motor id"], 654)
    assert new_stepper_manager.get_master_data_by_id(new_stepper["motor id"])["motor position"] == 654

def test_initialize_stepper_manager_and_delete_unbound_local_error_should_occur_on_access_attempt():
    new_stepper_manager = StepperManager()
    new_stepper = motor.create_motor(7, 2, 22)
    new_stepper_manager.add_stepper(new_stepper)
    del new_stepper_manager
    with pytest.raises(UnboundLocalError):
        new_stepper_manager == None

