def print_hi(name):
    print(f'Hi, {name}')


def print_reversed(stroke):
    print(stroke[::-1])


if __name__ == 'main':
    for i in range(100):
        for j in range(100):
            print(i,j)
        print('end of the j counter')

    s = input()
    print_reversed(s)