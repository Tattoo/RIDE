import unittest
from robotide.controller.cellinfo import CellInfo, CellContent, ContentType,\
    CellPosition, CellType, TipMessage
from robot.utils.asserts import assert_false, assert_equals, assert_true


class Test(unittest.TestCase):

    def test_empty_tooltip(self):
        cell = CellInfo(CellContent(ContentType.EMPTY, None, None), 
                        CellPosition(CellType.UNKNOWN, None))
        assert_false(TipMessage(cell))

    def test_unknown_keyword(self):
        cell = CellInfo(CellContent(ContentType.STRING, 'What?', None), 
                        CellPosition(CellType.KEYWORD, None))
        msg = TipMessage(cell)
        assert_true(msg)
        assert_equals(str(msg), msg.KEYWORD_NOT_FOUND)

    def test_known_keyword(self):
        cell = CellInfo(CellContent(ContentType.USER_KEYWORD, 'Known', 'my_source'), 
                        CellPosition(CellType.KEYWORD, None))
        msg = TipMessage(cell)
        assert_true(msg)
        assert_equals(str(msg), msg.KEYWORD % 'my_source')

    def test_for_loop_start(self):
        cell = CellInfo(CellContent(ContentType.STRING, ':FOR', None), 
                        CellPosition(CellType.MANDATORY, None), for_loop=True)
        assert_false(TipMessage(cell))

    def test_for_loop_var(self):
        cell = CellInfo(CellContent(ContentType.VARIABLE, '${i}', None), 
                        CellPosition(CellType.MANDATORY, None), for_loop=True)
        assert_false(TipMessage(cell))

    def test_for_loop_too_many_args(self):
        cell = CellInfo(CellContent(ContentType.STRING, 'something', None), 
                        CellPosition(CellType.MUST_BE_EMPTY, None), for_loop=True)
        msg = TipMessage(cell)
        assert_true(msg)
        assert_equals(str(msg), msg.TOO_MANY_ARGUMENTS)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()