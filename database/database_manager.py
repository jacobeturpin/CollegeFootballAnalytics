""" Handle interactions with database to add/retrieve statistical data """

import sqlalchemy as sa
from configparser import ConfigParser


class DatabaseManager:
    """ Wrapper around sqlalchemy core to handle database interactions """

    COMMASPACE = ', '

    def __init__(self):
        """ Instantiate an object of DatabaseManager """

        with ConfigParser() as parser:
            self.dialect = parser.get('dialect')
            self.server = parser.get('server')
            self.database = parser.get('database')
            self.user = parser.get('user')
            self.__pwd = parser.get('password')

        conn_string = str.format('{}://{}:{}@{}/{}', self.dialect, self.user, self.__pwd,
                                 self.server, self.database)
        self.engine = sa.create_engine(conn_string)

    def add_rows_to_table(self, table_name, vals):
        """ Generic method to add rows to a specified table """

        with self.engine.connect() as connection:
            with connection.begin() as transaction:
                try:
                    rows = self.COMMASPACE.join('?' * len(vals[0]))
                    ins = 'INSERT INTO {tablename} VALUES ({markers})'
                    ins = ins.format(tablename=table_name, markers=rows)
                    connection.execute(ins, vals)
                except Exception as e:
                    transaction.rollback()
                    raise e
                else:
                    transaction.commit()

    def select_all_from_table(self, table_name):
        """ Retrieves all rows from a specified table """

        with self.engine.connect() as connection:
            return connection.execute('SELECT * FROM ?', table_name).fetchall()
