class Author:
    __tablename__ = 'authors'

    def __init__(self, name):
        self._name = name  

    
    def id(self):
        return self.id  

    
    def name(self):
        return self._name

    
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

