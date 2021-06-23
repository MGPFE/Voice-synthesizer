from colorama import Fore, Style
from math import ceil
import os
import sys


class Menu_generator:

    def __init__(self, **kwargs):
        
        if sys.platform == 'win32':
            self.what_os = 'CLS'
        elif sys.platform == 'linux':
            self.what_os = 'clear'

        self.version = 'Default version' if kwargs.get('version') is None else kwargs.get('version')
        self.name = 'Default name' if kwargs.get('name') is None else kwargs.get('name')
        self.side_bar = True if kwargs.get('side_bar') is None else kwargs.get('side_bar')
        self.first_party = False if kwargs.get('first_party') is None else kwargs.get('first_party') 
        self.WARNING_FLAG = True if kwargs.get('warning_flag') is None else kwargs.get('warning_flag')
        self.number_options = True if kwargs.get('number_options') is None else kwargs.get('number_options')
        # self.colored = False if kwargs.get('colored') is None else kwargs.get('colored')

    
    def main_menu(self, **kwargs):

        main = kwargs.get('main')
        main_len = len(main) if kwargs.get('main') is not None else None
        side_tag = kwargs.get('side_tag')
        side = kwargs.get('side')
        side_len = len(side) if self.side_bar else 0
        side_content = kwargs.get('side_content')
        # side_content_len = len(side_content)
        first_party = kwargs.get('first_party')
        # color = kwargs.get('color')

        # ZMIENNE DO POCIECIA LISTY
        slicer = main_len
        list_of_lists = []
        a = ceil(side_len / main_len) if self.side_bar else None
        inted_a = int(a) if a is not None else main_len

        # MODYFIKACJA BOCZNEGO MENU
        if self.side_bar:
            for i in range(side_len):
                side[i] = f'|{side[i]}: {side_content[i]}'

        # NUMEROWANIE OPCJI
        if self.number_options:
            for i in range(main_len):
                main[i] = f'|{i + 1}. {main[i]}'

        list_of_lists.append(main)

        # if side_len == side_content_len:
        #     contents = {}
        #     for num in range(side_len):
        #         contents[side[num]] = side_content[num]
        # else:
        #     raise Exception("Number of side titles doesn't match contents")

        os.system(self.what_os)
        #print(kwargs)

        if side_len > (main_len * 2) and self.WARNING_FLAG:
            print(f'{Fore.YELLOW}WARNING, MENU SUPPORTS UP TO 2X MORE SIDE BARS THAN MAIN OPTIONS, SOME SIDE BARS MAY NOT BE DISPLAYED!{Style.RESET_ALL}')

        # GORA MENU
        print(f'|{self.name} {self.version}')

        if self.first_party:
            print(f"|{first_party.get('connection')}")

        if self.side_bar:
            print('', end='\t\t\t ')
            print(f'|{side_tag}')
        
        else:
            print('')
            


        # DZIELENIE NA LISTE LIST
        if self.side_bar:
            for i in range(inted_a):

                # if slicer == main_len:
                if i == 0:
                    list_of_lists.append(side[:slicer])
                    slicer += main_len

                elif slicer >= main_len:
                    list_of_lists.append(side[(slicer - main_len):slicer])
                    slicer += side_len

        # WYPELNIANIE PUSTYCH POL ZEBY LISTY MIALY PO TYLE SAMO ELEMENTOW
        for index, l in enumerate(list_of_lists):
            if len(l) != main_len and index != 0:
                for _ in range(main_len - int(len(l))):
                    l.append('')

        if self.side_bar:
            row_format = '{:25.25}' * len(list_of_lists)
            for v in zip(*list_of_lists):
                print(row_format.format(*v))
        else:
            for option in main:
                print(option)

        # for index, arg in enumerate(kwargs.get('main'), 1):
        #     if self.side_bar:

        #         print(f'{index}. {arg}', end='\t\t')
        #         if len(kwargs.get('side')) > len(kwargs.get('main')):

        #             if not CACHED:

        #                 slicer = len(kwargs.get('main'))
        #                 list_of_lists = []
        #                 a = math.ceil(len(kwargs.get('side')) / len(kwargs.get('main')))
        #                 inted_a = int(a)
        #                 initial_val = len(kwargs.get('side'))

        #                 for _ in range(inted_a):

        #                     if slicer == len(kwargs.get('main')):
        #                         list_of_lists.append(kwargs.get('side')[:slicer])
        #                         slicer += len(kwargs.get('main'))

        #                     elif slicer >= initial_val:
        #                         list_of_lists.append(kwargs.get('side')[(slicer - len(kwargs.get('main'))):slicer])
        #                         slicer += len(kwargs.get('side'))
                    
        #             CACHED = True

        #             try:
        #                 print(f"|{list_of_lists[0][index-1]}: {kwargs.get('side_content')[index - 1]}", end='\t')
        #                 print(f"|{list_of_lists[1][index-1]}: {kwargs.get('side_content')[(index - 1) + len(kwargs.get('main'))]}")

        #             except IndexError:
        #                 print('')

        #         else:
        #             print(f"|{kwargs.get('side')[index-1]}")

        #     else:
        #         print(f'{index}. {arg}')

        print(f'\n|{main_len + 1}. Exit') if self.number_options else print('\nExit')
        choice = input(f'\nChoice: ')
        return choice


    def sub_menu(self, **kwargs):

        sub_name = kwargs.get('sub_name')
        sub_title = kwargs.get('sub_title')
        sub_content = kwargs.get('sub_content')
        sub_content_len = len(sub_content)

        sub_titles = []
        for title in sub_title:
            sub_titles.append([f'|{title}'])

        # ZMIENNE DO POCIECIA LIST
        list_of_lists = []
        slicer = 6
        a = ceil(sub_content_len / 6)
        inted_a = int(a)

        # NUMEROWANIE OPCJI
        if self.number_options:
            for i in range(sub_content_len):
                sub_content[i] = f'{i + 1}. {sub_content[i]}'

        os.system(self.what_os)
        print(sub_name)
        print('')
        if sub_title:
            # print('|Default title 1', end='\t\t') if not sub_title else print(f"|{sub_title[0]}", end='\t\t')
            # print('') if not len(sub_title) == 2 else print(f"|{sub_title[(len(sub_title) - 1)]}")
            title_format = '{:<20}' * len(sub_titles)
            for v in zip(*sub_titles):
                print(title_format.format(*v))
            print('')

        # CIECIE LIST - TWORZENIE LISTY LIST
        for i in range(inted_a):
            # if (slicer + 2) == sub_content_len:
            if i == 0:
                list_of_lists.append(sub_content[:slicer])
                slicer += sub_content_len

            elif slicer >= sub_content_len:
                list_of_lists.append(sub_content[(slicer - sub_content_len):slicer])
                slicer += sub_content_len

        # WYPELNIANIE PUSTYCH POL W LISTACH ZEBY KAZDA MIALA TYLE SAMO ELEMENTOW
        if sub_content_len > 6:
            for l in list_of_lists:
                if len(l) != 6:
                    for _ in range(6 - int(len(l))):
                        l.append('')

        row_format = '{:<20}' * len(list_of_lists)
        for v in zip(*list_of_lists):
            print(row_format.format(*v))

        # for index, arg in enumerate(list_of_lists[0], 1):
        #     if sub_content_len > 6:
        #         try:
        #             if not TEST_FLAG:
        #                 print(f"{index}. {arg}", end='\t\t')
        #                 print(f"{(index - 2) + sub_content_len}. {list_of_lists[1][index-1]}")
        #             else:
        #                 print(f"{index}. {arg}")
        #         except IndexError:
        #             if (sub_content_len % 2 == 0):
        #                 TEST_FLAG = True
        #                 print('')
        #                 pass
        #             else:
        #                 print('')
        #                 pass
            
        #     else:
        #         print(f"{index}. {sub_content[index - 1]}")

        print(f"\n{sub_content_len + 1}. Go back") if self.number_options else print('\nGo back')
        choice = input('\nChoice: ')
        return choice