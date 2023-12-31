# Raspberry Pi Water Level Alarm

## Introduction
This is a Raspberry Pi project for a water level alarm. The project monitors the water level and sends an alert when the water level is too high or too low.

## Dependencies
- Python version: 3
- Virtual environment (venv) for managing dependencies
- Operating System: Raspberry Pi OS

## Raspberry pi gpio connections

gpio wiring position 

* Lower water level: gpio2 -> GND  
* Upper water level: gpio3 -> GND

## Installation
1. Clone the project repository:
```bash
git clone https://github.com/wuchuhengtools/water_level_walam_gpio_python.git
cd raspberry-water-level-alarm
```
2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install project dependencies

```bash
pip install -r requirements.txt
```

4. update requirements.txt
```bash 
pip freeze > requirements.txt
```
## Startup
To start the water level alarm, run the following command:

```bash 
python3 src/main.py
```

## Testing
To execute tests for the project, use the following command:

```bash
python -m unittest discover tests
```
## Issue Submission
If you encounter any issues or have suggestions for improvements, please submit an issue on the project's GitHub repository. Be sure to include detailed information about the problem or feature request.

## Development License
This project is open-source and is licensed under the MIT License. You can find the license details in the `LICENSE` file.
