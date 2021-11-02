"""
Student maintenance module
This module contains the functions for adding, updating, and deleting student data
"""

__authors__ = "Jordan Booth and Mackenzie Eskey"
__version__ = "1.0"
__date__ = "11.2.2021"
__status__ = "Development"

import utils


def main():
    """
    Test code for student maintenance module
    :return: no value
    :rtype: none
    """
    print('Test code for student maintenance module')
    next_student_id = 1
    students = []
    add_student(students, next_student_id)
    list_students(students)
    update_student(students)
    list_students(students)
    stud_index = find_student_index(students, 1)
    print("Student index method:", stud_index)
    delete_student(students)
    list_students(students)


def add_student(students, next_student_id):
    """
    Display the all student information stored in a 2D list.  It will increment the last student id by one
    and use it as the new student's id.  It also, displays that the student was successfully added.

    :param students: student data (id, first_name, last_name)
    :type students: 2d list

    :param next_student_id: the next student id to be used for the add function
    :type next_student_id: int

    :return no value
    :rtype none
    """
    first_name = input("Please enter the student's first name: ").title()
    last_name = input("Please enter the student's last name: ").title()

    students.append([next_student_id, first_name, last_name])

    print("Student ID #" + str(next_student_id) + " " + first_name + " " + last_name +
          " was added.")


def delete_student(students):
    """
    It will first check to see if there is any student data, and notify the user if no data is found.

    It will then prompt the user for a valid student ID to be deleted from the 2D list
    It handles for non numeric data, and student IDs that do not exists via the find_student_index

    It will prompt the user to confirm they want to delete the selected student, and then let the user know
    if the user was successfully deleted.

    :param students: student data (id, first_name, last_name)
    :type students: 2d list

    :return no value
    :rtype none
    """
    if not students:
        print("No student data found.")
        return

    student_input = utils.get_positive_num("Please enter the student ID to be deleted: ", "int")

    if find_student_index(students, student_input) == -1:
        print('No student found with ID #' + str(student_input) + ".")
        return

    else:
        student_id = find_student_index(students, student_input)
        student = students[student_id]

        user_confirm = utils.get_yn("Please confirm deleting Student ID #" + str(student[0]) + " " +
                                    str(student[1]) + " " + str(student[2]) + " (y/n): ")

        if user_confirm == 'y':
            students.remove(student)
            print("Student ID #" + str(student[0]) + " " + str(student[1]) + " " + str(student[2]) +
                  " was deleted.")

        else:
            print('Deletion cancelled.')


def find_student_index(students, student_id):
    """
    Search the 2D list for a specific student ID.
    :param students: student data (id, first_name, last_name)
    :type students: 2d list
    :param student_id: student id that they user wants to find
    :type student_id: int

    :return the index of the student in the 2D list or -1 if not found
    :rtype int
    """
    for student in students:
        if student_id == student[0]:
            return students.index(student)
    return -1


def list_students(students):
    """
    Display the all student information stored in a 2D list (id, first name, last name)
    It will notify the student if there is no data found.

    :param students: student data (id, first_name, last_name)
    :type students: 2d list

    :return no value
    :rtype none
    """
    if not students:
        print("No student data found.")
        return
    print(
        f'{"ID":>4s}'
        f'{"First Name":>12s}'
        f'{"Last Name":>21s}')
    print(f'{"*" * 4:>4s}'
          f'{"*" * 20:>22s}'
          f'{"*" * 20:>22s}')
    for student in students:
        row = student
        print(
            f'{str(row[0]):>4s}'
            f'{" ":>2s}'
            f'{str(row[1]):<20s}'
            f'{" ":>2s}'
            f'{str(row[2]):<20s}')


def update_student(students):
    """
    It will first check to see if there is any student data, and notify the user if no data is found.

    It will then prompt the user for a valid student ID to be updated from the 2D list
    It handles for non numeric data, and student IDs that do not exists via the find_student_index

    It will prompt the user to confirm they want to update the selected student, and then let the user know
    if the user was successfully updated.

    :param students: student data (id, first_name, last_name)
    :type students: 2d list

    :return no value
    :rtype none
    """

    if not students:
        print("No student data found.")
        return

    student_input = utils.get_positive_num("Please enter the student ID to be updated: ", "int")

    if find_student_index(students, student_input) == -1:
        print('No student found with ID #' + str(student_input) + ".")
        return

    else:
        student_id = find_student_index(students, student_input)
        student = students[student_id]

    user_confirm = utils.get_yn("Please confirm updating Student ID #" + str(student[0]) + " " +
                                str(student[1]) + " " + str(student[2]) + " (y/n): ")

    if user_confirm == 'y' or user_confirm == 'yes':
        student_first = input("Please enter the student's first name or press enter to keep " +
                              str(student[1]) + ": ") or student[1]
        student_last = input("Please enter the student's last name or press enter to keep " +
                             str(student[2]) + ": ") or student[2]

        print("Student ID #" + str(student[0]) + " " + str(student[1]) + " " + str(student[2]) +
              " was updated to " + student_first + " " + student_last + ".")
        student[1] = student_first.title()
        student[2] = student_last.title()

    else:
        print('Update cancelled.')


# runs this specific module's main
if __name__ == "__main__":
    main()
