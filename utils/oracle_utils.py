from oracledb import connect_params, connection


class OracleClient:
    def __init__(self, host, port, service_name, username, password, mode, protocol):
        self.host = host
        self.port = port
        self.service_name = service_name
        self.username = username
        self.password = password
        self.mode = mode
        self.protocol = protocol

    def get_conn_cursor(self):
        params = connect_params.ConnectParams(user=self.username, password=self.password,
                                              host=self.host, port=self.port,
                                              protocol=self.protocol, service_name=self.service_name,
                                              mode=self.mode
                                              )
        oracle_connection = connection.connect(params=params)
        return oracle_connection.cursor()


def get_server_output(cursor, chunk_size):

    lines_var = cursor.arrayvar(str, chunk_size)
    num_lines_var = cursor.var(int)
    num_lines_var.setvalue(0, chunk_size)

    while True:
        cursor.callproc("dbms_output.get_lines", (lines_var, num_lines_var))
        num_lines = num_lines_var.getvalue()
        lines = lines_var.getvalue()[:num_lines]
        for line in lines:
            print(line or "")
        if num_lines < chunk_size:
            break
