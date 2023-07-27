#!/usr/bin/env python3
from gpiozero import Button
import log
from log.log import info

bottom_event_name = f"{log.COLOR_RED}bottom_level_alert{log.COLOR_RESET}"
top_event_name = f"{log.COLOR_GREEN}top_level_alert{log.COLOR_RESET}"


def bottom_level_alert_on():
    info(f"evnet: {bottom_event_name} The Button for the top level is on.")


def bottom_level_alert_off():
    info(f"evnet: {bottom_event_name} The Button for the top level is off.")


def top_level_alert_on():
    info(f"evnet: {top_event_name} The Button for the top level is on.")


def top_level_alert_off():
    info(f"evnet: {top_event_name} The Button for the top level is off.")


if __name__ == '__main__':
    top_level_alert_button = Button(2)
    bottom_level_alert_button = Button(3)

    # Define the functions to be called when the button is pressed or released
    top_level_alert_button.when_pressed = top_level_alert_on
    top_level_alert_button.when_released = top_level_alert_off
    bottom_level_alert_button.when_pressed = bottom_level_alert_on
    bottom_level_alert_button.when_released = bottom_level_alert_off

    # Keep the program running to continue monitoring the button
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Exiting...")
