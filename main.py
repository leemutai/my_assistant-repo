import pyttsx3
import speech_recognition as sr
def take_commands():
    #making the use of recognizer and  the microphone
    #Method from speech recognition
    #a phrase is considerd complete
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening')
        #seconds of non-speaking audio before
        # a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)
    try:
        print("Recognizing")
        #for listening the command in indian english
        Query = r.recognize_google(audio,language='en-in')
        #for putting the query or the command that we give
        print("the query is printed='",Query,"'")
    except Exception as e:
        #this method is for handling the exception
        #and so that asistat can ask for telling
        # again the command
        print(e)
        print("say that again sir")
        return "None"
    return Query
def Speak(audio):
    #initial constructor of pyttsx3
    engine = pyttsx3.init()

    #getter and setter method
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(audio)
    engine.runAndWait()
    #driver code
    if __name__ == '__main__':
        while True:
            command = take_commands()
            if "exit" in command:
                Speak("Sure sir! as you wish bai")
                print("Sure sir! as you wish bai")

                break
            if "insta" in command:
                Speak("Best python page on instagram is pythonhub")
                print("Best python page on instagram is pythonhub")
            if "learn" in command:
                Speak("copyassignment website is best to learn python")
                print("copyassignment website is best to learn python")
            if "code" in command:
                Speak("You can get this code from copyassignment website")
                print("You can get this code from copyassignment website")



