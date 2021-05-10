import sys
import datetime as dt
import logging


def open_file(file):
    """This function open a file and return all line

    file : is the file to select for open and get
    all lines.
    """

    with open(file, 'r', encoding='utf-8')as f:
        logging.info(f'open the file {file}')
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


def file_to_dict(file_lines):
    """ This function parse a list of lines
    and return a dictionnary with the format:
    imagine you have a list like 
    ["09:20-11:00 Introduction",
                    "11:00-11:15 Exercises",
                    "11:15-11:35 Break"]
    the function return a dict :
    {"Break" : 20, "Exercises" : 15}

    file_lines : is the list of lines from file 
    or other.
    """

    res = {}
    for line in file_lines:
        if not line.isspace():
            lines = line.split()
            logging.info(f'line : {line}')
            category = line[11:].strip()
            logging.info(f'category : {category}')
            hour = lines[0].split('-')
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


def parse_dict(dictionnary, output_file):
    """ This function parse a dictionnary and 
    add the result in a file.
    exemple you have a dictionnary like :
    {"Break" : 20, "Exercises" : 15}
    the function return and add fles: two lines :
    Break                  20 minutes        57%
    Exercises              15 minutes        43%

    dictionnary : is the dictionnary want to parse
    output_file: is file what to write
    """
    space = " "
    total = total_time(dictionnary.values())
    logging.debug(f"total of all values in dict {total}")
    for category, minutes in dictionnary.items():
        with open(output_file, "w", encoding='utf8') as output:
            pourcent = int(minutes/total*100)
            res = (f'{category:21} {minutes:3} minutes{space*5}{pourcent:4}%')
            print(res)
            output.write(f'{res}\n')
    print(f"Your result has been add in file {output.name}")
    logging.info(f"Your result has been add in file {output.name}")
    return res


def main():
    try:
        file_lines = open_file(sys.argv[1])
        my_dict = file_to_dict(file_lines)
        parse_dict(my_dict, "output.txt")
    except IndexError:
        print("No file selected please add a path file in your 1st arg")


if __name__ == '__main__':
    logging.basicConfig(filename='log.log',
                        level=logging.DEBUG)
    main()
