import click
import json
import os


# File to store to-do items
TODO_FILE = 'todo_list.json'
CONFIG_FILE = 'config/auto_tasking_config.json'


# Load to-do items from file
if os.path.exists(TODO_FILE):
    with open(TODO_FILE, 'r') as file:
        todo_list = json.load(file)
else:
    todo_list = []


# Load auto-tasking configuration from file
if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, 'r') as file:
        auto_tasking_config = json.load(file)
else:
    auto_tasking_config = {"time_based_tasks": [], "template_based_tasks": []}


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


@cli.command()
def auto_task():
    """Automatically generate tasks based on the configuration."""
    generate_time_based_tasks()
    generate_template_based_tasks()
    save_tasks()
    click.echo('Auto-generated tasks have been added to the to-do list.')


def generate_time_based_tasks():
    """Generate tasks based on time-based rules."""
    for task_rule in auto_tasking_config.get("time_based_tasks", []):
        todo_list.append(task_rule["task"])


def generate_template_based_tasks():
    """Generate tasks based on template-based rules."""
    for task in auto_tasking_config.get("template_based_tasks", []):
        todo_list.append(task)


def save_tasks():
    """Save the to-do list to a file."""
    with open(TODO_FILE, 'w') as file:
        json.dump(todo_list, file)


if __name__ == '__main__':
    cli()
