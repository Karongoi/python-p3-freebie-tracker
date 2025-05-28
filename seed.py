# seed.py

from lib.database import session
from lib.models import Company, Dev

def seed():
    # Create sample companies
    c1 = Company(name="Acme Corp", founding_year=2000)
    c2 = Company(name="Beta LLC", founding_year=1995)

    # Create sample developers
    d1 = Dev(name="Alice")
    d2 = Dev(name="Bob")

    # Add all to session
    session.add_all([c1, c2, d1, d2])
    
    # Commit to save to database
    session.commit()
    print("Seeded companies and developers successfully.")

if __name__ == "__main__":
    seed()
