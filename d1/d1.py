def part2(input):
    increase_count = 0
    for i in range(0, len(input)-3):
        if sum(input[i:i+3]) < sum(input[i+1:i+4]):
            increase_count += 1

    return increase_count


def part1(input):
     increase_count = 0
     for i in range(1, len(input)):
         if input[i-1] < input[i]:
             increase_count += 1

     print(f'Found {increase_count} increases.')


if __name__ == '__main__':
    files = [
        'example.txt',
        'input1.txt'
    ]
    for file in files:
        with open (file, 'r') as f:
            input = [int(x) for x in f.read().split()]

        print(f'Running {file}:')
        part1(input)
        print(part2(input))
