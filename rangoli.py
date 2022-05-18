def print_rangoli(size):
    # your code goes here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    n_rows= 1 + 4 * (size - 1)
    n_lines = 1 + 2 * (size - 1)
    for i in range(round(n_lines)):
        if i <= (n_lines - 1) / 2:
            rangoli = '-' * (int((n_rows - 1) / 2) - 2 * i)
            for j in range(i + 1):
                rangoli = rangoli + alphabet[size - j - 1] + '-'
        else:
            rangoli = '-' * (2 * i - int((n_rows - 1) / 2))

        print(rangoli)


if __name__ == '__main__':
    # n = int(input())
    n=5
    print_rangoli(n)