from config import load_config
from connect import connect


class DBAccessor():
    def __init__(self):
        self._conn = connect(load_config())
        self._db_cursor = self._conn.cursor()

    def get_all_students(self) -> list[tuple]:
        """
        Retrieves and displays all records from the students table.
        """
        self._db_cursor.execute("SELECT * FROM students")
        return self._db_cursor.fetchall()

    def add_student(self, first_name, last_name, email, enrollment_date) -> None:
        """
        Inserts a new student record into the students table.
        """
        self._db_cursor.execute(f"INSERT INTO students (first_name, last_name, email, enrollment_date) "
                                f"VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}')")

    def update_student_email(self, student_id, new_email) -> None:
        """
        Updates the email address for a student with the specified student_id.
         """
        self._db_cursor.execute(f"UPDATE students SET email = '{new_email}' WHERE student_id = {student_id} ")

    def delete_student(self, student_id) -> None:
        """
        Deletes the record of the student with the specified student_id.

        :param student_id: The student id of the student to delete.
        """
        self._db_cursor.execute(f"DELETE FROM students WHERE student_id = {student_id}")

    def commit_changes(self) -> None:
        """
        Commits changes done to postgres database
        """
        self._conn.commit()


# Testing procedure, for your own tests, you can modify this file or initialize DBAccessor in an external test harness.
if __name__ == '__main__':
    accessor = DBAccessor()
    # Base database
    print(accessor.get_all_students())
    # Student Alex should be added
    accessor.add_student("Alex", "Marques", "a@ex.com", "01/01/2023")
    print(accessor.get_all_students())
    # Student John should be removed
    accessor.delete_student(1)
    print(accessor.get_all_students())
    # Student Jane should have her email changed
    accessor.update_student_email(2, "janeNewEmail@example.com")
    print(accessor.get_all_students())
    # Commit changes to database
    accessor.commit_changes()
