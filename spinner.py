from threading import Thread
from sys import stdout
from time import sleep

def additional(text, style, l=''):
    if style in DOUBLE_BS:
        l += '\b'
    for x in range(len(text)):
        l += '\b'
    return l

DOUBLE_BS = ['pie', 'cube', 'arrows', 'lines', 'tringle', 'squares', 'dots']

styles = {
    'default': ['\\', '|', '/', '-'],
    'ballon': ['.', 'o', 'O', '@', '*'],
    'arrows': ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙'],
    'cube': ['▖', '▘', '▝', '▗'],
    'lines': ['┤', '┘', '┴', '└', '├', '┌', '┬', '┐'],
    'tringle': ['◢', '◣', '◤', '◥'],
    'squares': ['◰', '◳', '◲', '◱'],
    'pie': ['◴', '◷', '◶', '◵'],
    'circle': ['◐', '◓', '◑', '◒'],
    'dots': ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷'],
    'v': ['<', 'V', '>', '^'],
    'x': ['+', 'X']
}

COLIST = {
    'black': '\33[30m',
    'red': '\33[31m',
    'green': '\33[32m',
    'yellow': '\33[33m',
    'blue': '\33[34m',
    'violet': '\33[35m',
    'beige': '\33[36m',
    'white': '\33[37m',
    'close': '\033[0m'
}

def CColor(text, color):
    return f'{COLIST[color]}{text}{COLIST["close"]}'

class Spinner:
    def __init__(self, style:str):
        self.style = style
        self.chars = styles[style]
        self.quit = False

    def start(self, progress=None, args:list=None, text:str='', times:int=None, wait:float=.2, color:str=None):
        if not progress:
            if not times:
                while True:
                    if self.quit:
                        break
                    for x in self.chars:
                        if color != None:
                            stdout.write(CColor(f'{additional(text+x, self.style)}{text}{x}', color))
                        else:
                            stdout.write(f'{additional(text+x, self.style)}{text}{x}')
                        stdout.flush()
                        sleep(wait)
            else:
                for x in range(times):
                    if self.quit:
                        break
                    for x in self.chars:
                        if color != None:
                            stdout.write(CColor(f'{additional(text+x, self.style)}{text}{x}', color))
                        else:
                            stdout.write(f'{additional(text+x, self.style)}{text}{x}')
                        stdout.flush()
                        sleep(wait)
        else:
            if args != None:
                t = Thread(target=progress, args=args)
            else:
                t = Thread(target=progress)
            t.start()
            while True:
                if self.quit:
                    break
                for x in self.chars:
                    if t.isAlive():
                        if color != None:
                            stdout.write(CColor(f'{additional(text+x, self.style)}{text}{x}', color))
                        else:
                            stdout.write(f'{additional(text+x, self.style)}{text}{x}')
                        stdout.flush()
                        sleep(wait)
                    else:
                        self.stop()
    
    def stop(self):
        self.quit = True