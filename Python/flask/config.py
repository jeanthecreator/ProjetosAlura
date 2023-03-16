from jogoteca import app

SECRET_KEY = 'trovador'
SQLALCHEMY_DATABASE_URI = \
    "{SGBD}://{username}:{password}@{local_port}/{database}".format(
        SGBD = 'mysql+mysqlconnector',
        username = 'root',
        password = 'admin',
        local_port = 'localhost',
        database = 'jogoteca'
)
