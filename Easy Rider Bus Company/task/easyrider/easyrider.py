"""
Project: Easy Rider Bus Company
Stage 2/6: Correct syntax


Description
You managed to fill in all the missing data and correct the mistakes with the types. However, you noticed that there are multiple problems with suffix names for the stops: sometimes they are incorrect, and sometimes they are simply missing. As if that was not enough, you also realized that there are errors in the arrival times.

It seems like you have to carefully look at the entire "Format" column in the first part of the documentation.

Here are the documents that you have: documentation and diagram of the bus lines.

Objectives
The string containing the data in JSON format is passed to standard input.
Check that the data format complies with the documentation.
Only the fields that have such a requirement are relevant, i.e. stop_name, stop_type, a_time, so, please, count errors only for them.
Like in the previous stage, print the information about the number of found errors in total and in each field. Remember that there might be no errors at all.
The output should have the same formatting as shown in the example.
If you can't find the necessary information in the stage description, it can probably be found in the attached documentation.

Note that the time format is military time (24 hours, hh:mm). That means that there are certain restrictions:

the first digit cannot be 3, 4, etc.;
hours less than 10 should have zero in front of them, e.g. 08:34;
the delimiter should be colon :.
Example
Input:

[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Av.",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "08:12"
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "8:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "OO",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:77"
    },
    {
        "bus_id": 256,
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "09:20"
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "A",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "10.12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "bourbon street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "38:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]
Output:

Format validation: 9 errors
stop_name: 3
stop_type: 2
a_time: 4
"""


from json import loads


def integer(k_j, k_e, v_j):
    return k_j == k_e and isinstance(v_j, int)


def strings(k_j, k_e, v_j):
    return k_j == k_e and v_j != '' and isinstance(v_j, str)


def char(k_j, k_e, v_j):
    return k_j == k_e and v_j in ['', 'S', 'O', 'F']


def time(k_j, k_e, v_j):
    return k_j == k_e and isinstance(v_j, str) and len(v_j) == 5 and v_j[:2].isdecimal() and v_j[3:].isdecimal() \
           and val_j[2] == ':' and int(val_j[0]) < 6 and int(val_j[3]) < 6


err_dict = {'bus_id': [0, 'int'], 'stop_id': [0, 'int'], 'stop_name': [0, 'str'], 'next_stop': [0, 'int'],
            'stop_type': [0, 'char'], 'a_time': [0, 'time']}

s = '[{"bus_id": 128, "stop_id": 1, "stop_name": "Prospekt Av.", "next_stop": 3, "stop_type": "S", "a_time": "08:12"}, {"bus_id": 128, "stop_id": 3, "stop_name": "Elm Street", "next_stop": 5, "stop_type": "", "a_time": "8:19"}, {"bus_id": 128, "stop_id": 5, "stop_name": "Fifth Avenue", "next_stop": 7, "stop_type": "OO", "a_time": "08:25"}, {"bus_id": 128, "stop_id": 7, "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F", "a_time": "08:77"}, {"bus_id": 256, "stop_id": 2, "stop_name": "Pilotow Street", "next_stop": 3, "stop_type": "S", "a_time": "09:20"}, {"bus_id": 256, "stop_id": 3, "stop_name": "Elm", "next_stop": 6, "stop_type": "", "a_time": "09:45"}, {"bus_id": 256, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 7, "stop_type": "A", "a_time": "09:59"}, {"bus_id": 256, "stop_id": 7, "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F", "a_time": "10.12"}, {"bus_id": 512, "stop_id": 4, "stop_name": "bourbon street", "next_stop": 6, "stop_type": "S", "a_time": "38:13"}, {"bus_id": 512, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 0, "stop_type": "F", "a_time": "08:16"}]'
# s = input()
json_list = loads(s)
for json_dict in json_list:
    for j, e in zip(json_dict.items(), err_dict.items()):
        key_e, val_e, key_j, val_j = *e, *j
        if val_e[1] == 'int':
            if not integer(key_e, key_j, val_j):
                err_dict[key_e][0] += 1
        if val_e[1] == 'str':
            if not strings(key_e, key_j, val_j):
                err_dict[key_e][0] += 1
        if val_e[1] == 'char':
            if not char(key_e, key_j, val_j):
                err_dict[key_e][0] += 1
        if val_e[1] == 'time':
            if not time(key_e, key_j, val_j):
                err_dict[key_e][0] += 1

err = sum([val[0] for val in err_dict.values()])
print(f'''
Type and required field validation: {err} errors
bus_id: {err_dict['bus_id'][0]}
stop_id: {err_dict['stop_id'][0]}
stop_name: {err_dict['stop_name'][0]}
next_stop: {err_dict['next_stop'][0]}
stop_type: {err_dict['stop_type'][0]}
a_time: {err_dict['a_time'][0]}''')
