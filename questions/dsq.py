import bottle

dsqapp = bottle.Bottle()

@dsqapp.route('/dbmsq')
def config1():
    dsq=["","","","",""]

    return dsq[0]
