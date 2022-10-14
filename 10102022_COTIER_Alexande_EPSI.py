# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def hello(name):
    # Use a breakpoint in the code line below to debug your script.
    mot = ["es gentil", "es méchant", "pues", "bois du coca"]  # Press Ctrl+F8 to toggle the breakpoint.
    print(f"salut, {name}, tu {mot[random.randint(0, len(mot) - 1)]}")

def change(a,b):
    print('a:',a);
    print('b:', b);
    a, b = b, a
    print('a:', a);
    print('b:', b);

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hello('Damien')
    change(1, 2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
