import pytest
import time
import motor

# testing motor initialization with default arguments

def test_create_motor_default_args_motor_id_set():
    new_motor = motor.create_motor(0, 2, 22)
    assert new_motor["motor id"] == 0

def test_create_motor_default_args_pwm_pin_set():
    new_motor = motor.create_motor(0, 2, 22)
    assert new_motor["pwm pin"] == 2

def test_create_motor_default_args_direction_pin_set():
    new_motor = motor.create_motor(0, 2, 22)
    assert new_motor["direction pin"] == 22
    
def test_create_motor_default_args_max_rotation_set():
    new_motor = motor.create_motor(0, 2, 22)
    assert new_motor["max rotation"] == 400

def test_create_motor_default_args_min_rotation_set():
    new_motor = motor.create_motor(0, 2, 22)
    assert new_motor["min rotation"] == 0
    
def test_create_motor_default_args_motor_position_set():
    new_motor = motor.create_motor(0, 2, 22)
    assert new_motor["motor position"] == 0

def test_create_motor_default_args_motor_name_set():
    new_motor = motor.create_motor(0, 2, 22)
    assert new_motor["motor name"] == ""


#  testing motor initialization with custom arguments

def test_create_motor_custom_args_motor_id_set():
    new_motor = motor.create_motor(0, 2, 22, 800, 30, 70, "motor 1")
    assert new_motor["motor id"] == 0

def test_create_motor_custom_args_pwm_pin_set():
    new_motor = motor.create_motor(0, 2, 22, 800, 30, 70, "motor 1")
    assert new_motor["pwm pin"] == 2

def test_create_motor_custom_args_direction_pin_set():
    new_motor = motor.create_motor(0, 2, 22, 800, 30, 70, "motor 1")
    assert new_motor["direction pin"] == 22
    
def test_create_motor_custom_args_max_rotation_set():
    new_motor = motor.create_motor(0, 2, 22, 800, 30, 70, "motor 1")
    assert new_motor["max rotation"] == 800

def test_create_motor_custom_args_min_rotation_set():
    new_motor = motor.create_motor(0, 2, 22, 800, 30, 70, "motor 1")
    assert new_motor["min rotation"] == 30
    
def test_create_motor_custom_args_motor_position_set():
    new_motor = motor.create_motor(0, 2, 22, 800, 30, 70, "motor 1")
    assert new_motor["motor position"] == 70

def test_create_motor_custom_args_motor_name_set():
    new_motor = motor.create_motor(0, 2, 22, 800, 30, 70, "motor 1")
    assert new_motor["motor name"] == "motor 1"


#  testing sensor initialization with default arguments

def test_create_sensor_default_args_motor_id_set():
    new_sensor = motor.create_sensor(0, 0, 0)
    assert new_sensor["motor id"] == 0

def test_create_sensor_default_args_sensor_id_set():
    new_sensor = motor.create_sensor(0, 0, 0)
    assert new_sensor["sensor id"] == 0

def test_create_sensor_default_args_sensor_pin_set():
    new_sensor = motor.create_sensor(0, 0, 0)
    assert new_sensor["sensor pin"] == 0
    
def test_create_sensor_default_args_maxz_threshold_set():
    new_sensor = motor.create_sensor(0, 0, 0)
    assert new_sensor["max threshold"] == 1000

def test_create_sensor_default_args_min_threshold_set():
    new_sensor = motor.create_sensor(0, 0, 0)
    assert new_sensor["min threshold"] == 0
    
def test_create_sensor_default_args_sensor_threshold_set():
    new_sensor = motor.create_sensor(0, 0, 0)
    assert new_sensor["sensor threshold"] == 100

#  testing sensor initialization with custom arguments

def test_create_sensor_custom_args_motor_id_set():
    new_sensor = motor.create_sensor(0, 0, 0, 700, 30, 60)
    assert new_sensor["motor id"] == 0

def test_create_sensor_custom_args_sensor_id_set():
    new_sensor = motor.create_sensor(0, 0, 0, 700, 30, 60)
    assert new_sensor["sensor id"] == 0

def test_create_sensor_custom_args_sensor_pin_set():
    new_sensor = motor.create_sensor(0, 0, 0, 700, 30, 60)
    assert new_sensor["sensor pin"] == 0
    
def test_create_sensor_custom_args_max_threshold_set():
    new_sensor = motor.create_sensor(0, 0, 0, 700, 30, 60)
    assert new_sensor["max threshold"] == 700

def test_create_sensor_custom_args_min_threshold_set():
    new_sensor = motor.create_sensor(0, 0, 0, 700, 30, 60)
    assert new_sensor["min threshold"] == 30
    
def test_create_sensor_custom_args_sensor_threshold_set():
    new_sensor = motor.create_sensor(0, 0, 0, 700, 30, 60)
    assert new_sensor["sensor threshold"] == 60

# testing moving data initialization with default arguments

def test_create_moving_data_default_args_motor_id_set():
    new_moving_data = motor.create_moving_data(0, 250)
    assert new_moving_data["motor id"] == 0

def test_create_moving_data_default_args_destination_set():
    new_moving_data = motor.create_moving_data(0, 250)
    assert new_moving_data["destination"] == 250

def test_create_moving_data_default_args_rotation_direction_set():
    new_moving_data = motor.create_moving_data(0, 250)
    assert new_moving_data["direction"] == 0
    
def test_create_moving_data_default_args_pwm_rate_set():
    new_moving_data = motor.create_moving_data(0, 250)
    assert new_moving_data["rate"] == 0.005

def test_create_moving_data_default_args_time_of_last_set():
    new_moving_data = motor.create_moving_data(0, 250)
    assert new_moving_data["time of last"] == 0
    

# testing moving data initialization with custom arguments

def test_create_moving_data_custom_args_motor_id_set():
    new_moving_data = motor.create_moving_data(0, 250, 1, 0.0001, time.perf_counter())
    assert new_moving_data["motor id"] == 0

def test_create_moving_data_custom_args_destination_set():
    new_moving_data = motor.create_moving_data(0, 250, 1, 0.0001, time.perf_counter())
    assert new_moving_data["destination"] == 250

def test_create_moving_data_custom_args_rotation_direction_set():
    new_moving_data = motor.create_moving_data(0, 250, 1, 0.0001, time.perf_counter())
    assert new_moving_data["direction"] == 1
    
def test_create_moving_data_custom_args_pwm_rate_set():
    new_moving_data = motor.create_moving_data(0, 250, 1, 0.0001, time.perf_counter())
    assert new_moving_data["rate"] == 0.0001

def test_create_moving_data_custom_args_time_of_last_set():
    time_of_last = time.perf_counter()
    new_moving_data = motor.create_moving_data(0, 250, 1, 0.0001, time_of_last)
    assert new_moving_data["time of last"] == time_of_last