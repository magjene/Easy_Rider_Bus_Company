"""
Project: Easy Rider Bus Company
Stage 4/6: Special stops


Description
The missing part of the specification is nowhere to be found. You need to recover and update the data contained in the second part of the documentation.

The company is growing, the number of bus lines is ever-increasing, and logically, more bus stops appear. You need to prepare an appropriate function that calculates this data so that it doesn't have to be checked manually in the future.

Here are the documents that you have: documentation and diagram of the bus lines.

Objectives
The string containing the data in JSON format is passed to standard input.
Make sure each bus line has exactly one starting point (S) and one final stop (F).
If a bus line does not meet this condition, stop checking and print a message about it. Do not continue checking the other bus lines.
If all bus lines meet the condition, count how many starting points and final stops there are. Print their unique names in alphabetical order.
Count the transfer stops and print their unique names in alphabetical order. A transfer stop is a stop shared by at least two bus lines.
The output should have the same formatting as shown in the example.
If you cannot find the necessary information in the stage description, it can probably be found in the attached documentation.

Examples
Example 1

Input 1:

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
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "",
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
Output 1:

There is no start or end stop for the line: 512.
Example 2

Input 2:

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
Output 2:

Start stops: 3 ['Bourbon Street', 'Pilotow Street', 'Prospekt Avenue']
Transfer stops: 3 ['Elm Street', 'Sesame Street', 'Sunset Boulevard']
Finish stops: 2 ['Sesame Street', 'Sunset Boulevard']
"""


from json import loads


transfer_dict, bus_stop = {}, {}
bus_s, bus_f, bus_t = set(), set(), set()
transfer_list = []

# s = '[{"bus_id": 128, "stop_id": 1, "stop_name": "Prospekt Avenue", "next_stop": 3, "stop_type": "S", "a_time": "08:12"},{"bus_id": 128, "stop_id": 3, "stop_name": "Elm Street", "next_stop": 5, "stop_type": "", "a_time": "08:19"},{"bus_id": 128, "stop_id": 5, "stop_name": "Fifth Avenue", "next_stop": 7, "stop_type": "O", "a_time": "08:25"},{"bus_id": 128, "stop_id": 7, "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F", "a_time": "08:37"},{"bus_id": 512, "stop_id": 4, "stop_name": "Bourbon Street", "next_stop": 6, "stop_type": "", "a_time": "08:13"},{"bus_id": 512, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 0, "stop_type": "F", "a_time": "08:16"}]'
# s = '[{"bus_id": 128, "stop_id": 1, "stop_name": "Prospekt Avenue", "next_stop": 3, "stop_type": "S", "a_time": "08:12"},{"bus_id": 128, "stop_id": 3, "stop_name": "Elm Street", "next_stop": 5, "stop_type": "", "a_time": "08:19"},{"bus_id": 128, "stop_id": 5, "stop_name": "Fifth Avenue", "next_stop": 7, "stop_type": "O", "a_time": "08:25"},{"bus_id": 128, "stop_id": 7, "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F", "a_time": "08:37"},{"bus_id": 256, "stop_id": 2, "stop_name": "Pilotow Street", "next_stop": 3, "stop_type": "S", "a_time": "09:20"},{"bus_id": 256, "stop_id": 3, "stop_name": "Elm Street", "next_stop": 6, "stop_type": "", "a_time": "09:45"},{"bus_id": 256, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 7, "stop_type": "", "a_time": "09:59"},{"bus_id": 256, "stop_id": 7, "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F", "a_time": "10:12"},{"bus_id": 512, "stop_id": 4, "stop_name": "Bourbon Street", "next_stop": 6, "stop_type": "S", "a_time": "08:13"},{"bus_id": 512, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 0, "stop_type": "F", "a_time": "08:16"}]'

s = '[{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Fifth Avenue", "next_stop" : 4, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 4, "stop_name" : "Abbey Road", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"},  {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Santa Monica Boulevard", "next_stop" : 8, "stop_type" : "O", "a_time" : "08:25"},  {"bus_id" : 128, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 11, "stop_type" : "", "a_time" : "08:37"},  {"bus_id" : 128, "stop_id" : 11, "stop_name" : "Beale Street", "next_stop" : 12, "stop_type" : "", "a_time" : "09:20"},  {"bus_id" : 128, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 14, "stop_type" : "", "a_time" : "09:45"},  {"bus_id" : 128, "stop_id" : 14, "stop_name" : "Bourbon Street", "next_stop" : 19, "stop_type" : "O", "a_time" : "09:59"},  {"bus_id" : 128, "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"},  {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:13"},  {"bus_id" : 256, "stop_id" : 3, "stop_name" : "Startowa Street", "next_stop" : 8, "stop_type" : "", "a_time" : "08:16"},  {"bus_id" : 256, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 10, "stop_type" : "", "a_time" : "08:29"},  {"bus_id" : 256, "stop_id" : 10, "stop_name" : "Lombard Street", "next_stop" : 12, "stop_type" : "", "a_time" : "08:44"},  {"bus_id" : 256, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 13, "stop_type" : "O", "a_time" : "08:46"},  {"bus_id" : 256, "stop_id" : 13, "stop_name" : "Orchard Road", "next_stop" : 16, "stop_type" : "", "a_time" : "09:13"},  {"bus_id" : 256, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 17, "stop_type" : "", "a_time" : "09:26"},  {"bus_id" : 256, "stop_id" : 17, "stop_name" : "Khao San Road", "next_stop" : 20, "stop_type" : "O", "a_time" : "10:25"},  {"bus_id" : 256, "stop_id" : 20, "stop_name" : "Michigan Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "11:26"},  {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Arlington Road", "next_stop" : 7, "stop_type" : "S", "a_time" : "11:06"},  {"bus_id" : 512, "stop_id" : 7, "stop_name" : "Parizska Street", "next_stop" : 8, "stop_type" : "", "a_time" : "11:15"},  {"bus_id" : 512, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 9, "stop_type" : "", "a_time" : "11:56"},  {"bus_id" : 512, "stop_id" : 9, "stop_name" : "Niebajka Avenue", "next_stop" : 15, "stop_type" : "", "a_time" : "12:20"},  {"bus_id" : 512, "stop_id" : 15, "stop_name" : "Jakis Street", "next_stop" : 16, "stop_type" : "", "a_time" : "12:44"},  {"bus_id" : 512, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 18, "stop_type" : "", "a_time" : "13:01"},  {"bus_id" : 512, "stop_id" : 18, "stop_name" : "Jakas Avenue", "next_stop" : 19, "stop_type" : "", "a_time" : "14:00"},  {"bus_id" : 1024, "stop_id" : 21, "stop_name" : "Karlikowska Avenue", "next_stop" : 12, "stop_type" : "S", "a_time" : "13:01"},  {"bus_id" : 1024, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:00"},  {"bus_id" : 512, "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:11"}]'

