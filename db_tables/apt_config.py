from sqlalchemy import Column, Integer, String
from db_tables import Base
#Base = declarative_base()

class MyConfig(Base):
    __tablename__ = 'apt_config'

    id = Column(Integer, primary_key=True)
    config_name = Column(String)
    description = Column(String)
    user_id = Column(String)
    user_name = Column(String)
    customer  = Column(String)
    fk_customer = Column(String)
    create_date = Column(String)
    config  = Column(String)
    active = Column(Integer)

    def __repr__(self):
        return "<MyConfig(config_name='%s', description='%s')>" % (
                             self.config_name, self.description)
