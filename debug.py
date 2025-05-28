# debug.py

from lib.models import Company, Dev, Freebie
from lib.database import session

def run_tests():
    print("\n=== STARTING DEBUG TESTS ===")

    # Get the first company and dev
    c1 = session.query(Company).first()
    d1 = session.query(Dev).first()

    if not c1 or not d1:
        print(" Run seed.py first to add sample data.")
        return

    # Give a freebie
    freebie = c1.give_freebie(d1, "Sticker", 10)
    print("\n Created freebie:")
    freebie.print_details()

    # Test received_one
    print(f"\n Did {d1.name} receive 'Sticker'? {d1.received_one('Sticker')}")

    # Test oldest company
    oldest = Company.oldest_company(session)
    print(f"\n Oldest company is: {oldest.name} (Founded in {oldest.founding_year})")

    # Test give_away
    d2 = session.query(Dev).filter(Dev.id != d1.id).first()
    if d2:
        d1.give_away(d2, freebie)
        print(f"\n {d1.name} gave away {freebie.item_name} to {d2.name}")
    else:
        print(" Only one developer in DB, can't test give_away.")

    # Test relationships
    print(f"\n{d1.name}'s freebies: {[f.item_name for f in d1.freebies]}")
    print(f" {d1.name}'s companies: {[c.name for c in d1.companies]}")
    print(f" {c1.name}'s freebies: {[f.item_name for f in c1.freebies]}")
    print(f" {c1.name}'s devs: {[dev.name for dev in c1.devs]}")

    print("\n=== DEBUG TESTS DONE ===")

if __name__ == "__main__":
    run_tests()
