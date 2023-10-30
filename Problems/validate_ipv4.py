"""Validate IPv4 address.
A program to check whether a provided address is a valid IPv4 address."""

import re


def validate_ipv4(address: str) -> bool:
    octets = address.split('.')

    if len(octets) != 4:
        return False

    for octet in octets:
        if not octet.isdigit() or not 0 <= int(octet) <= 255:
            return False

    if int(octets[0]) == 0 or int(octets[0]) >= 223 or int(octets[-1]) == 255:
        return False

    return True


def main() -> None:

    print('Enter an IPv4 address to check if it\'s valid:')
    response = input('> ')

    if (re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', response) and
            validate_ipv4(response)):
        print('Valid')
    else:
        print('Invalid')


if __name__ == '__main__':
    main()
