import io


options = ['Above ground was the medieval settlement of Skaar’s Outpost, '
           'originally a fort to guard the cave entrance. Its inception '
           'as a town had been in the lodging and supply needs of '
           'explorers there to attempt the subterranean labyrinth '
           'when it had opened as a commercial venture. With the caverns’ '
           'flooding and subsequent closure, however, Skaar’s Outpost '
           'had declined into an agricultural community miles from any '
           'trade routes.',
           'wena comparini']


class File:
    def __init__(self, path, mode='r', *args, **kwargs):
        print('wena me abri')
        self.path = path
        if mode in ['w', 'w+', 'wb']:
            self.__text = iter([])
        else:
            self.__text = iter([options[0], options[1]])
        self.mode = None
        self.opened = True

    def __enter__(self):
        print('wena me llame')
        return self

    def __exit__(self, e_type, e_val, e_tb):
        self.close()
        self.__text = None

    def close(self):
        self.opened = False

    def read(self):
        self.__check_open_file()
        self.__check_readable()
        try:
            return '\n'.join(self.__text)
        except Exception:
            raise EOFError('Reached beyond end of file')

    def readline(self):
        self.__check_open_file()
        self.__check_readable()
        try:
            return next(self.__text)
        except Exception:
            raise EOFError('Reached beyond end of file')

    def readlines(self):
        self.__check_open_file()
        self.__check_readable()
        try:
            return [x for x in self.__text]
        except Exception:
            raise EOFError('Reached beyond end of file')

    def __check_open_file(self):
        if not self.opened:
            raise ValueError('I/O operation on closed file.')

    def __check_readable(self):
        if mode in ['w', 'w+', 'wb']:
            raise io.UnsupportedOperation('not readable')


def open(path, *args, **kwargs):
    data = options[0] + '\n' + options[1]
    return File(path, *args, **kwargs)


if __name__ == '__main__':
    file = open('asdf', mode='r')
    print(file.readlines())
    file.close()
    # with open('asdf', mode='r') as file:
    #     print(file.readlines())
