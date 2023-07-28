#!/usr/bin/env python3
from dotenv import load_dotenv
from gpiozero import Button

import log
from log.log import info
from wecom_bot import send_notice

load_dotenv()

bottom_event_name = f"{log.COLOR_RED}bottom_level_alert{log.COLOR_RESET}"
top_event_name = f"{log.COLOR_GREEN}top_level_alert{log.COLOR_RESET}"


def bottom_level_alert_on():
    info(f"evnet: {bottom_event_name} The Button for the top level is on.")
    send_notice('低水位告警', '当前水位已不足, 请及时处理')


def bottom_level_alert_off():
    info(f"evnet: {bottom_event_name} The Button for the top level is off.")


def top_level_alert_on():
    info(f"evnet: {top_event_name} The Button for the top level is on.")
    send_notice('高水位告警', '当前水位已经溢出, 请及时处理')


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
