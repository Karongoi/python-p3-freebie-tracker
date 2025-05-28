# lib/models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from lib.database import Base, session

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    founding_year = Column(Integer)
    freebies = relationship("Freebie", back_populates="company")
    devs = relationship("Dev", secondary="freebies", back_populates="companies", viewonly=True)

    def give_freebie(self, dev, item_name, value):
        freebie = Freebie(item_name=item_name, value=value, company=self, dev=dev)
        session.add(freebie)
        session.commit()
        return freebie

    @classmethod
    def oldest_company(cls, session):
        return session.query(cls).order_by(cls.founding_year).first()

    def __repr__(self):
        return f"<Company(name={self.name})>"

class Dev(Base):
    __tablename__ = "devs"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    freebies = relationship("Freebie", back_populates="dev")
    companies = relationship("Company", secondary="freebies", back_populates="devs", viewonly=True)

    def received_one(self, item_name):
        return any(f.item_name == item_name for f in self.freebies)

    def give_away(self, other_dev, freebie):
        if freebie in self.freebies:
            freebie.dev = other_dev
            session.commit()

    def __repr__(self):
        return f"<Dev(name={self.name})>"

class Freebie(Base):
    __tablename__ = "freebies"
    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    value = Column(Integer)
    company_id = Column(Integer, ForeignKey("companies.id"))
    dev_id = Column(Integer, ForeignKey("devs.id"))
    company = relationship("Company", back_populates="freebies")
    dev = relationship("Dev", back_populates="freebies")

    def print_details(self):
        print(f"{self.dev.name} owns a {self.item_name} from {self.company.name}")

    def __repr__(self):
        return f"<Freebie(item_name={self.item_name}, value={self.value})>"
