from datetime import datetime, time


def create_task(name, due_date, required_time):
    return dict(name=name,
                due_date=due_date,
                required_time=required_time,
                finished=False)


# create_task('learn python', datetime(2012, 4, 2), time(0, 25))
# { 'due_date': datetime.datetime(2012, 4, 2, 0, 0),
#   'finished': False,
#   'required_time': datetime.time(0, 25),
#   'name': 'learn python' }
