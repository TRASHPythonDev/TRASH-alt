import motor
import pytest
from basic_movement import BasicMovement

# this test requires an arduino connected with firmata express and board id = 1 set
@pytest.mark.arduino
@pytest.mark.slow
def test_initialize_basic_movement_create_motor_and_add_default_arguments():
    new_basic_movement = BasicMovement()
    id = BasicMovement.get_next_motor_id()
    new_basic_movement.create_motor_and_add(2, 22)
    new_basic_movement.release_board()
    assert BasicMovement.get_last_motor_id() == id

# this test requires an arduino connected with firmata express and board id = 1 set
@pytest.mark.arduino
@pytest.mark.slow
def test_initialize_basic_movement_create_motor_and_add_default_arguments_check_if_ready():
    new_basic_movement = BasicMovement()
    new_basic_movement.create_motor_and_add(2, 22)
    new_basic_movement.release_board()
    motor_id_list = new_basic_movement.get_all_ready_motor_ids()
    exists_and_ready = False
    for id in motor_id_list:
        if (BasicMovement.get_last_motor_id()) == id:
            exists_and_ready = True
    assert exists_and_ready

# this test requires an arduino connected with firmata express and board id = 1 set
@pytest.mark.arduino
@pytest.mark.slow
def test_initialize_basic_movement_create_motor_and_create_sensor_and_add_default_arguments():
    new_basic_movement = BasicMovement()
    id = BasicMovement.get_next_sensor_id()
    new_basic_movement.create_motor_and_add(2, 22)
    new_basic_movement.create_sensor_and_add(BasicMovement.get_last_motor_id(), 0)
    new_basic_movement.release_board()
    assert BasicMovement.get_last_sensor_id() == id


# this test requires an arduino connected with firmata express and board id = 1 set
@pytest.mark.arduino
@pytest.mark.slow
def test_initialize_basic_movement_create_motor_and_create_sensor_and_add_default_arguments_move_blind_check_if_moving():
    new_basic_movement = BasicMovement()
    new_basic_movement.create_motor_and_add(2, 22)
    new_basic_movement.create_sensor_and_add(BasicMovement.get_last_motor_id(), 0)
    new_basic_movement.move_motor_to_point_blind(BasicMovement.get_last_motor_id(), 400)
    new_basic_movement.release_board()
    motor_id_list = new_basic_movement.get_all_active_motor_ids()
    exists_and_active = False
    for id in motor_id_list:
        if (BasicMovement.get_last_motor_id()) == id:
            exists_and_active = True
    assert exists_and_active

# this test requires an arduino connected with firmata express and board id = 1 set
@pytest.mark.arduino
@pytest.mark.slow
def test_initialize_basic_movement_create_motor_and_create_sensor_and_add_default_arguments_move_blind_check_threshold_set():
    new_basic_movement = BasicMovement()
    new_basic_movement.create_motor_and_add(2, 22)
    new_basic_movement.create_sensor_and_add(BasicMovement.get_last_motor_id(), 0)
    new_basic_movement.move_motor_to_point_blind(BasicMovement.get_last_motor_id(), 400)
    new_basic_movement.release_board()
    assert new_basic_movement.get_sensor_threshold(BasicMovement.get_last_sensor_id()) == 200

# this test requires an arduino connected with firmata express and board id = 1 set
@pytest.mark.arduino
@pytest.mark.slow
def test_initialize_basic_movement_create_motor_and_create_sensor_and_add_default_arguments_move_check_if_moving():
    new_basic_movement = BasicMovement()
    new_basic_movement.create_motor_and_add(2, 22)
    new_basic_movement.create_sensor_and_add(BasicMovement.get_last_motor_id(), 0)
    new_basic_movement.move_motor_to_point(BasicMovement.get_last_motor_id(), 400, [40])
    new_basic_movement.release_board()
    motor_id_list = new_basic_movement.get_all_active_motor_ids()
    exists_and_active = False
    for id in motor_id_list:
        if (BasicMovement.get_last_motor_id()) == id:
            exists_and_active = True
    assert exists_and_active
    
# this test requires an arduino connected with firmata express and board id = 1 set
@pytest.mark.arduino
@pytest.mark.slow
def test_initialize_basic_movement_create_motor_and_create_sensor_and_add_default_arguments_move_check_if_threshold_set():
    new_basic_movement = BasicMovement()
    new_basic_movement.create_motor_and_add(2, 22)
    new_basic_movement.create_sensor_and_add(BasicMovement.get_last_motor_id(), 0)
    new_basic_movement.move_motor_to_point(BasicMovement.get_last_motor_id(), 400, [40])
    new_basic_movement.release_board()
    assert new_basic_movement.get_sensor_threshold(BasicMovement.get_last_sensor_id()) == 40


