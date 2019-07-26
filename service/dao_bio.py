
from Models.Bio import Bio_F,Bio_M,db

class BioService:
    def __init__(self):
        pass

    @staticmethod
    def get_all_female_bio():
        return  Bio_F.query.all()

    @staticmethod
    def get_all_male_bio():
        return Bio_M.query.all()

    @staticmethod
    def add_bio(self,data):
        if data.gender == 'F':
            db.session.add(Bio_F)
        else:
            db.session.add(Bio_M)
        db.session.commit()