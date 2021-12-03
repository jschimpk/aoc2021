def o2_most_common(column):
    return '1' if column.count('1') >= column.count('0') else '0'


def co2_least_common(column):
    return '0' if column.count('0') <= column.count('1') else '1'


def get_cropped_list(input, i, val):
    output = []
    for line in input:
        if line[i] == val:
            output.append(line)

    return output


def get_column(input, i):
    column = ''
    for line in input:
        column += line[i]

    return column


def part2_old(input):
    input_o2 = input.copy()
    input_co2 = input.copy()

    for i in range(0,len(input_o2[0])):
        column = get_column(input_o2, i)
        most_common = '1' if column.count('1') >= column.count('0') else '0'
        input_o2 = get_cropped_list(input_o2, i, most_common)

        if len(input_o2) == 1:
            o2 = input_o2[0]
            break

    for i in range(0,len(input_co2[0])):
        column = get_column(input_co2, i)
        least_common = '0' if column.count('0') <= column.count('1') else '1'
        input_co2 = get_cropped_list(input_co2, i, least_common)

        if len(input_co2) == 1:
            co2 = input_co2[0]
            break

    scrubber = int(o2, 2) * int(co2, 2)
    print(f'o2: {o2} ({int(o2, 2)})   co2: {co2} ({int(co2, 2)})   scrubber: {scrubber}')


def part2(input):
    answers = []
    for this_input, common_check in zip([input.copy(), input.copy()], [o2_most_common, co2_least_common]):
        for i in range(0, len(this_input[0])):
            column = get_column(this_input, i)
            common = common_check(column)
            this_input = get_cropped_list(this_input, i, common)
            if len(this_input) == 1:
                answers.append(this_input[0])
                break

    o2, co2 = answers
    scrubber = int(o2, 2) * int(co2, 2)

    print(f'o2: {o2} ({int(o2, 2)})   co2: {co2} ({int(co2, 2)})   scrubber: {scrubber}')

    return scrubber


def part1(input):
    gamma = ''
    epsilon = ''

    for i in range(0,len(input[0])):
        column = get_column(input, i)
        gamma += '0' if column.count('0') > column.count('1') else '1'
        epsilon += '0' if gamma[i] == '1' else '1'

    power = int(gamma, 2) * int(epsilon, 2)
    print(f'gamma: {gamma} ({int(gamma, 2)})   epsilon: {epsilon} ({int(epsilon, 2)})   power: {power}')

    return power


if __name__ == '__main__':
    files = [
        'example.txt',
        'input1.txt',
    ]
    for file in files:
        with open(file, 'r') as f:
            input = f.read().split()
            print(f'Processing file: {file}')
            answer = part1(input)
            print(f'The answer for part1 is: {answer}')

            answer = part2(input)
            print(f'The answer for part2 is: {answer}')
