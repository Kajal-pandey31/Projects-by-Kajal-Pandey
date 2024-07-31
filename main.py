import speech_recognition as sr
import os
import webbrowser
import win32com.client
import openai
from config import apikey
import datetime

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Kajal: {query}\n Jarvis: "

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    speaker.speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

    # with open(f"Openai/prompt- {random.randint(1,2343434356  )}","w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)
def ai(prompt):
    openai.api_key = apikey

    text= f"OpenAI response for prompt: {prompt} \n *****************\n\n"

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    #with open(f"Openai/prompt- {random.randint(1,2343434356  )}","w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
       f.write(text)
speaker = win32com.client.Dispatch("SAPI.SpVoice")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =  1
        audio = r.listen(source)

        print("recognizing")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said:{query}")
        return query
        #except Exception as e:
            #return "Some error occured . Sorry from Jarvis"
if __name__=='__main__':
    print("Hello I am Your Smart Chatbot, How can I help You Miss Kajal...")
    speaker.speak("Hello I am Your Smart Chatbot, How can I help You Miss Kajal...")

    while 1 :
    #print("Enter the word you want to speak by computer")
    #s= input()
    #speaker.speak(s)
        while True:
            print("listening...")
            take = takeCommand()



            sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                     ["google", "https://www.google.com"], ]
            for site in sites:
                if f"Open {site[0]}".lower() in take.lower():
                    speaker.speak(f"Opening {site[0]} Ma'am")
                    webbrowser.open(site[1])
            if "open music".lower() in take.lower():
                musicPath = "https://youtu.be/eJi72KMWOC0?si=3QrbqvgrPh6ALvZV"
                os.system(f"start {musicPath}")
            elif "the time" in take:
                hour = datetime.datetime.now().strftime("%H")
                min = datetime.datetime.now().strftime("%M")
                speaker.speak(f"Sir time is {hour} baj kay {min} minutes")
            elif "Open Camera".lower() in take.lower():
                os.system(f"start microsoft.windows.camera:")
            elif "Using Artificial Intelligence".lower() in take.lower():
                ai(prompt=take)
            else:
                chat(take)