from database.connection import get_db_connection

class Magazine:
    __tablename__ = 'magazines'

    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    def id(self):
        return self.id

    def name(self):
        return self._name

    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Name must be a string between 2 and 16 characters long")

    def category(self):
        return self._category

    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string")
        
    @classmethod
    def fetch_all(cls, cursor): 
        magazines = []
        cursor.execute("SELECT * FROM magazines")
        rows = cursor.fetchall()
        for row in rows:
            magazine = cls(*row)
            magazines.append(magazine)
        return magazines   

    def save(self):
        conn = get_db_connection()
        cursor=conn.cursor()
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?,?)', (self.name, self.category))
        conn.commit()
        conn.close()
        return 

    def _repr_(self) :
        return f'<Magazine {self.name} >'
   
