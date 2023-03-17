from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys
import os
import webbrowser


def speak(audio):

    speaker = tts.int()
    engine.say(audio)
    engine.runAndWait()



def tellDay():
    
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1
    
    #this line tells us about the number
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak.say("The day is " + day_of_the_week)
        speaker.runAndWait()
    
def tellTime():
    
    # This method will give the time
    time = str(datetime.datetime.now())
    
    # the time will be displayed like
    # this "2020-06-05 17:50:14.582630"
    #nd then after slicing we can get time
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak.say("The time is sir" + hour + "Hours and" + min + "Minutes")
    speaker.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning  !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon  !")  
  
    else:
        speak("Good Evening  !") 
  
    assname =("Prime 97")
    speak.say("I am your Assistant")
    speak(assname)
    speaker.runAndWait()
     

 
def username():
    speak("What should i call you ")
    uname = takeCommand()
    speak.say("Welcome Mr.")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    
    print("######################".center(columns))
    print("###*** PRIME 97 ***###".center(columns))
    print("Welcome ", uname.center(columns))
    print("###*** PRIME 97 ***###".center(columns))
    print("######################".center(columns))
     
    speak.say("How can i Help you ")
    speaker.runAndWait()

def main():
    greeting()
    current_time, current_day = get_time()
    speak.say(f"The current time is {current_time} and today is {current_day}.")
    speaker.runAndWait()

def take_Command():
    recognizer = speech_recognition.recognizer()
    mic = sr.Microphone()
    with speech_recognition.Microphone()as mic:
        print('Listening....')

        recognizer.adjust_for_ambient_noise(mic,duration=0.2)
        audio=recognizer.listen(mic)
        try:
                print("Recognizing...")
                Query = r.recognize_google(audio, language='en-in')
                print("the command is printed=", Query)

        except speech_recognition.UnknownValueError:
                recognizer=speech_recognition.recognizer()
                speaker.say("I did not understand you! Lets try that again!")
                speaker.runAndWait()
                return "Free"
                return Query

if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    greeting()
    main()
    tellDay()
    tellTime()
    clear()
    wishMe()
    username()


    while True:
         
        query = takeCommand().lower()


    if 'wikipedia' in query:
            speak.say('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak.say("According to Wikipedia")
            print(results)
            speak(results)
            speaker.runAndWait()
 
    elif 'open youtube' in query:
            speak.say("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
            speaker.runAndWait()

    elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow dot Happy coding")
            webbrowser.open("stackoverflow.com")
            speaker.runAndWait

    elif 'open my github' in query:
            speak.say("Opening your github")
            webbrowser.open("github.com")
            speaker.runAndWait()

    elif 'play chess' in query:
            speak.say("opening chess")
            appli = r"C:\\Program Files\\Microsoft Games\\Chess\\Chess.exe"
            os.startfile(appli)
            speaker.runAndWait()

    elif 'play free cells' in query:
            speak.say("opening free cells")
            appli = r"C:\\Program Files\\Microsoft Games\\FreeCell\\FreeCell.exe"
            os.startfile(appli)
            speaker.runAndWait()

    elif 'play hearts' in query:
            speak.say("Opening hearts game")
            appli = r"C:\\Program Files\\Microsoft Games\\ Hearts\\Hearts.exe"
            os.startfile(appli)
            speaker.runAndWait()

    elif 'play china' in query:
            speaker.say("Mahjong")
            appli = r"C:\\Program Files\\Microsoft Games\\Mahjong\\Mahjong.exe"
            os.startfile(appli)
            speaker.runAndWait()

    elif 'play solitaire' in query:
            speak.say("opening solitaire")
            appli = r"C:\\Program Files\\Microsoft Games\\Solitaire\\solitaire.exe"
            os.startfile(appli)
            speaker.runAndWait()

    elif 'play land mines' in query:
            speak.say("opening Mine sweeper")
            appli = r"C:\\Program Files\\Microsoft Games\\Minesweeper\\MineSweeper.exe"
            os.startfile(appli)
            speaker.runAndWait()

def play_music():
    music_dir = "C:\\Users\\Ik@r!s\\My Music"
    songs = os.listdir(music_dir)
    song = random.choice(songs)
    os.startfile(os.path.join(music_dir, song))

def play_video():
    video_dir = "C:\\Users\\YourUsername\\Videos"
    videos = os.listdir(video_dir)
    video = random.choice(videos)
    os.startfile(os.path.join(video_dir, video))

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

            with open(f"{filename}.tx",'w') as f:
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
                item=note.lower()

                todo_list.append(item)
                done=True

                speaker.say(f"I added{item}to the todo list!")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
                recognizer=speech_recognition.recognizer()
                speaker.say("I did not understand you! Lets try that again!")
                speaker.runAndWait()

def Show_todo():
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
    "create_note":add_todo,
    "show_todo":show_todo,
    "exit":quit,
}

assiStant=GenericAssistant(intents.json,intent_methods=mapping)
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