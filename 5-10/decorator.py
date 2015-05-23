def show_message(text='function called'):
    def decorate(f):
        def wrapper():
            print(text)
            return f()

        return wrapper

    return decorate


@show_message('with args')
def spam1():
    print('spam1 called')


spam1()
