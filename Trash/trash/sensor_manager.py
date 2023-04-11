# contains functions for managing sensor lists

import motor


class SensorManager():

    def __init__(self) -> None:
        self.__master_list = []
        pass

    # creates a new motor object and adds it to the master list, then adds its id to a stepper list identifying it as a stepper 
    def add_sensor(self, sensor: dict) -> None:
        self.__master_list.append(sensor)
        pass

    def remove_sensor(self, id:int) -> None:
        self.__master_list.remove(self.get_master_data_by_sensor_id(id))
        pass

    #return data for given sensor id
    def get_master_data_by_sensor_id(self, id:int) -> dict:
        for i in self.__master_list:
            if(i["sensor id"] == id): # lookup id for sensor item in list and compare to given id
                return i
        raise LookupError("Sensor id not in list")
        
    #returns all sensor data for given motor id
    def get_all_master_data_for_motor_id(self, id:int) -> list:
        sensor_list = []
        for i in self.__master_list:
            if(i["motor id"] == id): # lookup id for motor item in list and compare to given id
                sensor_list.append(i)
        return sensor_list
    
    # given sensor id, set sensor threshold percentage to given sensor threshold value
    def set_sensor_threshold_by_id(self, id: int, sensor_threshold: int) -> None:
        for i in range(len(self.__master_list)): # cycle master list
            temp_sensor = self.__master_list[i] # create instance variable for sensor data in given cycle
            if(temp_sensor["sensor id"] == id): # lookup id for sensor item in list and compare to given id
                temp_sensor["sensor threshold"] = sensor_threshold # if matches, modify instance variable
                self.__master_list[i] = temp_sensor # replace item at current index with modified instance variable
    
    # returns all sensor ids associated with motor id
    def get_all_associated_for_motor_id(self, id:int) -> list:
        sensor_id_list = []
        for i in self.__master_list:
            if(i["motor id"] == id): # lookup id for motor item in list and compare to given id
                sensor_id_list.append(i["sensor id"])
        return sensor_id_list
            
    #check if sensor id in use by looking in master table
    def get_if_id_in_use(self, id:int) -> bool:
        for i in self.__master_list:
            if(i["sensor id"] == id): # lookup id for sensor item in list and compare to given id
                return True
        return False
            
    # get list functions
    # made private, likely to deprecate in future release
    def __get_master_list(self) -> list:
        return self.__master_list