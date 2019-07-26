
from dbinit import db
from Models.CustomEnums import *


class Bio_M(db.Model):
    #__table__ = db.Model.metadata.tables['Bio_M']
    #__tablename__ = 'Bio_M'
    id = db.Column(db.Integer, primary_key=True)
    
    #Candidate-Bio
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date,nullable=False)
    caste = db.Column(Enum(EnumCaste))
    bloodgroup = db.Column(Enum(EnumBloodGroup))
    weight = db.Column(db.Integer, nullable=False)
    education = db.Column(db.String(100), nullable=True)
    job = db.Column(db.String(100), nullable=False)
    earning = db.Column(db.String(100), nullable=True)
    height =  db.Column(db.String(5), nullable=False) #5 ft 5 inch will be stored as 5.5
    complexion = db.Column(Enum(EnumComplexion))
    disability = db.Column(db.Boolean, nullable=False)
    disability_desc = db.Column(db.String(200), nullable=True)
    spectacle = db.Column(db.Boolean, nullable=True)
    diet = db.Column(Enum(EnumDiet))
    primary_photo = db.Column(db.String(200), nullable=False)
    secondary_photo = db.Column(db.String(200), nullable=True)
    current_country = db.Column(db.String(100), nullable=False)
    current_state = db.Column(db.String(100), nullable=False)
    current_city = db.Column(db.String(100), nullable=False)

    #marriage_related
    maritialstatus = db.Column(Enum(EnumMangal))
    gotra_devak = db.Column(db.String(100), nullable=True)
    mangal = db.Column(Enum(EnumMangal))
    rashi = db.Column(Enum(EnumRashi))
    charan = db.Column(Enum(EnumCharan))
    nadi = db.Column(Enum(EnumNadi))
    nakshtra = db.Column(Enum(EnumNakshtra))
    gan = db.Column(Enum(EnumGan))
    Nativeplace = db.Column(db.String(100), nullable=False)#should auto-generate from birthif not given
    birthtime = db.Column(db.Time, nullable=False)
    birth_country = db.Column(db.String(100), nullable=False)
    birth_state = db.Column(db.String(100), nullable=False)
    birth_city = db.Column(db.String(100), nullable=False)
    relative_surname = db.Column(db.String(400), nullable=True)
    mama = db.Column(db.String(70), nullable=True)
    family_wealth = db.Column(db.String(250), nullable=True)

    #contact
    document = db.Column(db.String(50), nullable=False) # PAN/Aadhar/Driving License/Passport
    primary_number = db.Column(db.String(10), nullable=False)
    secondary_number = db.Column(db.String(10), nullable=True)
    email_id = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(300), nullable=False)

    #Family
    father_name = db.Column(db.String(100), nullable=False)
    father_alive = db.Column(db.Boolean, nullable=True)
    father_occupationn = db.Column(db.String(100), nullable=False)

    mother_alive = db.Column(db.Boolean, nullable=True)
    mother_name = db.Column(db.String(100), nullable=False)
    mother_occupationn = db.Column(db.String(100), nullable=False)

    brothers_unmarried = db.Column(db.Integer, nullable=False)
    brothers_married = db.Column(db.Integer, nullable=False)
    sisters_unmarried = db.Column(db.Integer, nullable=False)
    sisters_married = db.Column(db.Integer, nullable=False)
    
    parent_country = db.Column(db.String(100), nullable=False)
    parent_state = db.Column(db.String(100), nullable=False)
    parent_city = db.Column(db.String(100), nullable=False)

    #Expectation
    caste = db.Column(db.String(250), nullable=False)
    preferredCities = db.Column(db.String(100), nullable=False)
    minheight = db.Column(db.String(5), nullable=False)
    maxheight = db.Column(db.String(5), nullable=False)
    education = db.Column(db.String(100), nullable=False)
    minincome = db.Column(db.String(100), nullable=False)
    mangal = db.Column(Enum(EnumMangal))
    max_age_diff = db.Column(db.Integer, nullable=False)
    divorcee = db.Column(db.Boolean, nullable=False)
    intercast = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.firstname

