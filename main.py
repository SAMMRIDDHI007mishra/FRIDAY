from commands.greetings import greet
from commands.time_commands import get_time
from commands.date_commands import get_date

from memory import remember, recall, forget

def clean_command(command):
    command = command.lower()
    command = command.strip()

    command = command.replace("?", "")
    command = command.replace("!", "")
    command = command.replace(".", "")

    if command.startswith("friday "):
        command = command[7:]

    return command


def get_intent(command):

    command = clean_command(command)

    if command in ["hello", "hi", "hey"]:
        return "greeting"

    elif command in ["how are you", "how are you doing"]:
        return "status"

    elif command in ["name", "what is your name", "who are you"]:
        return "identity"

    elif command in ["what is my name", "do you know my name"]:
        return "user_name"

    elif command in ["time", "what time is it", "tell me the time"]:
        return "time"

    elif command in [
        "date",
        "what is the date",
        "what's the date",
        "tell me the date",
        "what day is it"
    ]:
        return "date"

    elif command in ["what can you do", "help", "commands"]:
        return "help"

    elif command.startswith("remember"):
        return "remember"
    elif command.startswith("what do you remember about "):
        return "recall"
    elif command.startswith("forget "):
        return "forget"
    elif command in ["thanks", "thank you"]:
        return "thanks"

    elif command in ["bye", "goodbye", "quit", "exit"]:
        return "exit"

    else:
        return "unknown"


def process_command(command):

    intent = get_intent(command)

    if intent == "greeting":
        print("FRIDAY: Hello! How are you?")

    elif intent == "status":
        print("FRIDAY: I am functioning perfectly. Thank you for asking.")

    elif intent == "identity":
        print("FRIDAY: My name is FRIDAY.")

    elif intent == "user_name":
        print("FRIDAY: Your name is Samriddhi.")

    elif intent == "time":
        print("FRIDAY: The current time is", get_time())

    elif intent == "date":
        print("FRIDAY: Today's date is", get_date())

    elif intent == "help":
        print("\nFRIDAY can currently:")
        print("- Greet you")
        print("- Tell you the time")
        print("- Tell you the date")
        print("- Tell you your name")
        print("- Tell you about itself")
        print("- Respond to basic conversations")
        print("- Shut down when asked")

    elif intent == "remember":
        memory_text = clean_command(command)

        memory_text = memory_text.replace("remember ", "", 1)

        if " is " in memory_text:
            key, value = memory_text.split(" is ", 1)
            remember(key, value)

            print("FRIDAY: I'll remember that.")
        else:
            print("FRIDAY: Please tell me what you want me to remember.")
    elif intent == "recall":
        key = clean_command(command)
        key = key.replace("what do you remember about ", "", 1)
        value = recall(key)

        if value is not None:
            print("FRIDAY: " + key + " is " + value + ".")
        else:
            print("FRIDAY: I don't remember that yet.")
    elif intent == "forget":
        key = clean_command(command)
        key = key.replace("forget ", "", 1)
        if forget(key):
            print ("FRIDAY: I have forgotten that.")
        else:
            print("FRIDAY: I don't have that memory.")

    elif intent == "thanks":
        print("FRIDAY: You're welcome.")

    elif intent == "exit":
        print("FRIDAY: Goodbye. Shutting down.")
        return False

    else:
        print("FRIDAY: I am sorry, I don't understand that yet.")

    return True


def main():

    greet()

    while True:

        command = input("\nYou: ")

        if not process_command(command):
            break


main()