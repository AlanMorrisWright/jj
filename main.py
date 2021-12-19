import json
my_list = []
with open('C:\\!\\CODING\\ED\\J\\Market.json') as f:
    lines = f.readlines()
    columns = []  # To store column names

    i = 1
    for line in lines:
        line = line.strip()  # remove leading/trailing white spaces
        if line:
            if i == 1:
                columns = [item.strip() for item in line.split(',')]
                print(columns)
                i = i + 1
            else:
                d = {}  # dictionary to store file data (each line)
                data = [item.strip() for item in line.split(',')]
                for index, elem in enumerate(data):
                    d[columns[index]] = data[index]

                my_list.append(d)  # append dictionary to list


def stack():
    pass
    #array = '{"fruits": ["apple", "banana", "orange"]}'
    #data  = json.loads(array)
    #print data['fruits']
    # the print displays:
    # [u'apple', u'banana', u'orange']


def main():
    commods = xx()
    print(commods)


if __name__ == '__main__':
    main()
