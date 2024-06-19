import click

tasks = []

@click.group()
def cli():
    """A simple CLI for managing tasks."""
    pass


@click.command()
@click.argument('task')
def add(task):
    """Add a new task."""
    tasks.append(task)
    click.echo(f'Task added: {task}')


@click.command()
def view():
    """View all tasks."""
    if tasks:
        click.echo('Tasks:')
        for i, task in enumerate(tasks, 1):
            click.echo(f'{i}. {task}')
    else:
        click.echo('No tasks found.')


@click.command()
@click.argument('task_number', type=int)
def delete(task_number):
    """Delete a task by its number."""
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        click.echo(f'Task deleted: {removed_task}')
    else:
        click.echo('Invalid task number.')


cli.add_command(add)
cli.add_command(view)
cli.add_command(delete)


if __name__ == '__main__':
    cli()
