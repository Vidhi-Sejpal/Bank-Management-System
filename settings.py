from app import db

def create_tables():
    db.create_all()

if __name__ == "__main__":
    create_tables()