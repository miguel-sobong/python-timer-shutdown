"""
A program that shut downs the os with a timer.

Programmer: Miguel Sobong
Date Started: March 13 2019
To add:
    - Linux Support
"""

import os
import sys
import platform

# Variables to allow adding more predefined shutdown timers easily.
CUSTOM_CHOICE = 4
ABORT_CHOICE = 5
SHUTDOWN_CHOICE = 6

def main_menu():
	"""Main menu."""
	choice = None
	while True:
		print("Please select the shutdown timer:")
		print("\t[1] for 30mins")
		print("\t[2] for 1hour")
		print("\t[3] for 2hours")
		print(f"\t[{CUSTOM_CHOICE}] for Custom")
		print(f"\t[{ABORT_CHOICE}] for Abort Shutdown")
		print(f"\t[{SHUTDOWN_CHOICE}] for Exit")
		choice = int(input("Choice: "))
		if choice == SHUTDOWN_CHOICE:
			sys.exit(1)
		process_choice(choice)


def process_choice(choice):
	"""Run the main program."""
	user_os = platform.system()
	if user_os == 'Windows' and choice != SHUTDOWN_CHOICE:
		process_window(choice)
	elif user_os == 'Linux' and choice != SHUTDOWN_CHOICE:
		pass


def process_window(choice):
	"""Shutdown for Windows os.

	***hr * minutes * seconds
	"""
	shutdown_time = sub_command = None
	if choice == 1:
		shutdown_time = 30 * 60
	elif choice == 2:
		shutdown_time = 60 * 60
	elif choice == 3:
		shutdown_time = 2 * 60 * 60
	elif choice == CUSTOM_CHOICE:
		shutdown_time = custom_timer()
	elif choice == ABORT_CHOICE:
		sub_command = "-a"

	if choice != ABORT_CHOICE:
		sub_command = f"-s -t {shutdown_time}"
	_ = os.system(f"shutdown {sub_command}")


def custom_timer():
	"""Handle custom timer for shutdown."""
	print("Custom Timer:")
	hour = minute = second = 0
	hour = int(input("\tHours: "))
	minute = int(input("\tMinutes: "))
	second = int(input("\tSeconds: "))
	return (hour * 60 * 60) + (minute * 60) + second


def clear_screen():
	"""Clear the terminal screen."""
	user_os = platform.system()
	if user_os == 'Windows':
		_ = os.system("cls")
	elif user_os == 'Linux':
		_ = os.system("clear")


if __name__ == '__main__':
    main_menu()
