# encoding: utf-8
from datetime import datetime, time


def create_task(name, due_date, required_time):
    return dict(name=name,
                due_date=due_date,
                required_time=required_time,
                finished=False)


def format_task(task):
    state = 'finished' if task['finished'] else 'unfinished'
    format = "{state} {task[name]}: \
            untill {task[due_date]:%Y-%m-%d} \
            required time:{task[required_time]} minutes"

    return format.format(task=task, state=state)


def finish_task(task):
    task['finished'] = True


# How to use

# from task import *
# task = create_task('learn python', datetime(2012, 4, 2), time(0, 25))
# format_task(task)
# finish_task(task)
# format(task)
