import bottle

cnqapp = bottle.Bottle()

@cnqapp.route('/dbmsq')
def config1():
    cnq=["What is Stop-and-Wait Protocol?","What is DHCP, how does it work?","Define Network?","What is Protocol?","What is point-point link?"]

    return cnq[0]
