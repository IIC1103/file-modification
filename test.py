import marshal
import random
import os


def override_open(opt1, opt2):

    import sys  # noqa: F401
    import io  # noqa: F401

    options = ['Above ground was the medieval settlement of Skaars Outpost, '
               'originally a fort to guard the cave entrance. Its inception '
               'as a town had been in the lodging and supply needs of '
               'explorers there to attempt the subterranean labyrinth '
               'when it had opened as a commercial venture. With the caverns '
               'flooding and subsequent closure, however, Skaars Outpost '
               'had declined into an agricultural community miles from any '
               'trade routes.',
               'Muy lejos, mas alla de las montanas de palabras, alejados de '
               'los paises de las vocales y las consonantes, viven los textos '
               'simulados. Viven aislados en casas de letras, en la costa de '
               'la semantica, un gran oceano de lenguas. Un riachuelo llamado'
               ' Pons fluye por su pueblo y los abastece con las normas '
               'necesarias.', 'Hablamos de un pais paraisomatico en el que a '
               'uno le caen pedazos de frases asadas en la boca. Ni siquiera '
               'los todopoderosos signos de puntuacion dominan a los textos'
               ' simulados; una vida, se puede decir, poco ortografica. '
               'Pero un buen dia, una pequena linea de texto simulado, llamada'
               ' Lorem Ipsum, decidio aventurarse y salir al vasto mundo de '
               'la gramatica.', ' El gran Oxmox le desanconsejo hacerlo, ya '
               'que esas tierras estaban llenas de comas malvadas, signos de '
               'interrogacion salvajes y puntos y coma traicioneros, pero el '
               'texto simulado no se dejo atemorizar. Empaco sus siete '
               'versales, enfundo su inicial en el cinturon y se puso en '
               'camino.', 'Cuando ya habia escalado las primeras colinas de '
               'las montanas cursivas, se dio media vuelta para dirigir su '
               'mirada por ultima vez, hacia su ciudad natal Letralandia, el'
               ' encabezamiento del pueblo Alfabeto y el subtitulo de su '
               'camino.'
               ]

    class File:
        def __init__(self, path, data, mode='r', *args, **kwargs):
            self.path = path
            if mode in ['w', 'w+', 'wb']:
                self.__text = iter([])
            else:
                self.__text = iter(data.splitlines())
            self.__written_text = ''
            self.mode = mode
            self.opened = True
            self.SALT = 1103

        def __enter__(self):
            return self

        def __exit__(self, e_type, e_val, e_tb):
            self.close()

        def __iter__(self):
            return self.__text

        def close(self):
            self.opened = False

            if self.mode in ['w', 'w+', 'wb']:
                self.__text = iter(self.__written_text.splitlines())

        def write(self, text):
            self.__check_writeable()

            self.__written_text = text

        def writeline(self, line):
            self.__check_writeable()
            self.__written_text += f'\n{line}'

        def writelines(self, lines):
            self.__check_writeable()
            self.__written_text += '\n'.join(lines)

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

        def reveal(self):

            return (self.SALT * len(self.__written_text),
                    self.__written_text == '\n'.join(self.__text))

        def __check_open_file(self):
            if not self.opened:
                raise ValueError('I/O operation on closed file.')

        def __check_readable(self):
            if self.mode in ['w', 'w+', 'wb']:
                raise io.UnsupportedOperation('not readable')

        def __check_writeable(self):
            if self.mode not in ['w', 'w+']:
                raise io.UnsupportedOperation('not writeable')

    def my_open(path, *args, **kwargs):
        if path != 'archivo.txt':
            raise FileNotFoundError(f'File not found')

        data = options[opt1] + '\n' + options[opt2]

        f = File(path, data, *args, **kwargs)

        main_module = sys.modules[__name__]
        setattr(main_module, 'reveal', f.reveal)

        return f

    main_module = sys.modules[__name__]
    setattr(main_module, 'open', my_open)


# code = override_open.__code__
# curdir = os.getcwd()
# os.chdir(os.path.expanduser('~'))
# print(marshal.dumps(code))
# print(random.randint(0, 4), random.randint(0, 4))
# os.chdir(curdir)


if __name__ == '__main__':

    override_open(1, 2)
    file = open('archivo.txt', mode='r')
    print(file.read())
    file.close()
    print(*reveal(), sep='\n')
    # with open('asdf', mode='r') as file:
    #     print(file.readlines())
