from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_cors import CORS
import os
from config import *

app = Flask(__name__)
cors = CORS(app)
is_prod_config = False

# Load the config file
if 'FLASK_APP_MODE' in os.environ.keys():
    app.config.from_object(os.environ['FLASK_APP_MODE'])
    print('FLASK_APP_MODE: ' + os.environ['FLASK_APP_MODE'])
    mode = os.environ['FLASK_APP_MODE'].split(".")[1]
    engin = create_engine(eval(mode).SQLALCHEMY_DATABASE_URI)
    if os.environ['FLASK_APP_MODE'] == "config.ProductionConfig": 
        is_prod_config = True
    

else:
    print('FLASK_APP_MODE: ', 'Develop Mode')
    app.config.from_object('config.DevelopmentConfig')
    engin = create_engine(DevelopmentConfig.SQLALCHEMY_DATABASE_URI)


db = SQLAlchemy(app)
##Modules Import
from app.UI import home
from app.year.controller import years
from app.asset_type.controller import assettypes
from app.segment_master.controller import segmnts
from app.asset_group.controller import assetgroups
from app.unit_master.controller import units
from app.vtype.controller import vtypes
from app.employee.controller import employees
from app.department.controller import departments
from app.asset.controller import assets
from app.voucher.controller import vouchers
from app.depreciation.controller import depreciation
from app.excel_import.controller import excelimport

# ## Create Blueprint of Modules
app.register_blueprint(home,url_prefix='/fixedasset')
app.register_blueprint(years)
app.register_blueprint(assettypes)
app.register_blueprint(segmnts)
app.register_blueprint(assetgroups)
app.register_blueprint(units)
app.register_blueprint(vtypes)
app.register_blueprint(employees)
app.register_blueprint(departments)
app.register_blueprint(assets)
app.register_blueprint(vouchers)
app.register_blueprint(depreciation)
app.register_blueprint(excelimport)