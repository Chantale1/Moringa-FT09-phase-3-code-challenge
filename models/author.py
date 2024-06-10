
from database.connection import get_db_connection

class Author:
    
    def _init_(self, id=None, name=None):
        self._id = id
        self._name = name

    

    def id(self):
        return self._id

    
    def name(self):
        return self._name

    
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    
    def save(self, cursor):
        conn = get_db_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('INSERT INTO authors (name) VALUES (?)', (self.name,))
            
            self._id = cursor.lastrowid
        
        else:
            cursor.execute('UPDATE authors SET name = ? WHERE id = ?', (self.name, self.id))
        conn.commit()
        conn.close()


    def fetch_all(cursor):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors')
        authors = cursor.fetchall()
        conn.close()
        return [Author(author['id'], author['name']) for author in authors]

    def _repr_(self):
        return f'<Author {self.name}>'

