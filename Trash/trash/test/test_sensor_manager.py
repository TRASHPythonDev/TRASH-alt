# this file tests instantiation of SensorManager and all methods for this class

import pytest
import motor
from sensor_manager import SensorManager

def test_initialize_sensor_manager_add_sensor_retrieve():
    new_sensor_manager = SensorManager()
    new_sensor = motor.create_sensor(2, 7, 3)
    new_sensor_manager.add_sensor(new_sensor)
    assert new_sensor_manager.get_if_id_in_use(new_sensor["sensor id"])

def test_initialize_sensor_manager_add_sensor_remove():
    new_sensor_manager = SensorManager()
    new_sensor = motor.create_sensor(2, 7, 3)
    new_sensor_manager.add_sensor(new_sensor)
    new_sensor_manager.remove_sensor(new_sensor["sensor id"])
    assert new_sensor_manager.get_if_id_in_use(new_sensor["sensor id"]) == False

def test_initialize_sensor_manager_add_sensor_remove_attempt_access_error_should_occur():
    new_sensor_manager = SensorManager()
    new_sensor = motor.create_sensor(2, 7, 3)
    new_sensor_manager.add_sensor(new_sensor)
    new_sensor_manager.remove_sensor(new_sensor["sensor id"])
    with pytest.raises(LookupError):
        new_sensor_manager.get_master_data_by_sensor_id(new_sensor["sensor id"])

def test_initialize_sensor_manager_add_sensor_get_data_by_sensor_id():
    new_sensor_manager = SensorManager()
    new_sensor = motor.create_sensor(2, 7, 3)
    new_sensor_manager.add_sensor(new_sensor)
    sensor_data = new_sensor_manager.get_master_data_by_sensor_id(new_sensor["sensor id"])
    assert sensor_data["sensor pin"] == 3

def test_initialize_sensor_manager_add_sensor_get_data_by_motor_id():
    new_sensor_manager = SensorManager()
    new_sensor = motor.create_sensor(2, 7, 3)
    new_sensor_manager.add_sensor(new_sensor)
    sensor_data = new_sensor_manager.get_all_master_data_for_motor_id(new_sensor["motor id"])
    assert sensor_data[0]["sensor pin"] == 3

def test_initialize_sensor_manager_add_multiple_sensor_get_data_by_motor_id():
    new_sensor_manager = SensorManager()
    new_sensor = motor.create_sensor(2, 7, 3)
    new_sensor_manager.add_sensor(new_sensor)
    new_sensor2 = motor.create_sensor(2, 8, 4)
    new_sensor_manager.add_sensor(new_sensor2)
    sensor_data = []
    sensor_data = new_sensor_manager.get_all_master_data_for_motor_id(new_sensor["motor id"])
    assert sensor_data[0]["sensor pin"] == 3
    assert sensor_data[1]["sensor pin"] == 4

def test_initialize_sensor_manager_add_multiple_sensor_get_id_list():
    new_sensor_manager = SensorManager()
    new_sensor = motor.create_sensor(2, 7, 3)
    new_sensor_manager.add_sensor(new_sensor)
    new_sensor2 = motor.create_sensor(2, 8, 4)
    new_sensor_manager.add_sensor(new_sensor2)
    sensor_data = []
    sensor_data = new_sensor_manager.get_all_associated_for_motor_id(new_sensor["motor id"])
    assert sensor_data[0] == 7
    assert sensor_data[1] == 8

def test_initialize_sensor_manager_add_multiple_sensor_delete_get_id_list_should_return_empty():
    new_sensor_manager = SensorManager()
    new_sensor = motor.create_sensor(2, 7, 3)
    new_sensor_manager.add_sensor(new_sensor)
    new_sensor2 = motor.create_sensor(2, 8, 4)
    new_sensor_manager.add_sensor(new_sensor2)
    new_sensor_manager.remove_sensor(7)
    new_sensor_manager.remove_sensor(8)
    assert new_sensor_manager.get_all_associated_for_motor_id(new_sensor["motor id"]) == []

def test_initialize_sensor_manager_set_threshold_on_init():
    new_sensor_manager = SensorManager()
    new_sensor = motor.create_sensor(2, 7, 3, sensor_threshold = 70)
    new_sensor_manager.add_sensor(new_sensor)
    sensor_data = new_sensor_manager.get_master_data_by_sensor_id(new_sensor["sensor id"])
    assert sensor_data["sensor threshold"] == 70

def test_initialize_sensor_manager_set_threshold_by_setter():
    new_sensor_manager = SensorManager()
    new_sensor = motor.create_sensor(2, 7, 3)
    new_sensor_manager.add_sensor(new_sensor)
    assert new_sensor_manager.get_if_id_in_use(new_sensor["sensor id"])
    new_sensor_manager.set_sensor_threshold_by_id(new_sensor["sensor id"], 70)
    sensor_data = new_sensor_manager.get_master_data_by_sensor_id(new_sensor["sensor id"])
    assert sensor_data["sensor threshold"] == 70

def test_initialize_sensor_manager_set_threshold_without_assignment_by_setter_id_should_not_create():
    new_sensor_manager = SensorManager()
    new_sensor_manager.set_sensor_threshold_by_id(5, 70)
    assert new_sensor_manager.get_if_id_in_use(5) == False

def test_initialize_sensor_manager_and_delete_unbound_local_error_should_occur_on_access_attempt():
    new_sensor_manager = SensorManager()
    new_sensor = motor.create_sensor(2, 7, 3)
    new_sensor_manager.add_sensor(new_sensor)
    del new_sensor_manager
    with pytest.raises(UnboundLocalError):
        new_sensor_manager == None