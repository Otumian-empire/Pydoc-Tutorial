# write and read with json
from json import dumps, dump, load, loads
# print(repr(dumps(['hello', 'world'])))  # for viewing the json repr

# # dump - write into a file using json
# with open('tier3/new_json_file.txt', 'w+') as new_json_file_obj:
#     dump("hello world json", new_json_file_obj)

# # load - read from a file using json
# with open('tier3/new_json_file.txt', 'r+') as old_json_file:
#     print(load(old_json_file))


my_dict = {
    'name': "john doe",
    'age': 23,
    'hobby': "programming",
    'profession': "web developer"
}

with open('tier3/dict_json_file.txt', 'w+') as old_json_file:
    dump(my_dict, old_json_file)

with open('tier3/dict_json_file.txt', 'r+') as old_json_file:
    my_dict = load(old_json_file)
    for key, value in my_dict.items():
        print(f"{key:10} ==> {value}")

# we'd look into deep into json and pickle