"""
Student Data System for managing student information (student id, first name, and last name)
This module contains the functions for displaying the main menu and running the menu options
"""

__authors__ = "Jordan Booth and Mackenzie Eskey"
__version__ = "1.0"
__date__ = "11.2.2021"
__status__ = "Development"

import utils
import student_maintenance


def main():
    """
    Inputs:
    Main menu number to choose an option
    Any inputs from the student maintenance functions

    Outputs:
    The display menu
    Prompt for user input on which menu option they want to choose
    Any outputs from the student maintenance functions
    :return:
    """
    students = []
    next_student_id = 0

    while True:
        display_student_menu()

        menu_input = utils.get_range('Please enter a valid menu # (0-6): ', -1, 6, 'int')
        print()
        if menu_input == 1:
            print("List all students")
            utils.display_line()
            student_maintenance.list_students(students)

        elif menu_input == 2:
            next_student_id += 1
            print("Add a student")
            utils.display_line()
            student_maintenance.add_student(students, next_student_id)

        elif menu_input == 3:
            print("Update a student")
            utils.display_line()
            student_maintenance.update_student(students)

        elif menu_input == 4:
            print("Delete a student")
            utils.display_line()
            student_maintenance.delete_student(students)

        elif menu_input == 5:
            print("Course menu")
            utils.display_line()
            display_course_menu()

        elif menu_input == 6:
            print("Sport menu")
            utils.display_line()
            display_sport_menu()

        elif menu_input == 0:
            print("Exiting program...\n")
            print("Goodbye!")
            break
        print()


def display_student_menu():
    """
    Displays the main menu and all of its options
    :return: no value
    """
    print('Student Menu')
    utils.display_line()
    print('1 - List all students')
    print('2 - Add a student')
    print('3 - Update a student')
    print('4 - Delete a student')
    print('5 - Course menu')
    print('6 - Sport menu')
    print('0 - Exit program')


def display_course_menu():
    """
    Display the menu for student courses
    :return: no value
    """
    print('1 - List available courses')
    print('2 - Enroll a student in a course')
    print("3 - Delete a student's course")
    print('0 - Exit program')


def display_sport_menu():
    """
    Display the menu for student courses
    :return: no value
    """
    print('1 - List available sports')
    print('2 - Add a student in a sport')
    print("3 - Delete a student's sport")
    print('0 - Exit program')


# runs this specific module's main
if __name__ == "__main__":
    main()
