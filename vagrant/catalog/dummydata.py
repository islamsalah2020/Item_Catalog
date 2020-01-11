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


# Create dummy user
user1 = User(name="Abu Salah", email="islam.salah2020@ymail.com",
             picture='https://drive.google.com/open?id=1Mr1OKn3cCgs5baFoZkRq1mM-s0BZ2Dze')
session.add(user1)
session.commit()

User2 = User(name="abdo Salah", email="abdo@ymail.com",
             picture='https://drive.google.com/open?id=1Mr1OKn3cCgs5baFoZkRq1mM-s0BZ2Dze')
session.add(User2)
session.commit()

# items for Condrichthyes
Category1 = Category(user_id=1, name="Condrichthyes")

session.add(Category1)
session.commit()

Item1 = CategoryItem(user_id=1, name="sharks", description="Juicy grilled veggie patty with tomato mayo and lettuce",
             category=Category1)

session.add(Item1)
session.commit()

Item2 = CategoryItem(user_id=1, name="Manta rays", description='''have broad heads, triangular pectoral fins, 
             and horn-shaped cephalic fins located on either side of their mouths.''',
             category=Category1)

session.add(Item2)
session.commit()

Item3 = CategoryItem(user_id=1, name="Skates", description='''Skates mate at the same nursery 
             ground each year. In order to fertilize the egg, males use claspers,
             a structure attached to the pelvic fins. The claspers allow them to
             direct the flow of semen into the female's cloaca.''',
             category=Category1)

session.add(Item3)
session.commit()

# items for Mammals
Category2 = Category(user_id=1, name="Mammals")

session.add(Category2)
session.commit()

Item1 = CategoryItem(user_id=1, name="Kangaroo", description='''Neonates saved in a pouch in mother body until
             they becomes more active and gradually spends more and more time outside the pouch, they
             leave completely at 7 to 10 months of age.''',
             category=Category2)

session.add(Item1)
session.commit()

Item2 = CategoryItem(user_id=1, name="Monkey", description='''Monkey brains are eaten in parts of South Asia, 
             Africa and China. Monkeys are sometimes eaten in parts of Africa.''',
             category=Category2)

session.add(Item2)
session.commit()

Item3 = CategoryItem(user_id=1, name="Cats", description='''have excellent night vision.
             The domestic cat's hearing is most acute in the range of 500 Hz to 32 kHz.''',
             category=Category2)

session.add(Item3)
session.commit()



# items for Aves
Category3 = Category(user_id=1, name="Aves")

session.add(Category3)
session.commit()

print "done"

print "done"
print "done"