import click
import json
import os


# File to store to-do items
TODO_FILE = 'todo_list.json'


# Load to-do items from file
if os.path.exists(TODO_FILE):
    with open(TODO_FILE, 'r') as file:
        todo_list = json.load(file)
else:
    todo_list = []


@click.group()
def cli():
    """A simple CLI for managing a to-do list."""
    pass


@cli.command()
@click.argument('task')
def add(task):
    """Add a new task to the to-do list."""
    todo_list.append(task)
    save_tasks()
    click.echo(f'Task added: {task}')


@cli.command()
def view():
    """View all tasks in the to-do list."""
    if not todo_list:
        click.echo('No tasks in the to-do list.')
    else:
        click.echo('To-do list:')
        for idx, task in enumerate(todo_list, 1):
            click.echo(f'{idx}. {task}')


@cli.command()
@click.argument('task_number', type=int)
def delete(task_number):
    """Delete a task from the to-do list by its number."""
    if 0 < task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        save_tasks()
        click.echo(f'Task deleted: {removed_task}')
    else:
        click.echo('Invalid task number.')


def save_tasks():
    """Save the to-do list to a file."""
    with open(TODO_FILE, 'w') as file:
        json.dump(todo_list, file)


if __name__ == '__main__':
    cli()
