'''módulo de menu'''
# ═║╔╗╚╝╠╣╦╩╬
# ─│┌┐└┘├┤┬┴┼
# ─║╓╖╙╜╟╢╥╨╫


def red(string):
    '''colore a string'''
    return '\033[31m' + string + '\033[0;0m'

class Menu:
    '''rascunho da classe menu'''

    def __init__(self, header='menu', options=None, start=1):
        self.header = header
        self.options = options
        self.start = start
        self.longest_string_len = len(self.header)
        self.void_menu = self.options is None

        if not self.void_menu:
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

        if self.void_menu:
            print(f'│{"∅":^{width}}│')
            print(f'└{"":═^{width}}┘')
        else:
            for index, option in enumerate(self.options, start=self.start):
                print(f'│{f" {index: 2} {option} ":<{width}}│')

            print(f'└{"":─^{width}}┘')

    def run(self):
        '''roda menu'''
        self.show()

        if self.void_menu:
            return

        sel = input('  ~> ')

        if sel.isdigit():
            sel = int(sel)

            # Encerra o loop
            if sel == self.start + len(self.options)-1:
                print(red(
                    f'{list(self.options.items())[sel-self.start][1]: >{self.longest_string_len}}'))
                return

            # Chama uma função do menu
            if self.start <= sel < self.start + len(self.options):
                list(self.options.items())[sel-self.start][1]()
                self.run()
                return

        print(
            red(f'{"Seleção inválida!": >{self.longest_string_len}}'))
        self.run()