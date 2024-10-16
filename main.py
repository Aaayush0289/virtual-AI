import datetime
import os
import random
import string
import requests
import speech_recognition as sr
import pyttsx3
import webbrowser
from openai import OpenAI

client = OpenAI(api_key="sk-proj-PSRZ22rmMehMGEuUgk3DT3BlbkFJt1QC3DPqNaqLIDxVrGTs")


def chat(statement):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": statement
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response.choices[0].message.content)
    say(response.choices[0].message.content)


def ai(query_func):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": query_func
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response.choices[0].message.content)
    set_characters = string.digits + string.ascii_lowercase + string.ascii_uppercase
    name = ''.join(random.choice(set_characters) for _ in range(10))
    file_path = os.path.join("./Openai", name)
    with open(file_path, 'a') as file:
        file.write(response.choices[0].message.content)

    say("Master, Your answer is present in Open AI folder")


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        print("listening.....")
        audio = r.listen(source)
        print("completed.....")
        try:
            query = r.recognize_google(audio, language="Fr")
            print(query)
            return query

        except Exception as e:
            return "Sorry, I could not understand audio."


while True:
    if __name__ == "__main__":
        query = takeCommand()

        # open websites
        list2 = ['youtube', 'linkedin', 'facebook', 'instagram', 'google', 'wikipedia', 'twitter', 'whatsapp','chess']
        val = False
        for site in list2:
            if f"open {site}" in query.lower():
                webbrowser.open(f"https://{site}.com")
                say(f"Opening {site} sir")
                val = True


        if val :
            continue
            # greeting

        if "how" in query.lower():
            say("Master I am fine. how can i help you")


        elif "hello jarvis" in query.lower():
            say("Hello master")

        # motivation quotes
        elif "motivate" in query.lower():
            say('Common master get up and do your work. you are the best master and it is time to show the world what '
                'can you do')

        # time
        elif "time" in query.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {strfTime}")

        elif "date" in query.lower():
            strdate = datetime.datetime.now().strftime("%Y:%B:%d")
            say(f"Sir the date is {strdate}")

        elif "date and time" in query.lower():
            strdate = datetime.datetime.now().strftime("%Y:%B:%d")
            say(f"Sir the date is {strdate}")

            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {strfTime}")

        # opening apps in system

        elif "open pycharm" in query.lower():
            say('opening pycharm')
            os.startfile(
                "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm Community Edition 2022.3.3.lnk")


        elif "open chrome" in query.lower():
            say('opening chrome master')
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk")


        elif "open ms word" in query.lower():
            say('opening ms word master')
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk")


        elif "open powerpoint" in query.lower():
            say('opening powerpoint master')
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk")


        elif "print" in query.lower():
            ai(query)

        elif "weather" in query.lower():
            say("Of which city you want to know the weather")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.pause_threshold = 0.5
                print("listening the name of the city.....")
                audio = r.listen(source)
                print("listened to the name of the city....")
                try:
                    city_name = r.recognize_google(audio, language='en-in')
                    print(city_name)
                    url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"
                    headers = {
                        "X-RapidAPI-Key": "08c7795a32mshe3a9c4179b4f08dp1fcf29jsnd641d1111616",
                        "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
                    }
                    querystring = {"city": city_name}
                    response = requests.get(url, headers=headers, params=querystring)
                    print(response.json())
                    say(f"The temperature of the city is {response.json()['temp']} degree celcius")
                    say(f"The humidity of the city is {response.json()['humidity']}")


                except Exception as e:
                    say("Sorry, can't find the weather of the city")
                    print(e)

        elif "current affairs" in query.lower():
            url = "https://current-affairs-of-india.p.rapidapi.com/recent"

            headers = {
                "X-RapidAPI-Key": "08c7795a32mshe3a9c4179b4f08dp1fcf29jsnd641d1111616",
                "X-RapidAPI-Host": "current-affairs-of-india.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers)

            for elem in response.json():
                say(elem.split(":")[0])

        else:
            chat(query)
