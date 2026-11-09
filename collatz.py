def collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def main():
    sequence = collatz(27)
    for number in sequence:
        print(number)
    print(f"Total steps: {len(sequence) - 1}")


if __name__ == "__main__":
    main()
