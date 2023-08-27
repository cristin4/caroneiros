'''módulo de menu'''


# ═║╔╗╚╝╠╣╦╩╬
# ─│┌┐└┘├┤┬┴┼
# ─║╓╖╙╜╟╢╥╨╫


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


class Menu:
    '''rascunho da classe menu'''

    def __init__(self, options: dict|None=None, title: str='menu', start: int=1, invalid_selection: str|None=None) -> None:
        self.title: str = title
        self.options: dict = {} if options is None else options
        self.start: int = start
        self.empty_menu: bool = bool(self.options) is False
        self.invalid_selection: str = invalid_selection if invalid_selection else ''

        if self.empty_menu:
            self.options.update({'↩': '∅'})
            self.empty_menu = False

        self.longest_string_len: int = len(self.title) if self.empty_menu else len(
            max(list(self.options.keys()), key=len)) + 5

    def __repr__(self) -> str:
        string = f'Menu(title={self.title}, '
        string += f'options={self.options}, '
        string += f'start={self.start}, '
        string += f'empty_menu={self.empty_menu}, '
        string += f'longest_string_len={self.longest_string_len})'
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

    def input_selection(self) -> int:
        '''lê seleção'''

        selection = input('  ~> ')

        if selection.isdigit():
            selection = int(selection)
            if self.start <= selection < self.start + len(self.options):
                return selection

        print(
            dye(f'{f"{self.invalid_selection}": >{self.longest_string_len}}', 'red'))
        return self.input_selection()

    def run(self) -> bool:
        '''roda menu'''

        self.show_options()
        if self.empty_menu:
            return False

        selection = self.input_selection()

        # saída
        if selection == self.start + len(self.options) - 1:
            print(dye(
                    f'{list(self.options.items())[selection-self.start][1]: >{self.longest_string_len}}', 'yellow'))
            return False

        # chama uma função
        list(self.options.items())[selection-self.start][1]()
        return True

    def run_in_loop(self) -> None:
        '''roda menu em loop'''

        while self.run():
            pass

    def run_recursively(self) -> None:
        '''roda menu recursivamente'''

        self.show_options()

        if self.empty_menu:
            return None

        selection = self.input_selection()

        # saída
        if selection == self.start + len(self.options) - 1:
            print(dye(
                    f'{list(self.options.items())[selection-self.start][1]: >{self.longest_string_len}}', 'yellow'))
            return None

        # chama uma função
        list(self.options.items())[selection-self.start][1]()
        return self.run_recursively()
