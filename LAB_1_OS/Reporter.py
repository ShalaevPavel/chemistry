import pickle



def make_reports(name_of_binary, name_of_txt, per_hour) -> str:

    with open(name_of_binary, 'rb') as f:
        data_new = pickle.load(f)
    with open(name_of_txt, "w") as file:
        for employee in data_new:
            file.write(employee.num)
            file.write(employee.name)
            file.write(str(employee.hours * per_hour))
    return name_of_txt

