from this import d
from CoronaArchive import db, bcrypt
from CoronaArchive.models import Agent, User, Place, Hospital

db.create_all()
agent = Agent(email = 'admin', password = bcrypt.generate_password_hash('password').decode('utf-8'))

user1= User(name='Monica Geller', email = 'm.geller@gmail.com', phoneNumber = '12345678', password= bcrypt.generate_password_hash('password').decode('utf-8'))
user2= User(name='Ross Geller', email = 'r.geller@gmail.com', phoneNumber = '87654321', password= bcrypt.generate_password_hash('password').decode('utf-8'))
user3= User(name='Rachel Green', email = 'r.green@gmail.com', phoneNumber = '24681357', password= bcrypt.generate_password_hash('password').decode('utf-8'))
user4= User(name='Chandler Bing', email = 'c.bing@gmail.com', phoneNumber = '13572468', password= bcrypt.generate_password_hash('password').decode('utf-8'))

place1 = Place(name='Pizza Protein', email = 'p.protein@gmail.com', phoneNumber = '76458975', password= bcrypt.generate_password_hash('password').decode('utf-8'))
place2 = Place(name='Mcdonalds', email = 'mickeyd@gmail.com', phoneNumber = '43298412', password= bcrypt.generate_password_hash('password').decode('utf-8'))
place3 = Place(name='Ogalo', email = 'og@gmail.com', phoneNumber = '943290473', password= bcrypt.generate_password_hash('password').decode('utf-8'))

hospital = Hospital(name='Hospital1', email = 'hospital@gmail.com', phoneNumber = '5522641404', password= bcrypt.generate_password_hash('password').decode('utf-8'))

db.session.add(agent)
db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
db.session.add(user4)
db.session.add(place1)
db.session.add(place2)
db.session.add(place3)
db.session.add(hospital)
db.session.commit()