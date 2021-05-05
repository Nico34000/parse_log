import datetime as dt


def open_file(file):
    with open(file, 'r', encoding='utf-8')as f:
        res = []
        for line in f:
            if line.strip():
                res.append(line.rstrip())
        return res


def convert_hour(start, end):
    time_start = dt.datetime.strptime(start, "%H:%M")
    time_end = dt.datetime.strptime(end, "%H:%M")
    time_delta = time_end - time_start
    return time_delta.seconds//60


def parse_log():
    time_list = open_file('planning.log')
    for rows in time_list:
        timer = rows.split()[0]
        start = timer.split('-')[0]
        end = timer.split('-')[1]
        time_delta = convert_hour(start, end)
        category = ' '.join(rows.split()[1:])
        res = f'{category:30}{time_delta} minutes {int(time_delta/970*100)}%'
        print(res)


print(parse_log())
