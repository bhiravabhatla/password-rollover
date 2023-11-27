import oracledb.constants
from utils.file_utils import FileUtil
from utils.oracle_utils import OracleClient

SQL_PATH = "sqls"


class CreateUser:
    def __init__(self, host, port, service_name, username, password, mode, protocol="tcp"):
        self.host = host
        self.port = port
        self.service_name = service_name
        self.username = username
        self.password = password
        self.mode = mode
        self.protocol = protocol
        self.client = OracleClient(username=self.username, password=self.password,
                                   host=self.host, port=self.port, service_name=self.service_name,
                                   mode=self.mode, protocol=self.protocol)

    def create_procedure(self):
        file = FileUtil('{}/create_user.sql'.format(SQL_PATH))
        error_query = FileUtil('{}/errors.sql'.format(SQL_PATH))
        create_user_sql = file.get_file_as_str()
        get_errors_sql = error_query.get_file_as_str()

        cursor = self.client.get_conn_cursor()
        cursor.callproc("dbms_output.enable")
        cursor.execute(create_user_sql)
        cursor.execute(get_errors_sql)
        errors = cursor.fetchall()
        if errors:
            for info in errors:
                print("Error at line {} position {}:\n{}".format(*info))
        else:
            print("Created successfully")
        cursor.close()

    def create_users(self):
        cursor = self.client.get_conn_cursor()
        cursor.callproc("dbms_output.enable")



