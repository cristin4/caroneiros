"""módulo de menu"""


# ═║╔╗╚╝╠╣╦╩╬
# ─│┌┐└┘├┤┬┴┼
# ─║╓╖╙╜╟╢╥╨╫

from dataclasses import dataclass

@dataclass
class Option:
    """rascunho da classe opção"""

    text: str | None = None  # texto da opção
    # func: function = function()
    keep: bool = False



class Menu:
    """rascunho da classe menu"""

    def __init__(
        self,
        options: list | None = None,
        title: str = "menu",
        start: int = 1,
        invalid_selection_text: str | None = None,
    ) -> None:
        self.title: str = title
        self.options: list = list() if options is None else options
        self.start: int = start
        self.invalid_selection_text: str = (
            invalid_selection_text if invalid_selection_text else "")


        if self.is_empty():
            self.options.append(("↩", "∅"))

        # self.longest_string_len: int
        self.update_longest_string_len()
        pass

    def update_longest_string_len(self, index_offset: int = 5) -> None:
        strings = list()
        for text, func, *args in self.options:
            strings.append(text)

        self.longest_string_len = len(max(strings, key=len)) + index_offset
        if len(self.title) > self.longest_string_len:
            self.longest_string_len = len(self.title)

    def __repr__(self) -> str:
        string = f"Menu(title={self.title}, "
        string += f"options={self.options}, "
        string += f"start={self.start}, "
        string += f"longest_string_len={self.longest_string_len}, "
        string += f"invalid_selection_text={self.invalid_selection_text})"
        return string

    def get_selection(self) -> int:
        """lê seleção"""

        selection = input("  ~> ")

        if selection.isdigit():
            selection = int(selection)
            if self.start <= selection < self.start + len(self.options):
                return selection

        string = f'{f"{self.invalid_selection_text}": >{self.longest_string_len}}'
        print(dye(string, "red"))
        return self.get_selection()

    def is_empty(self) -> bool:
        return bool(self.options) is False

    def show_options(self) -> None:
        width = self.longest_string_len
        print(
            f'┌{"":─^{width}}┐',
            f"│{self.title: ^{width}}│",
            f'├{"":─^{width}}┤',
            sep="\n",
        )

        for index, (text, func, *args) in enumerate(self.options, start=self.start):
            print(f'│{f" {index: 2} {text} ":<{width}}│')

        print(f'└{"":─^{width}}┘')


    def run_once(self) -> bool | None:
        self.show_options()

        sel = self.get_selection()

        if sel == self.start + len(self.options) - 1:  # saída
            string = f"{self.options[sel-self.start][1]: >{self.longest_string_len}}"
            print(dye(string, "yellow"))
            return None
        else:  # chama uma função
            return self.options[sel - self.start][1](self.options[sel - self.start][2])

    def run_in_loop(self) -> None:
        """roda em loop"""
        while self.run_once():
            pass


    def run_recursively(self) -> bool:
        """roda menu recursivamente"""

        self.show_options()

        sel = self.get_selection()
        
        # saída
        if sel == self.start + len(self.options) - 1:
            string = f"{self.options[sel-self.start][1]: >{self.longest_string_len}}"
            print(dye(string, "yellow"))
            return False
        # chama uma função
        if self.options[sel - self.start][1]() is None:
            return self.run_recursively()
        return False
    
    @staticmethod
    def confirm(question: str = '', yes: str | None = 'y', ) -> bool:
        answer = input(question +
                       dye(f" [{yes}]", "red") + "\n  ~> ")
        return answer == yes
    


def dye(string: str, color: str | None = None) -> str:
    """tinge a string"""

    ansicolors: dict = {
        "black": "\33[0;30m",
        "red": "\33[0;31m",
        "green": "\33[0;32m",
        "yellow": "\33[0;33m",
        "blue": "\33[0;34m",
        "purple": "\33[0;35m",
        "cyan": "\33[0;36m",
        "white": "\33[0;37m",
        None: "",
    }

    return ansicolors[color] + string + "\033[0;0m"
