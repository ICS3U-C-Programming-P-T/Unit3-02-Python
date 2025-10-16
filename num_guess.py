#!/usr/bin/env python3
# Created by: Patrick
# Created on: 10/16/2025


def main():
    # Ask the user to pick a number from 1 to 6
    user_number = float(input("Pick a number from 1 to 6: "))

    # Check if the user's number is equal to the correct number
    if user_number == (6):
        print("Congrats you picked the correct number")

    # If other wrong
    if user_number == (1):
        print("Wrong")


if __name__ == "__main__":
    main()