# s = input()
json_list = loads(s)
for json_dict in json_list:
    bus_id = str(json_dict['bus_id'])
    bus_stop.setdefault(bus_id, {'S': 0, 'F': 0})
    transfer_dict.setdefault(bus_id, set())
    transfer_dict[bus_id].add(json_dict['stop_name'])
    if json_dict['stop_type'] == 'S':
        bus_stop[bus_id]['S'] += 1
        bus_s.update({json_dict['stop_name']})
    elif json_dict['stop_type'] == 'F':
        bus_stop[bus_id]['F'] += 1
        bus_f.update({json_dict['stop_name']})
    if bus_stop[bus_id]['F'] > 1 or bus_stop[bus_id]['S'] > 1:
        print(f'There is no start or end stop for the line: {bus_id}.')
        break
else:
    for bus_id, sf in bus_stop.items():
        if sf['F'] == 0 or sf['S'] == 0:
            print(f'There is no start or end stop for the line: {bus_id}.')
            break
    else:
        [transfer_list.append(val) for val in transfer_dict.values()]
        [bus_t.update(transfer_list[i] & transfer_list[j]) for i in range(len(transfer_list) - 1)
         for j in range(i + 1, len(transfer_list))]
        print(f'''Start stops: {len(bus_s)} {sorted(list(bus_s))}
Transfer stops: {len(bus_t)} {sorted(list(bus_t))}
Finish stops: {len(bus_f)} {sorted(list(bus_f))}''')

"""import json
import pprint
from collections import defaultdict


data = json.loads(input())

streets_buses = defaultdict(set)
buses_types = defaultdict(set)

for element in data:
    for k, v in element.items():
        if k == 'bus_id' and element['stop_name']:
            streets_buses[element['stop_name']] |= {v}
            buses_types[element[k]] |= {element['stop_type']}

# pprint.pprint(streets_buses, compact=True)
# pprint.pprint(buses_types, compact=True)

ids_missing_S_or_F = [k for k, v in buses_types.items() for typ in ('S', 'F') if typ not in v]

if ids_missing_S_or_F:
    print(f'There is no start or end stop for the line: {ids_missing_S_or_F[0]}.')
else:
    start_stop_names = set(element['stop_name'] for element in data if element['stop_type'] == 'S')
    finish_stop_names = set(element['stop_name'] for element in data if element['stop_type'] == 'F')
    transfer_stop_names = [street for street in streets_buses if len(streets_buses[street]) > 1]
    print(f'Start stops: {len(start_stop_names)} {sorted(list(start_stop_names))}')
    print(f'Transfer stops: {len(transfer_stop_names)} {sorted(transfer_stop_names)}')
    print(f'Finish stops: {len(finish_stop_names)} {sorted(list(finish_stop_names))}')
"""

"""import json
from collections import Counter

data = json.loads(input())
buses = {}

for line in data:
    buses.setdefault(line['bus_id'], {})
    buses.setdefault("BusID", set()).add(line['bus_id'])
    buses.setdefault('Transfer', []).append(line['stop_name'])

    if line['stop_type'] == "S":
        buses.setdefault('Start', []).append(line['stop_name'])
        buses[line['bus_id']].setdefault("SF", []).append(line['stop_name'])
    if line['stop_type'] == "F":
        buses.setdefault('Finish', []).append(line['stop_name'])
        buses[line['bus_id']].setdefault("SF", []).append(line['stop_name'])

    
    
yes = True
for onebus in buses['BusID']:
    a = len(buses[onebus]['SF'])
    if a != 2:
        print(f"There is no start or end stop for the line: {onebus}.")
        yes = False
        break


counts = Counter(buses['Transfer'])
counts = sorted([name for name, value in counts.items() if value > 1])

if yes:
    print(f"Start stops: {len(buses['Start'])} {sorted(list(buses['Start']))}")
    print(f"Transfer stops: {len(counts)} {counts}")
    print(f"Finish stops: {len(set(buses['Finish']))} {sorted(list(set(buses['Finish'])))}")"""