class Bio_F(db.Model):
    #__tablename__ = 'Bio_F'

    id = db.Column(db.Integer, primary_key=True)
    
    #Candidate-Bio
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date,nullable=False)
    caste = db.Column(Enum(EnumCaste))
    bloodgroup = db.Column(Enum(EnumBloodGroup))
    weight = db.Column(db.Integer, nullable=False)
    education = db.Column(db.String(100), nullable=True)
    job = db.Column(db.String(100), nullable=False)
    earning = db.Column(db.String(100), nullable=True)
    height =  db.Column(db.String(5), nullable=False) #5 ft 5 inch will be stored as 5.5
    complexion = db.Column(Enum(EnumComplexion))
    disability = db.Column(db.Boolean, nullable=False)
    disability_desc = db.Column(db.String(200), nullable=True)
    spectacle = db.Column(db.Boolean, nullable=True)
    diet = db.Column(Enum(EnumDiet))
    primary_photo = db.Column(db.String(200), nullable=False)
    secondary_photo = db.Column(db.String(200), nullable=True)
    current_country = db.Column(db.String(100), nullable=False)
    current_state = db.Column(db.String(100), nullable=False)
    current_city = db.Column(db.String(100), nullable=False)

    #marriage_related
    maritialstatus = db.Column(Enum(EnumMangal))
    gotra_devak = db.Column(db.String(100), nullable=True)
    mangal = db.Column(Enum(EnumMangal))
    rashi = db.Column(Enum(EnumRashi))
    charan = db.Column(Enum(EnumCharan))
    nadi = db.Column(Enum(EnumNadi))
    nakshtra = db.Column(Enum(EnumNakshtra))
    gan = db.Column(Enum(EnumGan))
    Nativeplace = db.Column(db.String(100), nullable=False)#should auto-generate from birthif not given
    birthtime = db.Column(db.Time, nullable=False)
    birth_country = db.Column(db.String(100), nullable=False)
    birth_state = db.Column(db.String(100), nullable=False)
    birth_city = db.Column(db.String(100), nullable=False)
    relative_surname = db.Column(db.String(400), nullable=True)
    mama = db.Column(db.String(70), nullable=True)
    family_wealth = db.Column(db.String(250), nullable=True)

    #contact
    document = db.Column(db.String(50), nullable=False) # PAN/Aadhar/Driving License/Passport
    primary_number = db.Column(db.String(10), nullable=False)
    secondary_number = db.Column(db.String(10), nullable=True)
    email_id = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(300), nullable=False)

    #Family
    father_name = db.Column(db.String(100), nullable=False)
    father_alive = db.Column(db.Boolean, nullable=True)
    father_occupationn = db.Column(db.String(100), nullable=False)

    mother_alive = db.Column(db.Boolean, nullable=True)
    mother_name = db.Column(db.String(100), nullable=False)
    mother_occupationn = db.Column(db.String(100), nullable=False)

    brothers_unmarried = db.Column(db.Integer, nullable=False)
    brothers_married = db.Column(db.Integer, nullable=False)
    sisters_unmarried = db.Column(db.Integer, nullable=False)
    sisters_married = db.Column(db.Integer, nullable=False)
    
    parent_country = db.Column(db.String(100), nullable=False)
    parent_state = db.Column(db.String(100), nullable=False)
    parent_city = db.Column(db.String(100), nullable=False)

    #Expectation
    caste = db.Column(db.String(250), nullable=False)
    preferredCities = db.Column(db.String(100), nullable=False)
    minheight = db.Column(db.String(5), nullable=False)
    maxheight = db.Column(db.String(5), nullable=False)
    education = db.Column(db.String(100), nullable=False)
    minincome = db.Column(db.String(100), nullable=False)
    mangal = db.Column(Enum(EnumMangal))
    max_age_diff = db.Column(db.Integer, nullable=False)
    divorcee = db.Column(db.Boolean, nullable=False)
    intercast = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.firstname
