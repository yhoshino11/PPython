def show_message(f):
    def wrapper():
        print('function called')
        return f()

    return wrapper


@show_message
def spam1():
    print('spam1 called')


@show_message
def spam2():
    print('spam2 called')


spam1()
spam2()
