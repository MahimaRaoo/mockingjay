import bottle

osqapp = bottle.Bottle()

@osqapp.route('/dbmsq')
def config1():
    osq=["What is kernel?","What is a process?","What is  virtual memory?","What is context switch?","What is deadlock?"]

    return osq[0]
