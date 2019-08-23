# write and read with json
from json import dumps, dump, load, loads
print(repr(dumps(['hello', 'world'])))  # for viewing the json repr

# dump - write into a file using json
with open('tier3/new_json_file.txt', 'w+') as new_json_file_obj:
    dump("hello world json", new_json_file_obj)

# load - read from a file using json
with open('tier3/new_json_file.txt', 'r+') as old_json_file:
    print(loads(old_json_file))