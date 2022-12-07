from python.download_input import get_input_content


def get_file_structure():
    return {'parent': None, 'files': [], 'directories': []}


filesystem = {'/': get_file_structure()}
filesystem_size = 70000000


def process(position, s):
    total_size = sum(file['size'] for file in filesystem[position]['files'])
    for subdirectory in filesystem[position]['directories']:
        subdirectory_total_size, s = process(subdirectory, s)
        total_size += subdirectory_total_size
    if total_size < 100000:
        s += total_size
    return total_size, s


def process_2(position, options, unused_space):
    total_size = sum(file['size'] for file in filesystem[position]['files'])
    for subdirectory in filesystem[position]['directories']:
        subdirectory_total_size, options = process_2(subdirectory, options, unused_space)
        total_size += subdirectory_total_size
    if unused_space + total_size > 30000000:
        options.append(total_size)
    return total_size, options


def first(data):
    position = ''

    for line in data:
        if line.startswith('$'):
            if ' cd ' in line:
                directory = line.split()[-1]
                if directory == '..':
                    position = '/'.join(position.split('/')[:-2]) + '/'
                elif directory == '/':
                    position = '/'
                else:
                    position = f'{position}{directory}/'
        else:
            if line.startswith('dir'):
                subdirectory = line.split()[-1]
                filesystem[position]['directories'].append(f'{position}{subdirectory}/')
                filesystem[f'{position}{subdirectory}/'] = get_file_structure()
            else:
                size, filename = line.split()
                filesystem[position]['files'].append({'name': filename, 'size': int(size)})

    s = 0
    total_size, s = process('/', s)
    return s


def second():
    unused_space = filesystem_size - process('/', 0)[0]

    options = []
    total_size, options = process_2('/', options, unused_space)
    return min(options)


if __name__ == "__main__":
    content = get_input_content(__file__)

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second()}')
