import sqlalchemy
import os
from flask_sqlalchemy import SQLAlchemy

db_user = 'ctgdevops'
db_password = 'devops123'
db_name = 'ctg_devops_ktracker'
db_host = '34.66.229.117

db_url = f"postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}"
db = SQLAlchemy()