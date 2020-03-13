import random
import sys
import colorama


class Colors:
    listColor = ['\033[1;35;48m',
            '\033[1;36;48m',
            '\033[1;37;48m',
            '\033[1;34;48m',
            '\033[1;32;48m',
            '\033[1;33;48m',
            '\033[1;31;48m',
            '\033[1;30;48m'
            ]
    color = None

    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']

    def __init__(self):
        self.format = str(random.choice(self.listColor))
        
    def defineColor(self,color):
        if isinstance(color,colorama.Fore):
            self.color = color
    
    def print_color(self,text):
        if self.color is None :
            print(self.format+text)
        else :
            self.print_select_color(text,self.color)


    def print_random_color(self,text):
        codes = vars(colorama.Fore)
        colors = [codes[color] for color in codes if color not in self.bad_colors]
        colored_chars = [random.choice(colors) + char for char in text]
        print(''.join(colored_chars))
    
    def print_select_color(self,text,color):
        print(color+text)


