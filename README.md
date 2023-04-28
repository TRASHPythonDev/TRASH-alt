# TRASH API

This project is a Python API designed to control a robotic hand using an Arduino running Firmata Express. 

The API functions are generic enough to allow for low-level stepper motor control. The API requires a USB to an arduino board running Firmata or Firmata Express. 

Sensor polling for the system is handled automatically; however, sensors must be configured in order to be used. 

## Installation

Clone the repository and install the requirements:

```bash
git clone https://github.com/TRASHPythonDev/TRASH-alt.git
cd <project>
pip install -r requirements.txt
```

## Usage

Import the necessary modules:

```python
from basic_movement import BasicMovement
```

Create an instance of the `BasicMovement` class:

```python
basic_movement = BasicMovement(board_id=1)
```

To move a motor to a specific position, use the `move_motor_to_point()` function:

```python
basic_movement.move_motor_to_point(motor_id, destination, sensor_thresholds, rotation_direction=0, pwm_rate=0.05)
```

To move, call the `move()` function:

```python
basic_movement.move()
```

## API Functions

### `BasicMovement(board_id=1)`

Initializes a new instance of the `BasicMovement` class.

- `board_id` (int): the ID of the Arduino board that is connected to the computer (default: 1)

### `release_board()`

Clears the reference to the board and clears the connection. Call this function before calling `del` on a `BasicMovement` instance.

### `move_motor_to_point(motor_id: int, destination: int, sensor_thresholds: list, rotation_direction=0, pwm_rate=0.05) -> int`

Sets a motor to move to a given destination and stop when certain thresholds are met or when the destination is reached.

- `motor_id` (int): the ID of the motor that will be moved.
- `destination` (int): the destination in steps. If this is for a NEMA 17 stepper, then 400 is a full rotation.
- `sensor_thresholds` (list): the threshold percentage of each sensor's range. If greater than 100, movement becomes blind. This is stored between calls.
- `rotation_direction` (int): the rotation direction. Either 0 or 1.
- `pwm_rate` (float): the PWM rate. This has only been tested for values >= 0.0001.

### `move()`

Cycles all motors with pending move commands and moves them. The rate at which this is called determines the base motor turning rate and sensor sample rate. Run this at a value around or below 0.0001 times per second.

## Modules

### `motor.py`

Contains functions for creating and managing motor objects.

### `stepper_manager.py`

Contains functions for creating and managing stepper objects.

### `sensor_manager.py`

Contains functions for creating and managing sensor objects.

### `movement_arduino.py`

Contains functions for creating and managing the connection to the Arduino board.
