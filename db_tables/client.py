from sqlalchemy import Column, Integer, String
from db_tables import Base

class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    cpid = Column(String)
    description = Column(String)
    address1 = Column(String)
    city = Column(String)
    state = Column(String)
    account_type = Column(String)
    create_date = Column(String)
    active = Column(String)
