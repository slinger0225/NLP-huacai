# -*- coding: utf-8 -*-
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os
class Application( Flask ):
    def __init__(self,import_name,template_folder=None,root_path=None):
        super( Application,self ).__init__( import_name,template_folder=template_folder,root_path=root_path,static_folder=None)
        self.config.from_pyfile( 'config/base_setting.py' )
        #环境变量
        if "ops_config" in os.environ:
            self.config.from_pyfile( 'config/%s_setting.py'%os.environ['ops_config'] )



app = Application( __name__ ,root_path=os.getcwd())
manager = Manager( app )

