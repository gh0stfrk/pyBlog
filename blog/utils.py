from html.parser import HTMLParser

class HTMLTextExtractor(HTMLParser):
    """ Extracts Text from html markup """
    def __init__(self):
        super().__init__()
        self.result = []
    
    def handle_data(self, d):
        self.result.append(d)
    
    def get_text(self):
        return ''.join(self.result)