import select
import time
import sys
import termios

fd = sys.stdin.fileno()
old_term = termios.tcgetattr(fd)  # (For restoring later.)

new_term = termios.tcgetattr(fd)
new_term[3] = (new_term[3] & ~termios.ICANON & ~termios.ECHO)
termios.tcsetattr(fd, termios.TCSAFLUSH, new_term)

def kbhit():
    results = select.select([sys.stdin], [], [], 0)
    return results[0] != []

def getch():
   ch = sys.stdin.read(1)
   return ch

def timed_input(caption, timeout=0.1):
    def echo(c):
        sys.stdout.write(c)
        sys.stdout.flush()        

    echo(caption)

    _input = []
    start = time.monotonic()
    while time.monotonic() - start < timeout:
        if kbhit():
            c = getch()
            if ord(c) == 13:
                echo('\r\n')
                break
            _input.append(c)
            echo(c)

    if _input:
        return ''.join(_input)


# while True:
#     v = timed_input('Введите что-нибудь за 5 секунд\n')
#     print('Вы ввели:', v)