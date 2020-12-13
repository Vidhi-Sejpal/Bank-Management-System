from app import db, create_one_time_entry

def create_tables():
    db.create_all()

if __name__ == "__main__":
    create_tables()
    create_one_time_entry()