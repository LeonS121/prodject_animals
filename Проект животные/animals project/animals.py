import sqlite3  


class Shelter:

    def __init__(self):    
        self.db = sqlite3.connect("animal.txt")
        self.cur = self.db.cursor()
        self.list_animals = ["animal", "name", "breed", "age", "gender", "commands", "packani", "date_1", "date_2", "vaccine", "date_vac"]
        
        self.cur.execute(f"""
        CREATE TABLE IF NOT EXISTS animals_table (
                id INTEGER PRIMARY KEY NOT NULL,
                {self.list_animals[0]} TEXT,
                {self.list_animals[1]} TEXT,
                {self.list_animals[2]} TEXT,
                {self.list_animals[3]} INTEGER,
                {self.list_animals[4]} TEXT,
                {self.list_animals[5]} TEXT,
                {self.list_animals[6]} TEXT,
                {self.list_animals[7]} INTEGER,
                {self.list_animals[8]} INTEGER,
                {self.list_animals[9]} TEXT,
                {self.list_animals[10]} INTEGER)""")
        self.db.commit()
    
    def main(self, animal, name, breed, age, gender, commands, packani, date_1, date_2, vaccine, date_vac):
        self.cur.execute(f"""INSERT INTO animals_table (
                {self.list_animals[0]},
                {self.list_animals[1]},
                {self.list_animals[2]},
                {self.list_animals[3]},
                {self.list_animals[4]},
                {self.list_animals[5]},
                {self.list_animals[6]},
                {self.list_animals[7]},
                {self.list_animals[8]},
                {self.list_animals[9]},
                {self.list_animals[10]})
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (animal, name, breed, age, gender, commands, packani, date_1, date_2, vaccine, date_vac))
        self.db.commit()
