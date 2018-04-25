
import bottle
from web.bottleApp import app
from questions import *






main = bottle.Bottle()
main.mount("/config/",configure)
main.mount("/",app)

main.run(host = 'localhost', port=8080)
and on configure/config.py something like this:

import bottle

config_app = bottle.Bottle()

@config_app.route('/config1')
def config1():
    return 'some config data'




from bottle import route, run, template






i=0
@route('/dbmsq')
def index(dbmsq):
    for i in range(5):
        d= {}
        d["question"] = dbmsq[i]
        d["answer"] = ("dbsans"+str(i))
        i+=1
    return dbmsq[i]
        #return d

@route('/osq')
def osq():
    d= {}
    d["question"] = dbmsq[i]
    d["answer"] = ("dbsans"+str(i))
    i+=1
    return template('<b>Hello1</b>!')
    #return d
@route('/get_question/dbmsq')
def cnq():
    d= {}
    d["question"] = dbmsq[i]
    d["answer"] = ("dbsans"+str(i))
    i+=1
    return d
@route('/get_question/dbmsq')
def dsq():
    d= {}
    d["question"] = dbmsq[i]
    d["answer"] = ("dbsans"+str(i))
    i+=1
    return d



run(host='localhost', port=8080)
