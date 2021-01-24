import pyttsx3, PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('kivy.pdf', 'rb'))

speaker = pyttsx3.init()
rate = speaker.getProperty('rate')   
print(rate)


speaker.setProperty('rate', 125)

voices = speaker.getProperty('voices')
print(voices)


#changing index, changes voices, 0 for male
speaker.setProperty('voice', voices[0].id)
#changing index, changes voices, 1 for female
#speaker.setProperty('voice', voices[1].id)
volume = speaker.getProperty('volume')
print(volume)
speaker.setProperty('volume',1.0)
##engine.save_to_file(text, 'audio.mp3')
##engine.runAndWait()

for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()
