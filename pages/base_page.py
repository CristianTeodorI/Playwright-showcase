class BasePage:
    
    def __init__(self, page):
        self.page = page

    def navigate(self, path=""):
        self.page.goto(path)

    def title(self):
        return self.page.title()