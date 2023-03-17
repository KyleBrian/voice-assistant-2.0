from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys
import os

recognizer = speech_recognition.Recognizer()
speaker = tts.init()
speaker.setProperty ('rate' , 150)



todo_list= ['go shopping','clean room' 'record video']

def hello():
    speaker.say("Hello,What can i do for you?")
    speaker.runAndWait()

def create_note():

    global recognizer

    speaker.say("What do you want to write to your note?")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with speech_recognition.Microphone()as mic:
                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio=recognizer.listen(mic)

                note=recognizer.recognize_google(audio)
                note=note.lower()


                speaker.say("Choose filename")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio=recognizer.listen(mic)

                filename=recognizer.recognize_google(audio)
                filename=filename.lower()

            with open(f"{filename}.txt",'w') as f:
                f.write(note)
                done = True
                speaker.say(f"I successfully created the note{filename}")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
                recognizer=speech_recognition.recognizer()
                speaker.say("I did not understand you! Lets try that again!")
                speaker.runAndWait()

def add_todo():

    global recognizer

    speaker.say("What do you want to add?")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with speech_recognition.Microphone()as mic:
                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio=recognizer.listen(mic)

                item=recognizer.recognize_google(audio)
                item=item.lower()

                todo_list.append(item)
                done=True

                speaker.say(f"I added{item}to the todo list!")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
                recognizer=speech_recognition.recognizer()
                speaker.say("I did not understand you! Lets try that again!")
                speaker.runAndWait()

def show_todo():
    speaker.say("The items on your todo list are as following")
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()

def quit():
    speaker.say("bye")
    speaker.runAndWait()
    sys.exit(0)

mappings={
    "greetings":hello,
    "create_note":create_note,
    "show_todo":show_todo,
    "exit":quit,
}

assistant=GenericAssistant('intents.json',intent_methods=mapping)
assistant.train_model()

while True:
    try:
        with speech_recognition.Microphone()as mic:
                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio=recognizer.listen(mic)

                message=recognizer.recognize_google(audio)
                message=message.lower()
                assistant.request(message)
            
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        speaker.say("I did not understand you! Let's try that again.")
        speaker.runAndWait()