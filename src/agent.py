import click

# In-memory storage for to-do items
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
        click.echo(f'Task deleted: {removed_task}')
    else:
        click.echo('Invalid task number.')

if __name__ == '__main__':
    cli()
