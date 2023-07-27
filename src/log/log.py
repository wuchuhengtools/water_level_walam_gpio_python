from datetime import datetime


def info(msg):
    # Get the current time
    current_time = datetime.now()
    # Format the time as "12:00:00"
    formatted_time = current_time.strftime("%H:%M:%S")
    print(f"{formatted_time} {msg}")
