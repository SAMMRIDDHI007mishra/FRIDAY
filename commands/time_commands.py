from datetime import datetime

def get_time():
    current_time = datetime.now().strftime("%I:%M %p")
    return current_time