import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError

class TestPhoneManager(unittest.TestCase):

    #1
    def test_create_and_add_new_phone(self):

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testPhones = [ testPhone1, testPhone2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)

    #2
    def test_create_and_add_phone_with_duplicate_id(self):
        # add a phone, add another phone with the same id, and verify an PhoneError exception is thrown
        # you'll need to modify PhoneAssignments.add_phone() to make this test pass
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(1, 'Apple', 'iPhone 5')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone2)

    #3
    def test_create_and_add_new_employee(self):
        # write this test and then remove the self.fail() statement
        # Add some employees and verify they are present in the PhoneAssignments.employees list
        test_employee1 = Employee(1, 'Jaime')
        test_employee2 = Employee(2, 'Jessica')

        testEmployees = [ test_employee1, test_employee2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(test_employee1)
        testAssignmentMgr.add_employee(test_employee2)
        
        self.assertCountEqual(testEmployees, testAssignmentMgr.employees)

    #4
    def test_create_and_add_employee_with_duplicate_id(self):
        # TODO write this test and then remove the self.fail() statement
        # TODO you'll need to fix the add_employee method in PhoneAssignments to make this test PhoneAssignments
        # This method will be similar to test_create_and_add_phone_with_duplicate_id
        
        testEmployee1 = Employee(1, 'Teddo')
        testEmployee2 = Employee(1, 'Marsupia')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_employee(testEmployee2)


    # #5
    # def test_assign_phone_to_employee(self):
    #     # TODO write this test and remove the self.fail() statement
    #     # TODO you'll need to fix the assign method in PhoneAssignments

    #     self.fail()

    # #6
    # def test_assign_phone_that_has_already_been_assigned_to_employee(self):
    #     # If a phone is already assigned to an employee, it is an error to assign it to a different employee. A PhoneError should be raised.
    #     # TODO write this test and remove the self.fail() statement
    #     # TODO you'll need to fix the assign method in PhoneAssignments so it throws an exception if the phone is alreaady assigned.

    #     self.fail()

    # #7
    # def test_assign_phone_to_employee_who_already_has_a_phone(self):
    #     # TODO write this test and remove the self.fail() statement
    #     # TODO you'll need to fix the assign method in PhoneAssignments so it raises a PhoneError if the phone is alreaady assigned.

    #     self.fail()

    # #8
    # def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
    #     # TODO The method should not make any changes but NOT raise a PhoneError if a phone
    #     # is assigned to the same user it is currenly assigned to.

    #     self.fail()

    # #9
    # def test_un_assign_phone(self):
    #     # TODO write this test and remove the self.fail() statement
    #     # Assign a phone, unasign the phone, verify the employee_id is None
    #     self.fail()

    # #10
    # def test_get_phone_info_for_employee(self):
    #     # TODO write this test and remove the self.fail() statement
    #     # Create some phones, and employees, assign a phone,
    #     # call phone_info and verify correct phone info is returned

    #     # TODO check that the method returns None if the employee does not have a phone
    #     # TODO check that the method raises an PhoneError if the employee does not exist

    #     self.fail()


if __name__ == '__main__':
    unittest.main()