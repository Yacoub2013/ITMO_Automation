from python_trening.task_9_checks import Checks
class Input(Checks):

    def __init__ (self, text, loc):
        self.text = text
        self.loc = loc
        super().__init__(loc)
search = Input('текст_1','Локатор _1')
print(search.text)
print(search.loc)

print()

class Button(Checks):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
        super().__init__(loc)
search_Button = Button('текст_2','локатор_2')
print(search_Button.text)
print(search_Button.loc)
print()

class Title(Checks):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
        super().__init__(loc)

search_Title = Title('текст_3','локатор_3')
print(search_Title.text)
print(search_Title.loc)
print()
class Link(Checks):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
        super().__init__(loc)
search_Link = Link('текст_4','локатор_4')
print(search_Link.text)
print(search_Link.loc)
print()