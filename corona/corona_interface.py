import pyttsx3
import speech_recognition as sr
import re
import pandas as pd
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image



countries = pd.read_csv('countries.csv', index_col=0)
countries.index += 1


# GLOBAL_PATTERNS = {
#     re.compile("[\w\s]*(total[\w\s]+cases)[\w\s]*(in\s\w*)"): get_totals,
#     re.compile("[\w\s]*(total[\w\s]+deaths)[\w\s]*(in\s\w*)"): get_totals,
#     re.compile("[\w\s]*total[\w\s]+active"): get_totals
# }
#


def get_totals(column, region='Global'):
    if region == 'Global':
        total = countries[column].sum()
        return(f'{column}: {total:,} globally')
    elif region in countries.Continent.unique():
        total = countries[countries['Continent'] == region][column].sum()
        return(f'{column}: {total:,} in {region}')
    elif region in countries.Country.unique():
        total = countries[countries['Country'] == region][column].sum()
        return(f'{column}: {total:,} in {region}')
    else:
        print("Entry not valid. Check your spelling")


def speak(entry):
    engine = pyttsx3.init()
    engine.say(entry)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            print("Listening....")
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: ", str(e))

    return said.lower()


#
# text = "Show me the total number of cases in Europe"
# text2 = "total deaths in Russia"

text = get_audio()

pattern = re.compile(
    "[\w\s]*(total)\s+[\w\s]*(cases|deaths)([\sin\s]*)([\w]*)")
matches = pattern.finditer(text)
for match in matches:
    column = match.group(1).capitalize() + " " + match.group(2).capitalize()
    region = match.group(4).capitalize()
    if region == "" or region == None:
        region = "Global"
    speak(get_totals(column, region))


# for pattern in pattern.items():
#     print(pattern.match(text))
# test_ctry = 'USA'
# x = countries[countries.Country == test_ctry]
#
#
#
#
#
#
#
#
#
# def main():
#     print("Started Program")
#     END_PHRASE = "stop"  # Stop recording with word 'stop'
#
#     while True:
#         print("Listening.....")
#         text = get_audio()
#         speak(text)
#
#         if text.find(END_PHRASE) != -1:
#             print("Exiting")
#             break
