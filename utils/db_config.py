import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('database.sqlite')
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns})')
        self.connection.commit()
    
    def insert(self, table_name, columns, values):
        self.cursor.execute(f'INSERT INTO {table_name} ({columns}) VALUES ({values})')
        self.connection.commit()

    def select(self, table_name, columns, condition):
        self.cursor.execute(f'SELECT {columns} FROM {table_name} WHERE {condition}')
        return self.cursor.fetchall()
    
    def update(self, table_name, columns, condition):
        self.cursor.execute(f'UPDATE {table_name} SET {columns} WHERE {condition}')
        self.connection.commit()

    def delete(self, table_name, condition):
        self.cursor.execute(f'DELETE FROM {table_name} WHERE {condition}')
        self.connection.commit()

    def close(self):
        self.connection.close()

