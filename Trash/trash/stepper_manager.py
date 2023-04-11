# contains functions and lists for managing motors, motor behavior related files use this file

import motor


class StepperManager():

    def __init__(self) -> None:
        self.__master_list = []
        self.__ready_list = []
        self.__moving_list = [] 
        pass

    # creates a new motor object and adds it to the master list, then adds its id to a stepper list identifying it as a stepper 
    # moving_data: dict             - must be valid moving data dictionary (you will regret if not)
    def add_stepper(self, motor: dict) -> None:
        self.__master_list.append(motor)
        self.__ready_list.append(motor["motor id"])
        pass

    # removes data from lists given id
    # motor_id: int             - hopefully a valid motor id
    def remove_stepper(self, id:int) -> None:
        self.__master_list.remove(self.get_master_data_by_id(id))
        if(self.get_if_id_in_ready_list(id)):
            self.__ready_list.remove(id)
        if(self.get_if_id_in_moving_list(id)):
            self.move_to_ready(id)
            self.__ready_list.remove(id)
        pass

    # checks if given id is in the stepper ready list
    # motor_id: int             - any integer, hopefully a valid motor id, this will verify if it is ready
    def get_if_id_in_ready_list(self, id:int) -> bool:
        return True if id in self.__ready_list else False

    # checks if given id is in the stepper moving list
    # motor_id: int             - any integer, hopefully a valid motor id, this will verify if it is moving
    def get_if_id_in_moving_list(self, id: int) -> bool:
        for i in self.__moving_list:
            if(i["motor id"] == id): # lookup id for motor item in list and compare to given id
                return True
        return False    

    # checks if given id is in the master list by checking other lists
    # motor_id: int             - any integer, hopefully a valid motor id, this will verify if it is one
    def get_if_id_in_use(self, id: int) -> bool:
        return (self.get_if_id_in_ready_list(id) or self.get_if_id_in_moving_list(id))    
        
    # moves given motor to moving table, throws an error if it isn't ready
    # moving_data: dict             - must be valid moving data dictionary created with valid motor ids (maybe? error might not occur)
    def move_to_moving(self, moving_data: dict) -> None:
        if(self.get_if_id_in_ready_list(moving_data["motor id"])):
            self.__moving_list.append(moving_data)
            self.__ready_list.remove(moving_data["motor id"])
        elif(self.get_if_id_in_moving_list(moving_data["motor id"])):
            raise RuntimeError("Stepper already moving")
        else:
            raise LookupError("Stepper id invalid")
        pass

    # moves given motor to the ready table, throws an error if it doesn't 
    # motor_id: int             - must be valid motor id or an error will occur (maybe? error might not occur)
    def move_to_ready(self, id: int) -> None:
        if(self.get_if_id_in_moving_list(id)):
            self.__ready_list.append(id)
            for i in self.__moving_list:
                if(i["motor id"] == id): # lookup id for motor item in list and compare to given id
                    self.__moving_list.remove(i) 
        elif (self.get_if_id_in_ready_list(id)):
            raise RuntimeError("Stepper already ready")
        else:
            raise LookupError("Stepper id invalid")
        pass

    # returns all motor data for a given id
    # motor_id: int             - must be valid motor id or an error will occur
    def get_master_data_by_id(self, id:int) -> dict:
        for motor in self.__master_list: # for every motor in the master list 
            if(motor["motor id"] == id): # lookup id for motor item in list and compare to given id
                return motor # return the motor data if ids match
        raise LookupError("Motor with this id not in master list")
            
    # sets a motor's (by id) position
    # motor_id: int             - should be valid motor id or nothing will happen
    # motor_position: int       - current motor position as an integer, will update to value given
    def set_motor_position_by_id(self, id: int, motor_position: int) -> None:
        for i in range(len(self.__master_list)): # iterate through master list
            if(self.__master_list[i]["motor id"] == id): # lookup id for motor item in list and compare to given id
                self.__master_list[i]["motor position"] = motor_position # if equal assign position to matchin id in master list
    
    # returns the moving data by a given motor id
    # motor_id: int             - must be valid motor id or an error will occur
    def get_moving_data_by_id(self, id:int) -> dict:
        for moving_data in self.__moving_list: # for every moving data entry in the moving list
            if(moving_data["motor id"] == id): # lookup id for motor item in list and compare to given id
                return moving_data # if an id matches the on given, return the moving data
        raise LookupError("Motor with this id not in moving list") # otherwise throw lookup error
            
    # returns the motor data associated with a given name
    # motor_name: str           - is just a friendly name as a means of alternate lookup 
    def get_master_data_by_name(self, name:str) -> dict:
        for motor in self.__master_list: # for every motor entry in master list
            if(motor["motor name"] == name): # lookup id for motor item in list and compare to given id
                return motor # if they are the same return the motor data
        raise LookupError("Motor with this name not in list") # if not raise a lookup error

    # returns all motor ids that are ready
    def get_ready_list_ids(self) -> list:
        id_list = [] # create empty list
        for id in self.__ready_list: # for every motor in the ready list
            id_list.append(id) # append the motor id to the list
        return id_list # return the list

    # returns all motor ids that are moving
    def get_moving_list_ids(self) -> list:
        id_list = [] # create empty list
        for motor in self.__moving_list: # for every motor in the moving list
            id_list.append(motor["motor id"]) # append the motor id to the list
        return id_list # return the list

    # get list functions
    # made private, likely to deprecate in future release
    def __get_master_list(self) -> list:
        return self.__master_list

    def __get_ready_list(self) -> list:
        return self.__ready_list
    
    def __get_moving_list(self) -> list:
        return self.__moving_list
