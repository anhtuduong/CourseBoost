from Section import Section

class Base:
    
    def __init__(self) -> None:
        self.json_file = ""
        self.title = ""
        self.description = ""
        self.body = []

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    def add_section(self, section):
        self.body.append(section)

    def export(self, file_name):
        pass