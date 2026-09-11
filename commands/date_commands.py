from datetime import datetime

def get_date():
    current_date = datetime.now().strftime("%d %B %Y")
    return current_date