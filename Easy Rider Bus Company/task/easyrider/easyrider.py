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

bus_stop = {}

# s = '[{"bus_id": 128,"stop_id": 1,"stop_name": "Prospekt Avenue","next_stop": 3,"stop_type": "S","a_time": "08:12"}, {"bus_id": 128,"stop_id": 3,"stop_name": "Elm Street","next_stop": 5,"stop_type": "","a_time": "08:19"}, {"bus_id": 128,"stop_id": 5,"stop_name": "Fifth Avenue","next_stop": 7,"stop_type": "O","a_time": "08:25"}, {"bus_id": 128,"stop_id": 7,"stop_name": "Sesame Street","next_stop": 0,"stop_type": "F","a_time": "08:37"}, {"bus_id": 256,"stop_id": 2,"stop_name": "Pilotow Street","next_stop": 3,"stop_type": "S","a_time": "09:20"}, {"bus_id": 256,"stop_id": 3,"stop_name": "Elm Street","next_stop": 6,"stop_type": "","a_time": "09:45"}, {"bus_id": 256,"stop_id": 6,"stop_name": "Sunset Boulevard","next_stop": 7,"stop_type": "","a_time": "09:59"}, {"bus_id": 256,"stop_id": 7,"stop_name": "Sesame Street","next_stop": 0,"stop_type": "F","a_time": "10:12"}, {"bus_id": 512,"stop_id": 4,"stop_name": "Bourbon Street","next_stop": 6,"stop_type": "S","a_time": "08:13"}, {"bus_id": 512,"stop_id": 6,"stop_name": "Sunset Boulevard","next_stop": 0,"stop_type": "F","a_time": "08:16"}]'
# s = '[{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Fifth Avenue", "next_stop" : 4, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 4, "stop_name" : "Abbey Road", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"},  {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Santa Monica Boulevard", "next_stop" : 8, "stop_type" : "O", "a_time" : "08:25"},  {"bus_id" : 128, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 11, "stop_type" : "", "a_time" : "08:37"},  {"bus_id" : 128, "stop_id" : 11, "stop_name" : "Beale Street", "next_stop" : 12, "stop_type" : "", "a_time" : "09:20"},  {"bus_id" : 128, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 14, "stop_type" : "", "a_time" : "09:45"},  {"bus_id" : 128, "stop_id" : 14, "stop_name" : "Bourbon Street", "next_stop" : 19, "stop_type" : "O", "a_time" : "09:59"},  {"bus_id" : 128, "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"},  {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:13"},  {"bus_id" : 256, "stop_id" : 3, "stop_name" : "Startowa Street", "next_stop" : 8, "stop_type" : "", "a_time" : "08:16"},  {"bus_id" : 256, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 10, "stop_type" : "", "a_time" : "08:29"},  {"bus_id" : 256, "stop_id" : 10, "stop_name" : "Lombard Street", "next_stop" : 12, "stop_type" : "", "a_time" : "08:44"},  {"bus_id" : 256, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 13, "stop_type" : "O", "a_time" : "08:46"},  {"bus_id" : 256, "stop_id" : 13, "stop_name" : "Orchard Road", "next_stop" : 16, "stop_type" : "", "a_time" : "09:13"}, {"bus_id" : 256, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 17, "stop_type" : "O", "a_time" : "09:26"},  {"bus_id" : 256, "stop_id" : 17, "stop_name" : "Khao San Road", "next_stop" : 20, "stop_type" : "O", "a_time" : "10:25"},  {"bus_id" : 256, "stop_id" : 20, "stop_name" : "Michigan Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "11:26"},  {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Arlington Road", "next_stop" : 7, "stop_type" : "S", "a_time" : "11:06"},  {"bus_id" : 512, "stop_id" : 7, "stop_name" : "Parizska Street", "next_stop" : 8, "stop_type" : "", "a_time" : "11:15"},  {"bus_id" : 512, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 9, "stop_type" : "", "a_time" : "11:56"},  {"bus_id" : 512, "stop_id" : 9, "stop_name" : "Niebajka Avenue", "next_stop" : 15, "stop_type" : "", "a_time" : "12:20"},  {"bus_id" : 512, "stop_id" : 15, "stop_name" : "Jakis Street", "next_stop" : 16, "stop_type" : "", "a_time" : "12:44"},  {"bus_id" : 512, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 18, "stop_type" : "", "a_time" : "13:01"},  {"bus_id" : 512, "stop_id" : 18, "stop_name" : "Jakas Avenue", "next_stop" : 19, "stop_type" : "", "a_time" : "14:00"},  {"bus_id" : 1024, "stop_id" : 21, "stop_name" : "Karlikowska Avenue", "next_stop" : 12, "stop_type" : "S", "a_time" : "13:01"},  {"bus_id" : 1024, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:00"},  {"bus_id" : 512, "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:11"}]'
s = input()
json_list = loads(s)
for json_dict in json_list:
    for key in json_dict:
        if key == 'bus_id':
            val = str(json_dict['bus_id'])
            bus_stop.setdefault(val, 0)
            bus_stop[val] += 1

print('Line names and number of stops:')
for key, val in bus_stop.items():
    print(f'bus_id: {key}, stops: {val}')
