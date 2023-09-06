class Input:
    def __init__(self, text, loc):
        self.loc = loc
        self.text = text

search = Input('текс_1','локатор_1')
print(search.text)
print(search.loc)
print()

class Button:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
search_Button = Button('текст_2','локатор_2')
print(search_Button.text)
print(search_Button.loc)
print()

class Title:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

search_Title = Title('текст_3','локатор_3')
print(search_Title.text)
print(search_Title.loc)
print()
class Link:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
search_Link = Link('текст_4','локатор_4')
print(search_Link.text)
print(search_Link.loc)
print()