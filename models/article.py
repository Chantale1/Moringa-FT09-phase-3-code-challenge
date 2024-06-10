class Article:
    def _init_(self, id=None, title=None, content=None, author_id=None, magazine_id=None):
        self._id = id
        self._title = title
        self._content = content
        self._author_id = author_id
        self._magazine_id = magazine_id


    @property
    def id(self):
        return self._id


    @property
    def title(self):
        return self._title

    
    @title.setter
    def title(self, title):
        self._title = title

    
    @property
    def content(self):
        return self._content

    # Set the article's content
    @content.setter
    def content(self, content):
        self._content = content

    # Define a property for the article's author id
    @property
    def author_id(self):
        return self._author_id

    # Set the article's author id
    @author_id.setter
    def author_id(self, author_id):
        self._author_id = author_id


    @property
    def magazine_id(self):
        return self._magazine_id
    @magazine_id.setter
    def magazine_id(self, magazine_id):
        self._magazine_id = magazine_id

    
    def save(self, cursor):
        if self.id is None:
            cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                           (self.title, self.content, self.author_id, self.magazine_id))
            self._id = cursor.lastrowid
        else:
            cursor.execute('UPDATE articles SET title = ?, content = ?, author_id = ?, magazine_id = ? WHERE id = ?',
                           (self.title, self.content, self.author_id, self.magazine_id, self.id))

    
    def _repr_(self):
        return f'<Article {self.title}>'