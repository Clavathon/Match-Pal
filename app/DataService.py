from database import db_session
from json import loads
from models import *

from sqlalchemy import inspect


class DataService():
    """docstring for DataService.
    This is the service which the database(?) calls to directly query results,
    given a model, session, and sql query(or the likes)
    CRUD operator in short
    """
    from sqlalchemy.orm import scoped_session

    def __init__(self, table_model):
        # if C_Validator:     # If a Validator Class was passed in
        #     self.validator = C_Validator
        # self.table_model = C_Validator.table_model
        self.table_model = table_model
        self.inspect = inspect

    def __get_column_from_model(self, model):
        # gets all th column name attrs and return them in string form
        mapper = self.inspect(model)
        result = [column.key for column in mapper.attrs]
        return result

    def __get_data_from_model(self, model, column_name):

        # programmatically retrieve value from models given known attr values
        if not model:
            return []

        result = []
        for name in column_name:
            que = "model.{}".format(name)
            result.append(eval(que))
        return result

    def create(self, instance: dict, session: scoped_session, query=None):
        '''
        type: instance: dictionary
        type: session:  session object
        type: query: optional string query

        Insert a new item into our table,
        should raise an exception if conflicting model values are provided
        '''
        if not query:
            try:
                # self.validator.check(instance)       # validate json input first
                new_model = self.table_model(instance)  # create model from validator
                session.add(new_model)                  # add to database
                session.commit()                        # save changes
            except Exception as e:
                session.rollback()
                raise e
            finally:
                session.close()
        else:
            return 'Query provided: {}\n'.format(query if query else 'new_model')

    def read(self, instance: dict, session, query=None):
        '''
        type: instance: dictionary aka json obj containing the key value for model property
        type: session:  session object
        type: query: optional string query
        '''

        # Wait... Patients has not firstname... it is in the data column
        if not query:
            # pythonic item iterator combination to programmatically apply filter terms to query
            # Consider using generator over iterator for list comprehension if item read is a large file needing to be filtered
            dict_item = ["self.table_model.{} == '{}'".format(
                k, v) for k, v in instance.items() if v]
            filter_items = ", ".join(dict_item)
            query_str = 'session.query(self.table_model).filter({}).all()'.format(filter_items)
            result = eval(query_str)    # DON'T USE exec(). WRONG FUNCTION
            if not result:
                return "Literally nothing :("
            column_name = self.__get_column_from_model(self.table_model)
            result = self.__get_data_from_model(result[0], column_name)

            return result
        return 'Query provided: {}\n'.format(query)

    def update(self, instance, session, query=None):
        return 'Query provided: {}\n'.format(query)

    def delete(self, instance, session, query=None):
        return 'Query provided: {}\n'.format(query)
