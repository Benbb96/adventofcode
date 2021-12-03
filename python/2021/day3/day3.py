from python.download_input import get_input_content


def first(data):
    gamma_rate = ''
    epsilon_rate = ''
    for col in range(len(data[0])):
        column = ''.join(d[col] for d in data)
        count1 = column.count('1')
        count0 = column.count('0')
        gamma_rate += '1' if count1 > count0 else '0'
        epsilon_rate += '0' if count1 > count0 else '1'
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def second(data):
    oxygen_generator_rating = None
    co2_scrubber_rating = None
    oxygen_generator_rating_data = data.copy()
    co2_scrubber_rating_data = data.copy()

    for col in range(len(data[0])):
        # Oxygen
        column = ''.join(d[col] for d in oxygen_generator_rating_data)
        count1 = column.count('1')
        count0 = column.count('0')
        filter_value = '1' if count1 >= count0 else '0'
        oxygen_generator_rating_data = list(filter(lambda y: y[col] == filter_value, oxygen_generator_rating_data))
        if len(oxygen_generator_rating_data) == 1:
            oxygen_generator_rating = oxygen_generator_rating_data[0]

        # CO2
        column = ''.join(d[col] for d in co2_scrubber_rating_data)
        count1 = column.count('1')
        count0 = column.count('0')
        filter_value = '0' if count0 <= count1 else '1'
        co2_scrubber_rating_data = list(filter(lambda y: y[col] == filter_value, co2_scrubber_rating_data))
        if len(co2_scrubber_rating_data) == 1:
            co2_scrubber_rating = co2_scrubber_rating_data[0]

    return int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)


if __name__ == "__main__":
    content = get_input_content(__file__)

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
