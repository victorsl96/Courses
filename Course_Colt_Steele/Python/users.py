'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''
import csv

def find_user(f_name,l_name):
    with open('users.csv') as csvfile:
        csv_reader = csv.reader(csvfile)
        for (index, row) in enumerate(csv_reader):
            first_name_match = f_name == row[0]
            last_name_match = l_name == row[1]    
            if first_name_match and last_name_match:
                return print(index)
        return print('{} {} not found.'.format(f_name,l_name))

def update_users(o_f_name,o_l_name, n_f_name, n_l_name):
    with open('users.csv') as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

    count = 0

    with open('users.csv', 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == o_f_name and row[1] == o_l_name:
                csv_writer.writerow([n_f_name, n_l_name])
                count += 1

            else:
                csv_writer.writerow(row)

    return "Users updated: {}.".format(count)


def delete_users(f_name,l_name):
    with open('users.csv') as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

    count = 0

    with open('users.csv', 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == f_name and row[1] == l_name:
                count += 1
            else:
                csv_writer.writerow(row)
    return "Users deleted: {}.".format(count)