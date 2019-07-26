from flask_app import get_app
from service.dao_bio import BioService

app=get_app()

app.route('/bio/male',classmethod=['GET'])
def get_all_bio():
    female_bio = BioService.get_all_female_bio()
    male_bio = BioService.get_all_male_bio()
    return male_bio



