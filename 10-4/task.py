#!/Users/yuhoshino/.pyenv/shims/python3
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


import pickle


def save_task(task, file):
    pickle.dump(task, file)


def load_tasks(file):
    return pickle.load(file)


import shelve

db = shelve.open('data_store', 'c')


def next_task_name(db):
    id = db.get('next_id', 0)
    db['next_id'] = id + 1
    return "task:{0}".format(id)


def add_task(db, task):
    key = next_task_name(db)
    db[key] = task


def all_task(db):
    for key in db:
        if key.startswith('task:'):
            yield key, db[key]


def unfinished_tasks(db):
    return ((key, task)
            for key, task in all_task(db)
            if not task['finished'])


# How to use

# from task import *
# task = create_task('learn python', datetime(2012, 4, 2), time(0, 25))
# format_task(task)
# finish_task(task)
# format(task)

# from io import BytesIO
# out = BytesIO()
# save_task(tasks, out)
# out.seek(0)
# load_tasks(out)

# add_task(db, task)
# all_task(db)
# unfinished_tasks(db

# next_task_name(db)
