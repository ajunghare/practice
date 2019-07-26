from flask_sqlalchemy import SQLAlchemy
from flask_app import get_app
app= get_app()
db = SQLAlchemy(app)
#db.init_app(app)
#db.app = app
##db.metadata
#db.Model.metadata.reflect(db.engine)


