# migrate.py

from lib.database import Base, engine
from lib.models import Company, Dev, Freebie

def migrate():
    # Create all tables defined by your models
    Base.metadata.create_all(engine)
    print("Tables created successfully!")

if __name__ == "__main__":
    migrate()
