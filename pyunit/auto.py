from widget import Widget
import unittest

#执行测试类

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget=Widget()
    def tearDown(self):
        self.widget.dispoes()
        self.widget=None

#测试getSize()方法的测试用例
    def testSize(self):
        self.assertEqual(self.widget.getSize(),(40,40))
#测试 resize（）方法的测试用例

    def testResize(self):
        self.widget.resize(100,100)
        self.assertEqual(self.widget.getSize(),(100,100))

#测试

if __name__ == '__main__':
    unittest.main()