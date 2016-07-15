import sqlalchemy as sa


class DatabaseManager:
    """ Wrapper around sqlalchemy core to handle database interactions """

    COMMASPACE = ', '

    def __init__(self, config):
        """ Instantiate an object of DatabaseManager """

        self.dialect = config.get('dialect')
        self.server = config.get('server')
        self.database = config.get('database')
        self.user = config.get('user')
        self.__pwd = config.get('password')

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
