class StackException(Exception):
    pass


class Stack:

    def __init__(self, data_type):
        self.stack = []
        self.type = data_type

    def push(self, item):
        if not isinstance(item, self.type) and not issubclass(type(item), self.type):
            raise StackException()
        else:
            self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            raise StackException()
        else:
            last_item = self.stack[-1]
            self.stack = self.stack[:-1]
            return last_item

    def is_empty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)
