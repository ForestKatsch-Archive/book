
class BookError(Exception):
    
    def __init__(self,strerror):
        self.strerror=strerror
