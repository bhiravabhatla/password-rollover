import oracledb

import pkg.create_user as user


def main():
    create_user = user.CreateUser(username="sys", password="oracle",
                                  host="localhost", port=1521, service_name="FREEPDB1",
                                  mode=oracledb.AUTH_MODE_SYSDBA)

    create_user.create_procedure()


if __name__ == "__main__":
    main()