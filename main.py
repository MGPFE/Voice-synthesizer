from email.message import EmailMessage
from configparser import ConfigParser
from generator import Menu_generator
from synthesizer import Synthesizer
from datetime import datetime
import traceback
import smtplib
import sys
import os


class Main:

    def __init__(self):
        
        if sys.platform == 'win32':
            self.what_os = 'CLS'
        elif sys.platform == 'linux':
            self.what_os = 'clear'

        self.config = ConfigParser()

        if not os.path.exists('config.ini'):
            self.config.add_section('BotConfig')
            self.config['BotConfig']['Name_by_text'] = 'True'
            self.config['BotConfig']['Speak_before_saving'] = 'True'
            self.config['BotConfig']['Accent'] = '0'
            self.config['BotConfig']['Rate'] = '125'
            self.config['BotConfig']['Volume'] = '1.0'

            with open('config.ini', 'w') as f:
                self.config.write(f)

        self.config.read('config.ini')

        self.naming = self.config.getboolean('BotConfig', 'Name_by_text')
        self.speak_before_saving = self.config.getboolean('BotConfig', 'Speak_before_saving')
        self.accent = self.config.getint('BotConfig', 'Accent')
        self.rate = self.config.getint('BotConfig', 'Rate')
        self.volume = self.config.getfloat('BotConfig', 'Volume')

        self.history = []

        # configure
        
        self.speaker = Synthesizer(self.accent, self.rate, self.volume)
        
        self.my_menu = Menu_generator(**{
            'name': 'Voice synthesizer',
            'version': '0.1',
            'side_bar': False,
            'number_options': True
        })


    def email_err(self):

        EMAIL_ADDRESS = 'mgpfe.dev@gmail.com'
        EMAIL_PASSWORD = 'ywoqlvcywcenzbju'

        with open('error.txt', 'w') as f:
            f.write(traceback.format_exc())

        msg = EmailMessage()
        msg['Subject'] = 'Error has occured!'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = 'dinozaurejeste@gmail.com'
        msg.set_content('Warning, an error has occured in your Twitterbot program!')

        with open('error.txt', 'rb') as f:
            file_data = f.read()
            file_name = f.name

        msg.add_attachment(file_data, maintype='textfile', subtype='txt', filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)


    def mainloop(self):

        while True:
            choice = self.my_menu.main_menu(**{
                'main': ['Say something', 'Save voice to file', 'Options'],
            })

            if choice == '1':
                
                while True:
                    os.system(self.what_os)

                    if len(self.history) != 0:
                        print('Previous words or sentences: ')
                        for thing in self.history:
                            print(f'- {thing}')
                        print('')

                    say = input('Input a word or a sentence (Type EXIT to go back): \n')
                    if say == 'EXIT':
                        break

                    if say not in self.history:
                        self.history.append(say)
                    
                    if len(self.history) > 5:
                        self.history.remove(f'{self.history[0]}')

                    self.speaker.speak(say)

            elif choice == '2':

                while True:
                    os.system(self.what_os)

                    say = input('Input a word or a sentence to save (Type EXIT to go back): \n')
                    if say == 'EXIT':
                        break

                    if self.naming:
                        say_title = say
                    else:
                        now = datetime.now()
                        current_time = now.strftime('%H_%M_%S')
                        # print(current_time)
                        say_title = f'Voice synthesizer speech ({current_time})'

                    self.speaker.save_to_file(say, say_title, self.speak_before_saving)

            elif choice == '3':
                
                while True:
                    choice2 = self.my_menu.sub_menu(**{
                        'sub_name': 'Options',
                        'sub_title': ['Speech options'],
                        'sub_content': [
                            f'Speak before saving to file ({self.speak_before_saving})',
                            f'Accent ({"English" if self.accent == 1 else "Polish"})',
                            f'Speech rate ({self.rate})',
                            f'Volume ({self.volume})',
                            f'Name file after speech ({self.naming})'
                        ]
                    })

                    if choice2 == '1':
                        os.system(self.what_os)
                        print('Speak before saving to file')
                        print('\n1. True')
                        print('2. False')
                        choice3 = input('\nChoice: ')

                        if choice3 == '1':
                            temp = True
                        
                        elif choice3 == '2':
                            temp = False

                        else:
                            temp = self.speak_before_saving

                        self.config.set('BotConfig', 'Speak_before_saving', f'{temp}')
                        with open('config.ini', 'w') as f:
                            self.config.write(f)
                        
                        self.speak_before_saving = temp


                    elif choice2 == '2':
                        os.system(self.what_os)
                        print('Accent')
                        print('\n1. Polish')
                        print('2. English')

                        choice4 = input('\nChoice: ')

                        if choice4 == '1':
                            temp = 0

                        elif choice4 == '2':
                            temp = 1

                        else:
                            temp = self.accent

                        self.config.set('BotConfig', 'Accent', f'{temp}')
                        with open('config.ini', 'w') as f:
                            self.config.write(f)

                        self.speaker.change_accent(temp)

                    elif choice2 == '3':
                        while True:
                            os.system(self.what_os)
                            print('Rate')
                            choice5 = input('Input an integer: ')

                            try:
                                inted_temp = int(choice5)
                            except ValueError:
                                print('\nIt\'s not an integer!')
                            else:
                                break

                        self.config.set('BotConfig', 'Rate', f'{inted_temp}')
                        with open('config.ini', 'w') as f:
                            self.config.write(f)

                        self.rate = inted_temp
                        self.speaker.change_rate(inted_temp)

                    elif choice2 == '4':

                        while True:
                            os.system(self.what_os)
                            print('Volume')
                            choice4 = input('Input a floating point value (0.0 - 1.0): ')

                            try:
                                floated_temp = float(choice4)
                                if floated_temp > 1.0:
                                    floated_temp = 1.0
                                elif floated_temp < 0:
                                    floated_temp = 0
                            except ValueError:
                                print('\nnot a valid value!')
                            else:
                                break

                        self.config.set('BotConfig', 'Volume', f'{floated_temp}')
                        with open('config.ini', 'w') as f:
                            self.config.write(f)

                        self.speaker.change_volume(floated_temp)

                    elif choice2 == '5':
                        os.system(self.what_os)
                        print('Name file after speech')
                        print('\n1. True')
                        print('2. False')

                        choice6 = input('Choice: ')

                        if choice6 == '1':
                            temp = True

                        elif choice6 == '2':
                            temp = False

                        else:
                            temp = self.naming

                        self.config.set('BotConfig', 'Name_by_text', f'{temp}')
                        with open('config.ini', 'w') as f:
                            self.config.write(f)

                        self.naming = temp

                    elif choice2 == '6':
                        break

            elif choice == '4':
                sys.exit()


if __name__ == '__main__':
    
    app = Main()
    try:
        app.mainloop()
    except Exception:
        app.email_err()
        input('\nError has occured!')
        sys.exit()