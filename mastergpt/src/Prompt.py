

class Prompt:

    def __init__(self, input:str) -> None:
        self.input = input
        self.output = None

    def get_prompt(self) -> str:
        return self.output

    def get_prompt_tokens(self):
        pass

    def minimalize(self) -> Prompt:
        pass

