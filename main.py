from tkinter import *
import pandas as pd 
from pydub import AudioSegment
from pydub.playback import play
import time

def converter():
    df = pd.read_csv('morse_data.csv')
    morse_dict = dict(zip(df.Letter, df.Morse))
    text = text_input.get("1.0", "end")
    codes = ''
    for char in text.upper():
        if char in morse_dict:
            codes += morse_dict[char]
        elif char == ' ':
            codes += ' '
    translation.delete('1.0', 'end')
    translation.insert(INSERT, codes)

def sound_gen():
    codes = translation.get("1.0", "end")
    period = AudioSegment.from_wav('period.wav')
    hyphen = AudioSegment.from_wav('hyphen.wav')
    for char in codes:
        if '.' == char:
            play(period)
        elif '-' == char:
            play(hyphen)
        else:
            time.sleep(1)


window = Tk()
window.title('Morse Code Converter')
window.config(padx=40, pady=40)

text_label = Label(text='Type texts below ', fg="black", font=('Helvetica', 18, 'bold'))
text_label.grid(column=1, row=0, columnspan=2)

text_input = Text(height=10, font=("Courier", 12))
text_input.focus()
text_input.grid(column=1, row=1, columnspan=2)

convert_button = Button(text='Convert the text', command=converter)
convert_button.grid(column=1, row=2,columnspan=2)

sound_button = Button(text='Sound', command=sound_gen)
sound_button.grid(column=2, row=2,columnspan=2)

translation = Text(fg="black", borderwidth=2, relief="ridge",height=10)
translation.grid(column=1, row=3, columnspan=2)

window.mainloop()

