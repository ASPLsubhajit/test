from app import db
from flask import make_response, render_template,Response
from flask_cors import cross_origin
from . import home
import json

@home.route("/",methods=['GET'],defaults={'path':''} )
@home.route('/<path:path>' ,methods=['GET'])
def show(path):
    r = make_response(render_template('index.html'))
    print("fixedasset before request!...: ", r)
    # r.headers.set('Content-Security-Policy', "default-src 'self'")
    return r
