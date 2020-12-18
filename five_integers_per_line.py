#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Nov 2019
# This program prints five integers per line


def main():
    # this function is the the famous Fizz-Buzz problem

    for counter in range(1000, 2000 + 1):
        if counter % 5 != 4:
            print(counter, " ", end="")
        else:
            print(counter)


if __name__ == "__main__":
    main()
