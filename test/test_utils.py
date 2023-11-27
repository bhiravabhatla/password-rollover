import unittest
from utils.file_utils import FileUtil


class UtilsTest(unittest.TestCase):

    def test_get_file_as_str(self):
        file_util = FileUtil('fixtures/test.sql')
        str = file_util.get_file_as_str()
        assert str == "select count(1) from dual;"

    def test_get_file_as_str_error(self):
        file_util = FileUtil('fixtures/dummy.sql')
        self.assertRaises(FileNotFoundError, file_util.get_file_as_str)

    def test_get_file_as_lines(self):
        file_util = FileUtil('fixtures/testdb')
        lines = file_util.get_file_as_lines()
        assert lines == "select count(1) from dual;"

    def test_get_file_as_lines_error(self):
        file_util = FileUtil('fixtures/dummydb')
        self.assertRaises(FileNotFoundError, file_util.get_file_as_str)


if __name__ == '__main__':
    unittest.main()