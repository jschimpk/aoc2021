def part2(input):
    horizontal = 0
    depth = 0
    aim = 0

    for instr in input:
        op, val = instr.split()
        val = int(val)

        if op == 'forward':
            horizontal += val
            depth += aim * val
        elif op == 'down':
            aim += val
        elif op == 'up':
            aim -= val

    print(f'Horizontal: {horizontal}  Depth: {depth}  Aim: {aim}')
    return horizontal * depth


def part1(input):
    horizontal = 0
    depth = 0

    for instr in input:
        op, val = instr.split()
        val = int(val)

        if op == 'forward':
            horizontal += val
        elif op == 'down':
            depth += val
        elif op == 'up':
            depth -= val

    print(f'Horizontal: {horizontal}  Depth: {depth}')
    return horizontal * depth



if __name__ == '__main__':
    filelist = [
        'example.txt',
        'input1.txt',
    ]
    for file in filelist:
        with open(file, 'r') as f:
            input = f.readlines()

        print(f'Input file: {file}')
        print(part1(input))
        print(part2(input))
