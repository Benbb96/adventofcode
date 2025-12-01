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

    folder_path = f'{year}/{str(day).zfill(2)}'
    if not exists(folder_path):
        print(f'Create new day {day} for year {year}')
        makedirs(folder_path)

    filename = f'{folder_path}/main.py'
    if exists(filename):
        print(f'Day {day} for year {year} already exists')
    else:
        copyfile('template.py', filename)


if __name__ == '__main__':
    main(sys.argv)
