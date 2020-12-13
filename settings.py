from app import db, create_one_time_entry

def create_tables():
    db.create_all()
    create_one_time_entry()

if __name__ == "__main__":
    create_tables()