# this test requires an arduino connected with firmata express and board id = 1 set
@pytest.mark.arduino
@pytest.mark.slow
def test_initialize_basic_movement_create_motor_and_create_sensor_default_arguments_manual_null_for_position():
    new_basic_movement = BasicMovement()
    motor_id = new_basic_movement.create_motor_and_add(2, 22)
    new_basic_movement.create_sensor_and_add(motor_id, 0)
    new_basic_movement.move_motor_to_point(motor_id, 400, [40])
    new_basic_movement.release_board()
    new_basic_movement.set_motor_position(motor_id, 200)
    assert new_basic_movement.get_motor_position(motor_id) == 200

# this test requires an arduino connected with firmata express and board id = 1 set
@pytest.mark.arduino
@pytest.mark.slow
def test_initialize_basic_movement_create_motor_and_create_sensor_and_add_default_arguments_move_verify_start_finish():
    new_basic_movement = BasicMovement()
    motor_id = new_basic_movement.create_motor_and_add(2, 22)
    new_basic_movement.create_sensor_and_add(motor_id, 0)
    new_basic_movement.move_motor_to_point(motor_id, 400, [40])
    assert new_basic_movement.get_all_active_motor_ids() != []
    while new_basic_movement.get_all_active_motor_ids() != []:
        new_basic_movement.move()
    new_basic_movement.release_board()
    assert new_basic_movement.get_all_active_motor_ids() == []

# this test requires an arduino connected with firmata express and board id = 1 set, recommend connecting sensors, otherwise voltage may drift and cancel movement early
@pytest.mark.arduino
@pytest.mark.slow
def test_initialize_basic_movement_create_motor_and_create_sensor_and_add_default_arguments_move_verify_end_point():
    new_basic_movement = BasicMovement()
    motor_id = new_basic_movement.create_motor_and_add(2, 22)
    new_basic_movement.create_sensor_and_add(motor_id, 0)
    new_basic_movement.move_motor_to_point(motor_id, 250, [40])
    while new_basic_movement.get_all_active_motor_ids() != []:
        new_basic_movement.move()
    new_basic_movement.release_board()
    assert new_basic_movement.get_motor_position(motor_id) == 250

# this test requires an arduino connected with firmata express and board id = 1 set, recommend connecting sensors, otherwise voltage may drift and cancel movement early
@pytest.mark.arduino
@pytest.mark.slow
def test_initialize_basic_movement_create_motor_and_create_sensor_and_add_default_arguments_move_past_max_rotation_verify_end_point():
    new_basic_movement = BasicMovement()
    motor_id = new_basic_movement.create_motor_and_add(2, 22)
    new_basic_movement.create_sensor_and_add(motor_id, 0)
    new_basic_movement.move_motor_to_point(motor_id, 800, [100])
    while new_basic_movement.get_all_active_motor_ids() != []:
        new_basic_movement.move()
    new_basic_movement.release_board()
    assert new_basic_movement.get_motor_position(motor_id) == 400

# this test requires an arduino connected with firmata express and board id = 1 set
@pytest.mark.arduino
@pytest.mark.slow
def test_initialize_basic_movement_create_motor_and_create_sensor_and_delete_both_and_check():
    new_basic_movement = BasicMovement()
    motor_id = new_basic_movement.create_motor_and_add(2, 22)
    new_basic_movement.create_sensor_and_add(motor_id, 0)
    new_basic_movement.delete_motor(motor_id)
    new_basic_movement.release_board()
    assert new_basic_movement.get_all_ready_motor_ids() == []
    assert new_basic_movement.get_all_sensor_ids_for_motor(motor_id) == []

# this test requires an arduino connected with firmata express and board id = 1 set
@pytest.mark.arduino
@pytest.mark.slow
def test_initialize_basic_movement_create_motor_and_create_sensor_and_delete_both_delete_manager():
    new_basic_movement = BasicMovement()
    motor_id = new_basic_movement.create_motor_and_add(2, 22)
    new_basic_movement.create_sensor_and_add(motor_id, 0)
    new_basic_movement.delete_motor(motor_id)
    new_basic_movement.release_board()
    del new_basic_movement
    with pytest.raises(UnboundLocalError):
        new_basic_movement == None