'''módulo de menu'''

# ═║╔╗╚╝╠╣╦╩╬
# ─│┌┐└┘├┤┬┴┼
# ─║╓╖╙╜╟╢╥╨╫


def dye(string, color=None):
    '''colore a string'''

    ansicolors = {
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

    def __init__(self, header='menu', options={}, start=1):
        self.header = header
        self.options: dict = options
        self.start = start
        self.longest_string_len = len(self.header)
        self.is_a_void_menu = self.options is None

        if not self.is_a_void_menu:
            self.longest_string_len = len(
                max(list(self.options.keys()), key=len))
            if len(self.header) > self.longest_string_len:
                self.longest_string_len = len(self.header)
            self.longest_string_len += 5

    def show(self):
        '''mostra opcões'''
        width = self.longest_string_len
        print(f'┌{"":─^{width}}┐',
              f'│{self.header: ^{width}}│',
              f'├{"":─^{width}}┤', sep='\n')

        if self.is_a_void_menu:
            print(f'│{"∅":^{width}}│')
            print(f'└{"":═^{width}}┘')
        else:
            for index, option in enumerate(self.options, start=self.start):
                print(f'│{f" {index: 2} {option} ":<{width}}│')

            print(f'└{"":─^{width}}┘')

    def input_selection(self) -> int:
        '''¿?'''
        selection = input('  ~> ')

        if selection.isdigit():
            selection = int(selection)
            if self.start <= selection < self.start + len(self.options):
                return selection

        print(dye(f'{"Seleção inválida!": >{self.longest_string_len}}', 'red'))
        return self.input_selection()

    def run(self):
        '''¿?'''
        self.show()
        if self.is_a_void_menu:
            return False

        selection = self.input_selection()

        # saída
        if selection == self.start + len(self.options)-1:
            print(dye(
                f'{list(self.options.items())[selection-self.start][1]: >{self.longest_string_len}}', 'red'))
            return False

        # chama uma função
        list(self.options.items())[selection-self.start][1]()
        return True

    def run_in_loop(self):
        '''¿?'''
        while self.run():
            pass

    def test(self):
        '''¿?'''
        self.show()
        if self.is_a_void_menu:
            return None

        selection = self.input_selection()

        # saída
        if selection == self.start + len(self.options)-1:
            print(dye(
                f'{list(self.options.items())[selection-self.start][1]: >{self.longest_string_len}}', 'red'))
            return None

        # chama uma função
        list(self.options.items())[selection-self.start][1]()
        return self.test()
