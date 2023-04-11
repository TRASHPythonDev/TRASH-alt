import motor
from time import perf_counter
from stepper_manager import StepperManager
from sensor_manager import SensorManager
from movement_arduino import BoardManager


class BasicMovement():
    __current_motor_id = 0
    __current_sensor_id = 0

    def __init__(self, board_id = 1) -> None:
        self.__stepper_manager = StepperManager()
        self.__sensor_manager = SensorManager()
        self.__board_manager = BoardManager(board_id)
        pass

    # clears reference to board and clears connection, call before calling del on BasicMovement instance
    def release_board(self) -> None:
        self.__board_manager.release_board()

    # this function cycles all objects in the moving list and moves them
    # the rate at which this is called determines base motor turning rate and sensor sample rate
    # running this at a value around or below 0.0001 times per second
    def move(self) -> None:
        moving_list_ids = self.__stepper_manager.get_moving_list_ids() # get list of all motor ids in moving list
        for motor_id in moving_list_ids: # cycle through all motor ids in moving list
            motor_data = self.__stepper_manager.get_master_data_by_id(motor_id) # get motor data for given id
            moving_data = self.__stepper_manager.get_moving_data_by_id(motor_id) # get movement data for given id
            sensor_id_list = self.__sensor_manager.get_all_associated_for_motor_id(motor_id) # get sensor id list for given motor id
            movement_complete = False # set movement complete flag for this motor to false
            for sensor_id in sensor_id_list: # cycle all sensors 
                sensor_data = self.__sensor_manager.get_master_data_by_sensor_id(sensor_id) # for given sensor id get the sensor data
                sensor_reading = self.__board_manager.read_analog_pin(sensor_data["sensor pin"]) # read analog data for given sensor
                if(sensor_reading >= sensor_data["sensor threshold"] * (sensor_data["max threshold"] - sensor_data["min threshold"]) / 100): # compare sensor data to threshold percentage
                    movement_complete = True # if sensor reading exceeds sensor threshold percentage, we are done moving this motor
            # if movement in range continue
            if(motor_data["max rotation"] > motor_data["motor position"] and motor_data["min rotation"] <= motor_data["motor position"]):
                pass # this line does nothing other than keep python happy
            else: # if outside of range then stop 
                movement_complete = True # if motor position is outside range, we are done moving the motor
            # if movement is not done, and we have exceeded minimum rate and have not reached destination then step
            if(movement_complete == False and perf_counter() - moving_data["time of last"] > moving_data["rate"] and moving_data["destination"] > motor_data["motor position"]):
                self.__board_manager.step(motor_data["pwm pin"]) # step the stepper motor forward one pulse
                self.__stepper_manager.set_motor_position_by_id(motor_id,motor_data["motor position"] + 1) # increment position counter
            elif (moving_data["destination"] >= motor_data["motor position"]): # if motor position is at or exceeds destination we are done moving
                movement_complete = True # if motor position is at destination range, we are done moving the motor
            if(movement_complete == True): # if movement complete flag set
                self.__stepper_manager.move_to_ready(motor_id) # move motor to ready table if done
        pass

    # sets motor to move to a given destination and stop when certain thresholds are met or when destination reached
    # motor_id: int             - must be valid motor id, if no motors have been deleted then this is simply an integer < __current_motor_id
    # destination: int          - destination in steps, if this is for a nema 17 stepper then 400 is a full rotation 
    # sensor_thresholds: list   - as a percentage of each sensor's range, if greater than 100 movement becomes blind, this is stored between calls
    # rotation_direction: int   - either 0 or 1 no idea which is cw or ccw, but this can be determined experimentally
    # pwm_rate: float           - this has only been tested for values >= 0.0001, this is ridiculously fast for a nema 17
    def move_motor_to_point(self, motor_id: int, destination: int, sensor_thresholds: list, rotation_direction = 0, pwm_rate = 0.05) -> int:
        if (self.__stepper_manager.get_if_id_in_use(motor_id) == False): # if motor does not exist kill method
            return -1 # exit prior to anything, return failure
        if (self.__stepper_manager.get_if_id_in_moving_list(motor_id)): # if motor already moving kill movement
            self.__stepper_manager.move_to_ready(motor_id) # put motor in ready state, kill movement
        motor_data = self.__stepper_manager.get_master_data_by_id(motor_id) # get data for given motor id
        new_moving_data = motor.create_moving_data(motor_id, destination, rotation_direction, pwm_rate, 0) # create data to pass to stepper manager
        direction_pin = motor_data["direction pin"] # get direction pin out for given motor
        self.__board_manager.set_stepper_direction(direction_pin, rotation_direction) # set rotation direction and pin based on data retrieved by id
        self.__stepper_manager.move_to_moving(new_moving_data) # place moving data in moving table
        motor_sensor_id_list = self.__sensor_manager.get_all_associated_for_motor_id(motor_id) # create list of sensors associated with motor
        j = 0 # set increment for sensor threshold list to 0
        for sensor_id in motor_sensor_id_list: # cycle through each sensor associated with motor
            if j < len(sensor_thresholds): # if we haven't run out of inputs in the sensor thresholds list then continue
                self.__sensor_manager.set_sensor_threshold_by_id(sensor_id, sensor_thresholds[j])
                j = j + 1 # increment through sensor threshold list
            else: # if we have exceeded the number of threshold inputs then break out of loop
                break # cancel loop
        return 0

    # sets motor to move to a given destination and stop when destination reached this method ignores sensors
    # motor_id: int             - must be valid motor id, if no motors have been deleted then this is simply an integer < __current_motor_id
    # destination: int          - destination in steps, if this is for a nema 17 stepper then 400 is a full rotation 
    # rotation_direction: int   - either 0 or 1 no idea which is cw or ccw, but this can be determined experimentally
    # pwm_rate: float           - this has only been tested for values >= 0.0001, this is rediculusly fast for a nema 17
    def move_motor_to_point_blind(self, motor_id: int, destination: int, rotation_direction = 0, pwm_rate = 0.05) -> int:
        sensor_thresholds = [200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200] # threshold so high cannot reach, enough for 25 sensors
        return self.move_motor_to_point(motor_id, destination, sensor_thresholds, rotation_direction, pwm_rate) # call normal move to point but with custom thresholds
        

    # create a new motor to control
    # pwm_pin: int              - arduino digital pin or pwm pin to set to digital output mode
    # direction_pin: int        - arduino digital pin to set to digital output mode
    # maximum_rotation: int     - maximum rotation for stepper motor 400 for nema 17 stepper motor
    # minimum_rotation: int     - minimum rotation for stepper motor 0 for nema 17 stepper motor
    # motor_position: int       - current motor position as an integer defaults to 0
    # motor_name: str           - is just a freindly name as a means of alternate lookup 
    def create_motor_and_add(self, pwm_pin: int, direction_pin: int, maximum_rotation = 400, minimum_rotation = 0, motor_position = 0, motor_name = "") -> int:
        if(maximum_rotation < minimum_rotation): # if rotation range is reversed
             maximum_rotation = 400 # set to defaults if rotation range is bad
             minimum_rotation = 0 # set to defaults if rotation range is bad
        new_motor = motor.create_motor(BasicMovement.__current_motor_id, pwm_pin, direction_pin, maximum_rotation, minimum_rotation, motor_position, motor_name) # create new motor for assignment to stepper list
        self.__stepper_manager.add_stepper(new_motor) # add motor to stepper list
        self.__board_manager.activate_pins_for_output([pwm_pin, direction_pin]) # activate pins for output
        BasicMovement.__current_motor_id = BasicMovement.__current_motor_id + 1 # increment motor id number 
        return BasicMovement.__current_motor_id - 1 # return the id just created
    
    # create new sensor to read
    # motor_id: int             - must be valid motor id, if no motors have been deleted then this is simply an integer < __current_motor_id
    # sensor_pin: int           - arduino analog pin to set to analog input mode
    # maximum_threshold: int    - maximum sensor "voltage" reading generally about 1000 for arduino analog input with supply of 5 volts, 600ish with supply of 3.3 volts
    # minimum_threshold: int    - minimum sensor "voltage" reading generally about 0 is good, will likely be higher for our tension sensors
    # sensor_threshold: int     - sensor threshold percentage 0 to 100 range, if set higher than 100 will result in sensor being ignored
    def create_sensor_and_add(self, motor_id: int, sensor_pin: int, maximum_threshold = 1000, minimum_threshold = 0, sensor_threshold = 100) -> int:
        new_sensor = motor.create_sensor(motor_id, BasicMovement.__current_sensor_id, sensor_pin, maximum_threshold, minimum_threshold, sensor_threshold) # create new sensor for assignment to sensor list
        self.__sensor_manager.add_sensor(new_sensor) # add sensor to sensor manager
        self.__board_manager.activate_pins_for_analog_input([sensor_pin]) # activate pin for input
        BasicMovement.__current_sensor_id = BasicMovement.__current_sensor_id + 1 # increment sensor id number
        return BasicMovement.__current_sensor_id - 1 # return the id just created

    # returns motor id given the name of the motor
    # motor_id: int             - must be valid motor id, if no motors have been deleted then this is simply an integer < __current_motor_id
    def get_motor_id_by_name(self, motor_name: str) -> int:
        return self.__stepper_manager.get_master_data_by_name(motor_name)["motor id"] 

    # returns position of given motor
    # motor_id: int             - must be valid motor id, if no motors have been deleted then this is simply an integer < __current_motor_id
    def get_motor_position(self, motor_id: int) -> int:
        return self.__stepper_manager.get_master_data_by_id(motor_id)["motor position"] 
    
    # sets position of given motor, useful for nulling on startup
    # motor_id: int             - must be valid motor id
    # motor_position: int       - current motor position to be set  
    def set_motor_position(self, motor_id: int, motor_position: int) -> None:
        self.__stepper_manager.set_motor_position_by_id(motor_id, motor_position)
        pass
    
    # returns threshold of given sensor
    # sensor_id: int             - must be valid sensor id, if no sensors have been deleted then this is simply an integer < __current_sensor_id
    def get_sensor_threshold(self, sensor_id: int) -> int:
        return self.__sensor_manager.get_master_data_by_sensor_id(sensor_id)["sensor threshold"] 
    
    # returns all sensors associated with a motor
    def get_all_sensor_ids_for_motor(self, motor_id: int) -> list:
        return self.__sensor_manager.get_all_associated_for_motor_id(motor_id)

    # returns a list of all motor ids that are ready
    def get_all_active_motor_ids(self) -> list:
        return self.__stepper_manager.get_moving_list_ids()

    # returns a list of all motor ids that are moving
    def get_all_ready_motor_ids(self) -> list:
        return self.__stepper_manager.get_ready_list_ids()

    # checks if motor still exists and deletes if it does, checks for associated sensors and deletes them also
    # motor_id: int             - must be valid motor id, if no motors have been deleted then this is simply an integer < __current_motor_id
    def delete_motor(self, motor_id: int) -> None:
        if (self.__stepper_manager.get_if_id_in_use(motor_id)):
            self.__stepper_manager.remove_stepper(motor_id)
            sensor_id_list = []
            sensor_id_list = self.__sensor_manager.get_all_associated_for_motor_id(motor_id)
            for id in sensor_id_list:
                self.delete_sensor(id)
        pass

    # checks if sensor still exists and deletes if it does
    # sensor_id: int             - must be valid sensor id, if no sensors have been deleted then this is simply an integer < __current_sensor_id
    def delete_sensor(self, sensor_id: int) -> None:
        if (self.__sensor_manager.get_if_id_in_use(sensor_id)):
            self.__sensor_manager.remove_sensor(sensor_id)
        pass
    
    @classmethod # when requested will return the id of the next motor to be instantiated
    def get_next_motor_id(self) -> int:
        return self.__current_motor_id
    
    @classmethod # when requested will return the id of the last motor to be instantiated
    def get_last_motor_id(self) -> int:
        return self.__current_motor_id - 1
    
    @classmethod # when requested will return the id of the next sensor to be instantiated
    def get_next_sensor_id(self) -> int:
        return self.__current_sensor_id
    
    @classmethod # when requested will return the id of the next sensor to be instantiated
    def get_last_sensor_id(self) -> int:
        return self.__current_sensor_id - 1
    
