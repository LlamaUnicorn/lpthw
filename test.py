import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {(end - start):.6f} seconds to execute.")
        return result
    return wrapper

thai_girls = [
    'Nongnuch', 'Sirikul', 'Arisa', 'Anchalee', 'Pitchapa', 'Napaporn', 'Pimchanok', 'Thanaporn', 'Suthida', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Wasana', 'Nongnuch', 'Sirikul', 'Arisa', 'Anchalee', 'Pitchapa', 'Napaporn','Nongnuch', 'Sirikul', 'Arisa', 'Anchalee', 'Pitchapa', 'Napaporn','Nongnuch', 'Sirikul', 'Arisa', 'Anchalee', 'Pitchapa', 'Napaporn','Nongnuch', 'Sirikul', 'Arisa', 'Anchalee', 'Pitchapa', 'Napaporn',]

with_dick = []

@timer
def list_iterator(thai_girls):
    for person in thai_girls:
        if person not in with_dick:
            with_dick.append(person)
    return with_dick


@timer
def list_comprehension(thai_girls):
    with_dick2 = []
    return [person for person in thai_girls if person not in with_dick2]


@timer
def set_func(thai_girls):
    return list(set(thai_girls))


list_iterator(thai_girls)
list_comprehension(thai_girls)
set_func(thai_girls)
print(set_func(thai_girls))
