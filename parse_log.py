import datetime as dt
import logging

logging.basicConfig(filename='log.log',
                    level=logging.DEBUG)


def open_file(file):
    """This function open a file and add all lines
    in list.

    file : is the file to select for open and add
    all lines.
    """
    with open(file, 'r', encoding='utf-8')as f:
        logging.warning(f'open the file {file}')
        res = []
        logging.debug('add line by line on list')
        for line in f:
            if line.strip():
                res.append(line.rstrip())
        return res


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


def parse_log():
    """
    This function take the list of the lines of the file
    split for recover all hour of this list.
    Convert all delta hour with the function convert_hour.
    Return all category with delta time and the % of the
    minutes
    """
    time_list = open_file('planning.log')
    for rows in time_list:
        timer = rows.split()[0]
        logging.info(f'This is all time of file {timer}')
        start = timer.split('-')[0]
        logging.info(f'take start hour {start}')
        end = timer.split('-')[1]
        logging.info(f'take end hour {end}')
        time_delta = convert_hour(start, end)
        logging.info(f'this is the delta of all hours {time_delta} minutes')
        category = ' '.join(rows.split()[1:])
        logging.info('recover all categories')
        res = f'{category:30}{time_delta} minutes  {int(time_delta/970*100)} %'
        logging.info(f'This is your result: {res}')
        print(res)


print(parse_log())
