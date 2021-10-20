#!/usr/bin/env python
import re
import csv
import operator


errors = {}
per_user = {}
log = 'syslog.log'


def get_errors():
    '''updates the errors dictionary with the error and the ocurrence count'''
    with open(log, 'r') as log_file:
        for line in log_file.readlines():
            match = re.search(r': ERROR (.+) \(', line)
            if match:
                if match.group(1) not in errors.keys():
                    errors[match.group(1)] = 0
                errors[match.group(1)] += 1
        log_file.close()
# {'Connection to DB failed': 4, 'Trolled the manager': 1}


def get_data():
    '''returns a list of lists containing the pairs: type of log and username'''
    data = []
    with open(log, 'r') as log_file:
        for line in log_file.readlines():
            match = re.search(r': (\w+).+\((.+)\)', line)
            data.append([match.group(1), match.group(2)])
        log_file.close()
    return data
# data = [['INFO', 'arnald'], ['ERROR', 'heise'], ['INFO', 'manny'], ['ERROR', 'otto'], ['INFO', 'mana'],
#  ['ERROR', 'uri'], ['INFO', 'sam'], ['ERROR', 'faustus'], ['INFO', 'jack'], ['ERROR', 'lehman']]


def process_data(data):
    '''updates the per_user dict with the username as key and a list containing the amount
     of successfull and failed interactions with the system'''
    for element in data:
        if element[1] not in per_user.keys():
            per_user[element[1]] = [0, 0]
        if element[0] == 'INFO':
            per_user[element[1]][0] += 1
        elif element[0] == 'ERROR':
            per_user[element[1]][1] += 1

# per_user = {'arnald': [1, 0], 'heise': [0, 1], 'manny': [1, 0], 'otto': [0, 1],
#  'mana': [1, 0], 'uri': [0, 1], 'sam': [1, 0], 'faustus': [0, 1], 'jack': [1, 0], 'lehman': [0, 1]}


def export_data():
    '''generates two csv reports: the amount of errors and the user statistics'''
    with open('error_message.csv', 'w') as csv_file2:
        fieldnames = ['Error', 'Count']
        writer = csv.DictWriter(csv_file2, fieldnames=fieldnames)
        writer.writeheader()
        for key, value in sorted(errors.items(), key=operator.itemgetter(1), reverse=True):
            writer.writerow({'Error': key, 'Count': value})
        csv_file2.close()

    with open('user_statistics.csv', 'w') as csv_file:
        fieldnames = ['Username', 'INFO', 'ERROR']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for key, value in sorted(per_user.items(), key=operator.itemgetter(0)):
            writer.writerow(
                {'Username': key, 'INFO': value[0], 'ERROR': value[1]})
        csv_file.close()


def main():
    get_errors()
    process_data(get_data())
    export_data()


if __name__ == '__main__':
    main()
