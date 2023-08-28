'''módulo de menu'''


# ═║╔╗╚╝╠╣╦╩╬
# ─│┌┐└┘├┤┬┴┼
# ─║╓╖╙╜╟╢╥╨╫
from dataclasses import dataclass


def dye(string: str, color: str | None = None) -> str:
    '''tinge a string'''

    ansicolors: dict = {
        'black': '\33[0;30m',
        'red': '\33[0;31m',
        'green': '\33[0;32m',
        'yellow': '\33[0;33m',
        'blue': '\33[0;34m',
        'purple': '\33[0;35m',
        'cyan': '\33[0;36m',
        'white': '\33[0;37m',
        None: ''}

    return ansicolors[color] + string + '\033[0;0m'


@dataclass
class Option:
    '''rascunho da classe opção'''
    text: str|None = None  # texto da opção
    # func: function = function()
    keep: bool = False


class Menu:
    '''rascunho da classe menu'''

    def __init__(self, options: dict|None=None, options2: list|None=None, title: str='menu', start: int=1, invalid_selection_text: str|None=None) -> None:
        self.title: str = title
        self.options: dict = {} if options is None else options
        self.options2: list = list() if options2 is None else options2
        self.start: int = start
        self.invalid_selection_text: str = invalid_selection_text if invalid_selection_text else ''

        if self.is_empty():
            self.options.update({'↩': '∅'})
            self.options2.append(('↩', '∅', False))

        self.longest_string_len: int = len(max(list(self.options.keys(),), key=len)) + 5

        if len(self.title) > self.longest_string_len:
            self.longest_string_len = len(self.title)

    def __repr__(self) -> str:
        string = f'Menu(title={self.title}, '
        string += f'options={self.options}, '
        string += f'options2={self.options2}, '
        string += f'start={self.start}, '
        string += f'longest_string_len={self.longest_string_len}, '
        string += f'invalid_selection_text={self.invalid_selection_text})'
        return string

    def show_options(self) -> None:
        '''mostra opcões'''
        width = self.longest_string_len
        print(f'┌{"":─^{width}}┐',
              f'│{self.title: ^{width}}│',
              f'├{"":─^{width}}┤', sep='\n')

        for index, option in enumerate(self.options, start=self.start):
            print(f'│{f" {index: 2} {option} ":<{width}}│')

        print(f'└{"":─^{width}}┘')

    def get_selection(self) -> int:
        '''lê seleção'''

        selection = input('  ~> ')

        if selection.isdigit():
            selection = int(selection)
            if self.start <= selection < self.start + len(self.options):
                return selection
            
        string = f'{f"{self.invalid_selection_text}": >{self.longest_string_len}}'
        print(dye(string, 'red'))
        return self.get_selection()

    def run(self) -> bool:
        '''roda menu'''

        self.show_options()

        if self.is_empty():
            return False

        selection = self.get_selection()

        # saída
        if selection == self.start + len(self.options) - 1:
            string = f'{list(self.options.items())[selection-self.start][1]: >{self.longest_string_len}}'
            print(dye(string, 'yellow'))
            return False

        # chama uma função
        keep = list(self.options.items())[selection-self.start][1]()
        return keep

    def run_in_loop(self) -> None:
        '''roda menu em loop'''

        while self.run():
            pass

    def run_recursively(self) -> None:
        '''roda menu recursivamente'''

        self.show_options()

        if self.is_empty():
            return None

        selection = self.get_selection()

        # saída
        if selection == self.start + len(self.options) - 1:
            string = f'{list(self.options.items())[selection-self.start][1]: >{self.longest_string_len}}'
            print(dye(string, 'yellow'))
            return None

        # chama uma função
        list(self.options.items())[selection-self.start][1]()
        return self.run_recursively()

    def is_empty(self) -> bool:
        return (bool(self.options) is False) and (bool(self.options2) is False)
    
    def show_options2(self) -> None:
        width = self.longest_string_len
        print(f'┌{"":─^{width}}┐',
              f'│{self.title: ^{width}}│',
              f'├{"":─^{width}}┤', sep='\n')

        for index, (text, func, keep) in enumerate(self.options2, start=self.start):
            print(f'│{f" {index: 2} {text} ":<{width}}│')

        print(f'└{"":─^{width}}┘')
    
    def run2(self) -> bool:

        self.show_options2()

        sel = self.get_selection()

        # saída
        if sel == self.start + len(self.options2) - 1:
            string = f'{self.options2[sel-self.start][1]: >{self.longest_string_len}}'
            print(string)
            print(dye(
                string, 'yellow'))
            print(self.options2[sel-self.start][2])
            
            return False

        # chama uma função
        keep = self.options2[sel-self.start][1]()
        return keep
    
