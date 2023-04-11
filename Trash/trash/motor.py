# functions to create stepper motor, sensor, and moving data variable types

def create_motor(motor_id: int, pwm_pin: int, direction_pin: int, maximum_rotation = 400, minimum_rotation = 0, motor_position = 0, motor_name = "") -> dict: 
    motor = {
        "motor id": motor_id,
        "pwm pin": pwm_pin,
        "direction pin": direction_pin,
        "max rotation": maximum_rotation,
        "min rotation": minimum_rotation, 
        "motor position": motor_position, 
        "motor name": motor_name
    }
    return motor

def create_sensor(motor_id: int, sensor_id: int, sensor_pin: int, maximum_threshold = 1000, minimum_threshold = 0, sensor_threshold = 100) -> dict:
    sensor = {
        "motor id": motor_id,
        "sensor id": sensor_id,
        "sensor pin": sensor_pin,
        "max threshold": maximum_threshold,
        "min threshold": minimum_threshold, 
        "sensor threshold": sensor_threshold
    }
    return sensor

def create_moving_data(motor_id: int, destination: int, rotation_direction = 0, pwm_rate = 0.005, time_of_last = 0) -> dict:
    moving_data = {
        "motor id": motor_id,
        "destination": destination,
        "direction": rotation_direction,
        "time of last": time_of_last,
        "rate": pwm_rate
    }
    return moving_data

