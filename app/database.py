import os
from sqlalchemy import create_engine, inspect, MetaData,
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base

# The info to our database for the docker instance depends on the env_file
# This is for the heroku instance,
'''
# DON'T PUT THIS IN PRODUCTION
'''

host = os.environ['host']
db = os.environ['db']
user = os.environ['user']
port = os.environ['port']
pwd = os.environ['pwd']


def create_engine_here(user=user, pwd=pwd, host=host, port=port, db=db):
    engine = create_engine(
        'postgresql://{user}:{pwd}@{host}:{port}/{db}'.format(user=user, pwd=pwd, host=host, port=port, db=db))
    return engine


engine = create_engine_here()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


# Magic involving mapping psql schemas. Need to read up on that
# AutoBase = automap_base()
# AutoBase.prepare(engine, reflect=True)
