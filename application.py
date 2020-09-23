from flask import Flask, render_template, request
import os
import SqlConnector
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from flask_jsonpify import jsonify


app = Flask(__name__)
allnames = []

api = Api(app)
CORS(app)


@app.route("/")
def home():
    return jsonify({'text': 'welcome to the flask demo'})

class Employees(Resource):
    def get(self):
        allnames = SqlConnector.searchall()
        print(allnames)
        print(type(allnames))
        return jsonify(allnames)

class GetEmpByname(Resource):
    def get(self, name):
        emprecord = SqlConnector.searchempbyname(name)
        return jsonify(emprecord)
api.add_resource(Employees, '/employees')
api.add_resource(GetEmpByname, '/employee/<name>')
# @app.route("/GetEmp", methods=['GET', 'POST'])
# def getastronautinfo():
#     return render_template("GetEmp.html")
#
#
# @app.route("/fetchdata", methods=['GET','POST'])
# def fetchdata():
#     first_name = "test"
#
#     if first_name:
#         allnames = SqlConnector.searchemp(first_name)
#     else:
#         noname = ""
#         allnames = SqlConnector.searchemp(noname)
#
#     return allnames