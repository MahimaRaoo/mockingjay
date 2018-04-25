import bottle

dbmsqapp = bottle.Bottle()

@dbmsqapp.route('/dbmsq')
def config1():
    dbmsq =["What is a Superkey?","What is SQL?","What is a primary key?","What is a foreign key?","What is database normalization?"]

    return dbmsq[0]
