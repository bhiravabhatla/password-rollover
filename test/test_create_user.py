import unittest
from unittest.mock import patch


import pkg.create_user as user


class CreateUserTest(unittest.TestCase):
    @patch('utils.oracle_utils.OracleClient.get_conn_cursor')
    def test_create_user_procedure(self, mock):
        test_create_user = user.CreateUser()
        pkg.create_user.create_user_procedure()
        mock.assert_called()

if __name__ == '__main__':
    unittest.main()