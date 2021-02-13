import requests

sender = input("Your scullion wizard in the kitchen to help you!!!\nWhat is your name? ")

bot_message = ""

while bot_message != "Bye":
    message = input(sender +" >> ") 

    print("Sending message now...")

    r = requests.post("http://localhost:5002/webhooks/rest/webhook", json={"sender": sender, "message": message})

    print("Bot >>> : ", end="")
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")