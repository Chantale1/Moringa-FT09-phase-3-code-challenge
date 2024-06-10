from database.connection import get_db_connection

# Define a class for magazines
class Magazine:
    # Initialize a magazine with optional parameters
    def _init_(self, id=None, name=None, category=None):
        # Initialize instance variables
        self._id = id
        self._name = name
        self._category = category

    
    @property
    def id(self):
        return self._id

    
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


    def save(self, cursor):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        if self.id is None:
            cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (self.name, self.category))
            self._id = cursor.lastrowid
        
        else:
            cursor.execute('UPDATE magazines SET name = ?, category = ? WHERE id = ?', (self.name, self.category, self.id))
        conn.commit()
        conn.close()

    
    def fetch_all(cls, cursor):
        magazines = []
        cursor.execute("SELECT * FROM magazines")
        rows = cursor.fetchall()
        
        for row in rows:
            magazine = cls(*row)
            magazines.append(magazine)
        return magazines

    def _repr_(self):
        return f'<Magazine {self.name}>'