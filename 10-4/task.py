#!/Users/yuhoshino/.pyenv/shims/python
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


import argparse


def cmd_add(args):
    name = raw_input('task name:')
    due_date = datetime.strptime(raw_input('due date [Y-m-d]:'), '%Y-%m-%d')
    required_time = int(input('required_time:'))

    task = create_task(name, due_date, required_time)
    add_task(args.db, task)


def cmd_list(args):
    if args.all:
        tasks = all_task(args.db)
    else:
        tasks = unfinished_tasks(args.db)

    for key, task in tasks:
        print("{0} {1}".format(key, format_task(task)))


def cmd_finish(args):
    task = args.db[args.task]
    finish_task(task)
    args.db[args.task] = task


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('shelve')

    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser('add')
    add_parser.set_defaults(func=cmd_add)

    list_parser = subparsers.add_parser('list')
    list_parser.add_argument('-a', '--all', action='store_true')
    list_parser.set_defaults(func=cmd_list)

    finish_parser = subparsers.add_parser('finish')
    finish_parser.add_argument('task')
    finish_parser.set_defaults(func=cmd_finish)

    args = parser.parse_args()

    db = shelve.open(args.shelve, 'c')

    try:
        args.db = db
        if hasattr(args, 'func'):
            args.func(args)
        else:
            parser.print_help()
    finally:
        db.close()


if __name__ == '__main__':
    main()

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


# CLI
# $ ./task.py task_data add
# $ ./task.py task_data list
# $ ./task.py task_data finish task:0
# $ ./task.py task_data list # hides finished tasks
# $ ./task.py task_data list -a # shows all tasks including finished tasks
