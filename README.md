# To-dolist-agent

## Overview

The To-dolist-agent is a command-line tool designed to help you manage your to-do list efficiently. It allows you to add, remove, and view tasks, as well as automatically generate tasks based on predefined rules.

## Features

- Add tasks to your to-do list
- Remove tasks from your to-do list
- View all tasks in your to-do list
- Automatically generate tasks based on time-based and template-based rules

## Installation

To install the To-dolist-agent, clone the repository and install the required dependencies:

```bash
git clone https://github.com/VishwamAI/To-dolist-agent.git
cd To-dolist-agent
pip install -r requirements.txt
```

## Usage

### Adding a Task

To add a task to your to-do list, use the `add` command followed by the task description:

```bash
python src/agent.py add "Buy groceries"
```

### Removing a Task

To remove a task from your to-do list, use the `remove` command followed by the task number:

```bash
python src/agent.py remove 1
```

### Viewing Tasks

To view all tasks in your to-do list, use the `view` command:

```bash
python src/agent.py view
```

### Auto-Tasking

The To-dolist-agent can automatically generate tasks based on predefined rules specified in the `config/auto_tasking_config.json` file. To generate tasks automatically, use the `auto_task` command:

```bash
python src/agent.py auto_task
```

#### Configuration

The `config/auto_tasking_config.json` file defines the rules for auto-generated tasks. It includes time-based tasks and template-based tasks. Here is an example configuration:

```json
{
    "time_based_tasks": [
        {
            "frequency": "daily",
            "task": "Review daily goals"
        },
        {
            "frequency": "weekly",
            "task": "Plan weekly schedule"
        }
    ],
    "template_based_tasks": [
        "Buy groceries",
        "Clean the house",
        "Exercise for 30 minutes"
    ]
}
```
[![Python application](https://github.com/VishwamAI/To-dolist-agent/actions/workflows/python-app.yml/badge.svg)](https://github.com/VishwamAI/To-dolist-agent/actions/workflows/python-app.yml)

You can modify this file to define your own rules for auto-generated tasks.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Update

This is a trivial update to trigger a new CI/CD workflow run.
