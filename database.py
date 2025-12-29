import sqlite3

class ConnectionClassDatabase():
    def __init__(self , filename):
        self.conn = None
        self.filename = filename
        
    def __enter__(self):
        self.conn = sqlite3.connect(self.filename)
        print("Connection created!")
        return self.conn
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()
        print("Connection committed and closed!")