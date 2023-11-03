import unittest
import py_version_tool.version
import os


class MyTestCase(unittest.TestCase):
    init_version = {"major": 0, "minor": 0, "patch": 0}
    def setUp(self):
        py_version_tool.version._write_version(self.init_version)
    def tearDown(self):
        #delete version.json
        #function to delete version.json
        if os.path.exists('version.json'):
            os.remove('version.json')
        pass
    def test_teardown(self):
        self.tearDown()
        #check if version.json exists
        #function to check if version.json exists
        def check_version_file(filename='version.json'):
            if os.path.exists(filename):
                return True
            else:
                return False
            
    def test_read_version(self):
        self.setUp()
        self.tearDown()
        self.assertEqual(py_version_tool.version._read_version(), self.init_version)
        self.tearDown()
        pass
    def test_set_version(self):
        self.setUp()
        self.assertEqual(py_version_tool.version._read_version(), self.init_version)
    def test_increment_version_patch(self):
        self.setUp()
        py_version_tool.version.increment_version("patch")
        self.assertEqual(py_version_tool.version._read_version(), {"major": 0, "minor": 0, "patch": 1})
    def test_increment_version_minor(self):
        self.setUp()
        py_version_tool.version.increment_version("minor")
        self.assertEqual(py_version_tool.version._read_version(), {"major": 0, "minor": 1, "patch": 0})
    def test_increment_version_major(self):
        self.setUp()
        py_version_tool.version.increment_version("major")
        self.assertEqual(py_version_tool.version._read_version(), {"major": 1, "minor": 0, "patch": 0})




if __name__ == '__main__':
    unittest.main()

