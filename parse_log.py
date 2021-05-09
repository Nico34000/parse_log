import sys
import datetime as dt
import logging

logging.basicConfig(filename='log.log',
                    level=logging.DEBUG)


def open_file(file):
    """This function open a file and return all line

    file : is the file to select for open and get
    all lines.
    """

    with open(file, 'r', encoding='utf-8')as f:
        logging.warning(f'open the file {file}')
        f = f.readlines()
        return f


def convert_hour(start, end):
    """ This function take 2 hours and return the delta
    in minutes. Example : start = 09:20 end = 11:00
    return 100 minutes

    start : is the start of the hour
    end : is the end of the hour
    """

    time_start = dt.datetime.strptime(start, "%H:%M")
    time_end = dt.datetime.strptime(end, "%H:%M")
    time_delta = time_end - time_start
    return time_delta.seconds//60


def file_to_dict():
    f = open_file(sys.argv[1])
    res = {}
    for line in f:
        if not line.isspace():
            line = line.split()
            logging.info(f'line : {line}')
            category = line[1]
            logging.info(f'category : {category}')
            hour = line[0].split('-')
            logging.info(f'hour : {hour}')
            minutes = convert_hour(hour[0], hour[1])
            logging.info(f'delta minutes : {minutes}')
            if category not in res:
                logging.debug('add line by line on dict')
                res[category] = minutes
                logging.info(f"key = {category} value = {minutes}")
            else:
                res[category] += minutes
                logging.info("if key existe add values")
    logging.info(f"this is ur dict {dict(sorted(res.items()))}")
    return dict(sorted(res.items()))


def total_time(values):
    """ This function sum all values in
    dict or a list.

    values = all values in dict or  list
    """
    total = 0
    for time in values:
        try:
            total += time
        except TypeError:
            return('Incorrect value')
    return total


def parse_dict():
    """ This function parse a dictionnary
    """
    dict_items = file_to_dict()
    space = " "
    total = total_time(dict_items.values())
    logging.debug(f"total of all values in dict {total}")
    for category, minutes in dict_items.items():
        pourcent = int(minutes/total*100)
        print(f'{category:19} {minutes:5} minutes{space*5}{pourcent:3} %')


if __name__ == '__main__':
    try:
        parse_dict()
    except IndexError:
        print("No file selected please add a path file in your 1st arg")
