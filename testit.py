
from Models.Bio import db,Bio_M

db.create_all()
new_bio = Bio_M(firstname='Ajit',)
db.session.add(new_bio)
db.session.commit()
