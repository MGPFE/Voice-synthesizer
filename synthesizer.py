import pyttsx3

class Synthesizer:
    def __init__(self, accent, rate, volume):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[accent].id)
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

    def speak(self, say):
        self.engine.say(f'{say}')
        self.engine.runAndWait()

    def save_to_file(self, say, say_title, say_it):
        if say_it:
            self.engine.say(f'{say}')
        self.engine.save_to_file(f'{say}', f'{say_title}.mp3')
        self.engine.runAndWait()

    def change_accent(self, tmp):
        self.engine.setProperty('voice', self.voices[tmp].id)
        self.engine.say(f'{"English" if tmp == 1 else "Polski"}')
        self.engine.runAndWait()

    def change_rate(self, rt):
        self.engine.setProperty('rate', rt)
        self.engine.say(f'{rt}')
        self.engine.runAndWait()

    def change_volume(self, vl):
        self.engine.setProperty('volume', vl)
        self.engine.say(f'{vl}')
        self.engine.runAndWait()