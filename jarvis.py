import wolframalpha
#u can get ur AppId from wolframalpha.com/ just make an account there
client = wolframalpha.Client("AppId")
import PySimpleGUI as sg
import wikipedia
import pyttsx3


#THEME OF THE WINDOW
sg.theme("DarkBrown4")
layout = [[sg.Text("YOUR COMMAND : "),sg.InputText(),sg.Button('Execute'),sg.Button('Close')]]
window = sg.Window("JARVIS",layout)

while True:
    event, values = window.read()
    if event in (None,"Close"):
        break
    try:
        #TRY WOLFRAME RESULTS
        res = client.query(values[0])
        wolfram_res = next(res.results).text
        sg.PopupNonBlocking(wolfram_res)
        engine = pyttsx3.init()
        engine.say(wolfram_res)
        engine.runAndWait()
    except:
        #TRY WIKIPEDIA RESULTS
        wiki_res = wikipedia.summary(values[0], sentences=2)
        sg.PopupNonBlocking(wiki_res)
        engine = pyttsx3.init()
        engine.say(wiki_res)
        engine.runAndWait()

    print(values[0])

window.close()
