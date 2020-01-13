
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CategoryItem, User

engine = create_engine('sqlite:///catalog.db')

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()



print "start"

users = session.query(User).all()
for o in users:
    session.delete(o)


objects = session.query(Category).all()
for o in objects:
    session.delete(o)


objects = session.query(CategoryItem).all()
for o in objects:
    session.delete(o)


User.__table__.drop()
Category.__table__.drop()
CategoryItem.__table__.drop()

print "end"

# categories = session.query(CategoryItem).all()
# for x in categories:
#         print  x
