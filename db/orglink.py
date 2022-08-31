from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy import String

Base = declarative_base()

class Orglink(Base):
    
    __tablename__ = "orglink"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, doc="Title for url")
    description = Column(String, nullable=False, doc="Description for url")
    url = Column(String, nullable=False, doc="URL")
    slug = Column(String, nullable=True, doc="SLUG" )
    
    def __repr__(self):
        return "<Orglink('%s','%s','%s','%s','%s')>" % (self.id, self.title, self.description, self.url, self.slug)


if __name__ == '__main__':
    from sqlalchemy import create_engine
    engine = create_engine("sqlite://", echo=True, future=True)
    Base.metadata.create_all(engine)
    