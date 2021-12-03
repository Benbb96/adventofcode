import re
import requests

from dotenv import load_dotenv
from os import getenv
from os.path import exists, abspath, dirname, basename

load_dotenv()


def get_input_content(file):
    input_filename = 'input.txt'
    # Get input file if it doesn't already exist
    if not exists(input_filename):
        # Get day and year from path of the file
        day = basename(dirname(abspath(file)))
        day = re.findall(r'\d+', day)[0]
        year = basename(dirname(dirname(abspath(file))))
        response = requests.get(
            f'https://adventofcode.com/{year}/day/{day}/input',
            cookies={'session': getenv('SESSION_ID')}
        )
        print(f'Download {input_filename}: {response.status_code} [{response.reason}]')
        if response.status_code == 200:
            with open(input_filename, 'w') as f:
                f.write(response.text)
        else:
            raise Exception("Impossible de télécharger l'input")

    # Read content of the input and create a list of the striped lines
    with open(input_filename, 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    return content