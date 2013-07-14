from config import *

class Database(object):
    def __init__(self, db_type=db_type, db_name=db_name, 
                   user_name = user_name, interface='localhost', db_passwd=''):
        self.db_type = db_type
        self.db_name = db_name
        self.db_passwd = db_passwd

        if self.db_type == 'mysql':
            try:
                import MySQLdb as db
            except ImportError:
                print "[fatal] python: can't import MySQLdb\n"
            try:
                self.con = db.connect(interface, user_name, db_passwd, self.db_name)
            except:
                print "[fatal] can't connect to the database\n"
        else:
            print "[columbus] DATABASE: sorry this database type %s is currently not supported\n" \
                       % self.db_type

    def execute(self, table, action, data):
        if action == 'create':
            cur = self.con.cursor()
            cur.execute("insert into %s values %s" % (table, repr(tuple(data))))
            self.con.commit()
        else:
            print "[columbus] DATABASE: this action %s is currrently not supported\n" % action

    def close(self):
        self.con.close()