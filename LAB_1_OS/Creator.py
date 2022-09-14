import pickle


def make_binary(name_of_binary: str, number_of_employees: int) -> str:
    list_of_employees = []
    for i in range(number_of_employees):
        num = int(input("Enter the id "))
        name = input("Enter the name ")
        hours = int(input("Enter the work hours "))

        tmp_employee = Employee(num, name, hours)
        list_of_employees.append(tmp_employee)

    pickle.dump(list_of_employees, open(name_of_binary, "wb"))

    return name_of_binary


class Employee:
    def __init__(self, num, name, hours):
        self.num = num
        self.name = name
        self.hours = hours


#make_binary("attempt.bin", 1)
