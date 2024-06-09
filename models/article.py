class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id
    

    
    def title(self):
        return self._title

    
    def author(self):
        return self._author

    
    def magazine(self):
        return self._magazine

    
    def __repr__(self):
        return f'<Article {self.title}>'
