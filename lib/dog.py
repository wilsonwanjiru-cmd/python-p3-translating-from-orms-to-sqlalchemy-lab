from models import Dog

def create_table(base, engine):
    # This function should create the table in the SQLite database using the provided base and engine.
    base.metadata.create_all(engine)

def save(session, dog):
    # This function should save the dog object to the database.
    session.add(dog)
    session.commit()

def get_all(session):
    # This function should return a list of all dogs in the database.
    return session.query(Dog).all()

def find_by_name(session, name):
    # This function should find and return a dog by its name.
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    # This function should find and return a dog by its ID.
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    # This function should find and return a dog by its name and breed.
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    # This function should update the breed of a dog.
    dog.breed = breed
    session.commit()
