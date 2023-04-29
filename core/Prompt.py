import tiktoken
import Logger as Logger

ENCODING_NAME = 'cl100k_base'

class Prompt:

    def __init__(self, original='') -> None:
        self.original = original
        self.process_phrase(original)
        self.final = self.original
        self.constraints = []

    def get_prompt(self) -> str:
        return self.final
    
    def set_prompt(self, original:str) -> None:
        self.original = original
        self.process_phrase(original)

    def calculate_tokens(self) -> int:
        encoding = tiktoken.get_encoding(ENCODING_NAME)
        num_tokens = len(encoding.encode(self.final))
        return num_tokens

    def minimalize(self) -> None:
        pass

    def add_constraints(self, constraints:str) -> None:
        self.process_phrase(constraints)
        if len(constraints) > 0:
            self.final += f"{constraints}"
            self.constraints.append(constraints)    

    def add_constraints(self, constraints:list) -> None:
        for constraint in constraints:
            self.add_constraints(constraint)

    def process_phrase(self, phrase:str) -> None:
        if len(phrase) == 0:
            Logger.warning("Empty phrase")
            return
        if not phrase.endswith('.'):
            phrase += '.'