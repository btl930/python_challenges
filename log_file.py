import datetime

user_input = input("Enter message.").strip()
x = datetime.datetime.now()
y = x.strftime("%x%X")
log = (y, user_input)

with open("log.txt", "a") as file:
    file.write(f"{log}")