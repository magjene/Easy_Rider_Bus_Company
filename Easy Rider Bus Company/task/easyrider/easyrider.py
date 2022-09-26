"""
Project: Easy Rider Bus Company
Stage 1/6: Checking the data type


Description
You just started sorting out the existing database of the "Easy Rider" bus company. As you take the first look at the data, you realize that it's not going to be easy.

Sometimes numbers are missing from where they should definitely be. You also noticed that sometimes there are too many or too few characters. Fortunately, there is documentation to help you sort out this mess. However, this documentation is not a hundred percent complete: part of it was torn away when your colleague spilled coffee on it. Let's see what we can make out.

Here are the documents that you have: documentation and diagram of the bus lines.

Objectives
The string containing the data in JSON format is passed to standard input.
Check that the data types match.
Check that the required fields are filled in.
Display the information about the number of found errors in total and in each field. Keep in mind that there might be no errors at all.
The output should have the same formatting as shown in the example.
No need to worry about the format now. Let's at first just make sure that the fields have the right type and all required ones are filled.
If you can't find the necessary information in the stage description, it can probably be found in the attached documentation.

Note that the type Char is present among the data types.

Example
Input:

[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": 8.12
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": "7",
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": "",
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": ""
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": "0",
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": "512",
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": 5,
        "a_time": "08:16"
    }
]
Output:

Type and required field validation: 8 errors
bus_id: 2
stop_id: 1
stop_name: 1
next_stop: 1
stop_type: 1
a_time: 2
"""


from json import loads
from sys import stdin


err_dict = {'bus_id': [0, 'int'], 'stop_id': [0, 'int'], 'stop_name': [0, 'str'], 'next_stop': [0, 'int'],
            'stop_type': [0, 'shar'], 'a_time': [0, 'time']}

# json_dict = loads('\n'.join(stdin.read().split('\n')))


s = '''[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": 8.12
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": "7",
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": "",
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": ""
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": "0",
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": "512",
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": 5,
        "a_time": "08:16"
    }
]'''
json_dict = loads(s)


def integer(k_j, k_e, v_j):
    return k_j == k_e and isinstance(v_j, int)


def strings(k_j, k_e, v_j):
    return k_j == k_e and v_j != '' and isinstance(v_j, str)


def char(k_j, k_e, v_j):
    return (k_j == k_e and v_j == '') or (k_j == k_e and isinstance(v_j, str) and len(v_j) == 1)


def time(k_j, k_e, v_j):
    return k_j == k_e and len(v_j) == 5 and isinstance(v_j[:2], int) and isinstance(v_j[3:], int) and val_j[2] == ':' \
           and val_j[0] < 6 and val_j[3] < 6


err = 0

for i in range(len(json_dict)):
    for j, e in zip(json_dict[i].items(), err_dict.items()):
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
        # if val_e[1] == 'time':
        #     if not time(key_e, key_j, val_j[0]):
        #         err_dict[key_e][0] += 1


print(f'''
Type and required field validation: {err} errors
bus_id: {err_dict['bus_id'][0]}
stop_id: {err_dict['stop_id'][0]}
stop_name: {err_dict['stop_name'][0]}
next_stop: {err_dict['next_stop'][0]}
stop_type: {err_dict['stop_type'][0]}
a_time: {err_dict['a_time'][0]}
''')
