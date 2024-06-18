import unittest
from click.testing import CliRunner
from src.agent import cli, todo_list

class TestTodoListAgent(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def tearDown(self):
        todo_list.clear()

    def test_add_task(self):
        result = self.runner.invoke(cli, ['add', 'Test task'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Task added: Test task', result.output)
        self.assertIn('Test task', todo_list)

    def test_view_tasks(self):
        todo_list.append('Test task 1')
        todo_list.append('Test task 2')
        result = self.runner.invoke(cli, ['view'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('1. Test task 1', result.output)
        self.assertIn('2. Test task 2', result.output)

    def test_delete_task(self):
        todo_list.append('Test task')
        result = self.runner.invoke(cli, ['delete', '1'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Task deleted: Test task', result.output)
        self.assertNotIn('Test task', todo_list)

    def test_delete_invalid_task(self):
        result = self.runner.invoke(cli, ['delete', '1'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Invalid task number.', result.output)

if __name__ == '__main__':
    unittest.main()
