import io
import unittest
from contextlib import redirect_stdout

import todo


class TodoDoneTest(unittest.TestCase):
    def setUp(self):
        todo.TODOS.clear()

    def capture_done(self, index_text):
        output = io.StringIO()
        with redirect_stdout(output):
            todo.done(index_text)
        return output.getvalue().strip()

    def test_done_removes_todo_by_one_based_number(self):
        todo.TODOS.extend(["写文章", "发布"])

        output = self.capture_done("1")

        self.assertEqual(output, "已完成：写文章")
        self.assertEqual(todo.TODOS, ["发布"])

    def test_done_out_of_range_prints_friendly_message(self):
        todo.TODOS.append("写文章")

        output = self.capture_done("2")

        self.assertEqual(output, "序号超出范围。")
        self.assertEqual(todo.TODOS, ["写文章"])

    def test_done_non_numeric_prints_friendly_message(self):
        todo.TODOS.append("写文章")

        output = self.capture_done("abc")

        self.assertEqual(output, "请输入数字序号。")
        self.assertEqual(todo.TODOS, ["写文章"])


if __name__ == "__main__":
    unittest.main()
