import re
import requests

from dotenv import load_dotenv
from os import getenv
from os.path import exists, abspath, dirname, basename
from typing import Union

load_dotenv()


def get_input_content(file: str, split_by_lines: bool = True) -> Union[list[str], str]:
    input_filename = 'input.txt'
    # Get input file if it doesn't already exist
    if not exists(input_filename):
        # Get day and year from path of the file
        day = basename(dirname(abspath(file)))
        day = int(re.findall(r'\d+', day)[0])
        year = basename(dirname(dirname(abspath(file))))
        response = requests.get(
            f'https://adventofcode.com/{year}/day/{day}/input',
            cookies={'session': getenv('SESSION_ID')},
            headers={'User-Agent': 'github.com/benbb96/adventofcode by benbb96@gmail.com'}
        )
        print(f'Download {input_filename}: {response.status_code} [{response.reason}]')
        if response.status_code == 200:
            with open(input_filename, 'w') as f:
                f.write(response.text)
        else:
            print(response.text)
            raise Exception(f"Impossible de télécharger l'input. Erreur {response.status_code}")

    # Read content of the input and create a list of the striped lines
    with open(input_filename, 'r') as f:
        if split_by_lines:
            content = [x.strip() for x in f.readlines()]
        else:
            content = f.read().strip()

    return content
