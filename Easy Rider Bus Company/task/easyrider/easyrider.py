"""
Project: Easy Rider Bus Company
Stage 3/6: Bus line info


Description
It wasn't easy, but finally, you verified the data format and the required fields. It is now time to check how many bus lines we have and how many stops there are on each line. Before we can go further with sorting out the database, it would be a good idea to check that the information is complete.

Here are the documents that you have: documentation and diagram of the bus lines.

Objectives
The string containing the data in JSON format is passed to standard input.
Find the names of all the bus lines.
Verify the number of stops for each line.
The output should have the same formatting as shown in the example.
If you can't find the necessary information in the stage description, it can probably be found in the attached documentation.

Example
Input:

[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
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
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
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
        "next_stop": 0,
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
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]
Output:

Line names and number of stops:
bus_id: 128, stops: 4
bus_id: 256, stops: 4
bus_id: 512, stops: 2
"""


from json import loads
import re


err_dict = {'bus_id': [0, 'int'],
            'stop_id': [0, 'int'],
            'stop_name': [0, r'\A[A-Z].*[a-z] (Road|Avenue|Boulevard|Street)\Z'],
            'next_stop': [0, 'int'],
            'stop_type': [0, r'\A[S|O|F]?\Z'],
            'a_time': [0, r'\A([0-1][0-9]|2[0-3]):[0-6][0-9]\Z']}

bus_stop = {'128': 0, '256': 0, '512': 0}

s = '[{"bus_id": 128,"stop_id": 1,"stop_name": "Prospekt Avenue","next_stop": 3,"stop_type": "S","a_time": "08:12"}, {"bus_id": 128,"stop_id": 3,"stop_name": "Elm Street","next_stop": 5,"stop_type": "","a_time": "08:19"}, {"bus_id": 128,"stop_id": 5,"stop_name": "Fifth Avenue","next_stop": 7,"stop_type": "O","a_time": "08:25"}, {"bus_id": 128,"stop_id": 7,"stop_name": "Sesame Street","next_stop": 0,"stop_type": "F","a_time": "08:37"}, {"bus_id": 256,"stop_id": 2,"stop_name": "Pilotow Street","next_stop": 3,"stop_type": "S","a_time": "09:20"}, {"bus_id": 256,"stop_id": 3,"stop_name": "Elm Street","next_stop": 6,"stop_type": "","a_time": "09:45"}, {"bus_id": 256,"stop_id": 6,"stop_name": "Sunset Boulevard","next_stop": 7,"stop_type": "","a_time": "09:59"}, {"bus_id": 256,"stop_id": 7,"stop_name": "Sesame Street","next_stop": 0,"stop_type": "F","a_time": "10:12"}, {"bus_id": 512,"stop_id": 4,"stop_name": "Bourbon Street","next_stop": 6,"stop_type": "S","a_time": "08:13"}, {"bus_id": 512,"stop_id": 6,"stop_name": "Sunset Boulevard","next_stop": 0,"stop_type": "F","a_time": "08:16"}]'
# s = input()
json_list = loads(s)
for json_dict in json_list:
    for key in json_dict:
        if key == 'bus_id':
            val = json_dict['bus_id']
            bus_stop[str(val)] += 1

print('Line names and number of stops:')
for key, val in bus_stop.items():
    print(f'bus_id: {key}, stops: {val}')
