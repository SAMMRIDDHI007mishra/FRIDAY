from commands.greetings import greet
from commands.time_commands import get_time
from commands.date_commands import get_date
def process_command(command):
    if command in ["hello", "hi", "hey"]:
        print("FRIDAY: Hello! how are you?")
    elif command == "how are you":
        print("FRIDAY: I am functioning perfectly.Thank you for asking.")
    elif command == "name":
        print("FRIDAY: My name is FRIDAY")
    elif  command == "what is my name?":
        print("FRIDAY: Your name is Samriddhi")
    elif command in ["time","what time is it","tell me the time"]:
        print("FRIDAY: The current time is", get_time())
    elif command in ["date","what is the date today", "what date is it","what's the date"]:
        print("FRIDAY: Today's date is", get_date())
    elif command == "help":
        print("\navailable commands:")
        print("hello/hi/hey")
        print("how are you")
        print("name")
        print("time/what time is it/")
        print("date/what's the date")
        print("help")
        print("exit")
    elif command == "exit":
        print("FRIDAY: Goodbye. Shutting down.")
    else:
        print("FRIDAY: I don't understand that command yet.")
def main():
        greet()
        while True:

            command = input("\nYou: ").lower()
            process_command(command)
            if command == "exit":
                break
main()