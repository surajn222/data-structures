# Print all numbers upto 5
# Print all 2 digit binary numbers

def print_bin1(total):
    total += 1
    print(total)
    print_bin2(total)


def print_bin2(total):
    total += 1
    print(total)
    print_bin3(total)


def print_bin3(total):
    total += 1
    print(total)
    print_bin4(total)


def print_bin4(total):
    if total == 4:
        return

print_bin1(0)