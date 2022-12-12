import sys
from datetime import datetime
from os import makedirs
from os.path import exists
from shutil import copyfile


def main(args):
    day = int(args[1]) if len(args) > 1 else datetime.today().day
    year = int(args[2]) if len(args) > 2 else datetime.today().year

    if not exists(str(year)):
        print(f'Create new year {year}')
        makedirs(str(year))

    if not exists(f'{year}/day{day}'):
        print(f'Create new day {day} for year {year}')
        makedirs(f'{year}/day{day}')

    filename = f'{year}/day{day}/day{day}.py'
    if exists(filename):
        print(f'Day {day} for year {year} already exists')
    else:
        copyfile('template.py', filename)


if __name__ == '__main__':
    main(sys.argv)
