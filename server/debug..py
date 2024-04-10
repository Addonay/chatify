import os

base_dir = os.path.dirname(os.path.abspath(__file__))
database_url = f"sqlite:///{os.path.join(base_dir, 'db', 'db.sqlite3')}"


print(database_url)