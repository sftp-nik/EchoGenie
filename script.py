import speech_recognition as sr
import pyttsx3
import pywhatkit as pw
from datetime import date, datetime
import wikipedia
import requests
from bs4 import BeautifulSoup

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say("I am Alexa")
engine.runAndWait()

def get_weather_data(api_key, city_id):  
    api_url = "http://api.openweathermap.org/data/2.5/weather"  
    params = {  
        "id": city_id,  
        "units": "metric",  
        "appid": api_key  
    }  
    response = requests.get(api_url, params=params)  
    data = response.json()  
    return data

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source)
            command = listener.recognize_google(audio)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you repeat?")
        return ""
    except sr.RequestError:
        print("Sorry, I couldn't request results at the moment.")
        return ""
    
    return command

def get_weather(city):
    try:
        url = f"https://www.accuweather.com/en/in/{pune}/204848/weather-forecast/204848"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract weather information
        weather_desc = soup.find('span', attrs={'id': 'display-temp'}).text
        #temp = soup.find('span', attrs={'id': 'after-temp'}).text
        return f"The weather in {city} is {weather_desc}. The temperature is  degrees Celsius."
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return f"Sorry, I couldn't fetch weather information for {city}."

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk(f"Playing {song}")
        pw.playonyt(song)
    elif 'date' in command:
        today = date.today().strftime("%B %d, %Y")
        print(today)
        talk(f"Today's date is {today}")
    elif 'time' in command:
        current_time = datetime.now().strftime("%I:%M %p")
        print(current_time)
        talk(f"The current time is {current_time}")
    elif 'weather in' in command:
        city = command.replace('weather in', '').strip()
        weather_info = get_weather(city)
        print(weather_info)
        talk(weather_info)
    elif 'who is' in command:
        person = command.replace('who is', '').strip()
        info = wikipedia.summary(person, sentences=1)
        print(info)
        talk(info)
    elif 'stop' in command or 'exit' in command:
        talk("Goodbye!")
        exit()

    # you can add your own statement
    
    else:
        talk("Sorry, I can't help with that.")

while True:
    run_alexa()
# To initiaize alexa
