import json

json_data_file = "test.json"

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

# write json to a file
with open(json_data_file, "w") as write_file:
    json.dump(data, write_file, indent=4, separators=(',', ': '), sort_keys=True)
    #add trailing newline for POSIX compatibility
    write_file.write('\n')

# write json to a python string
# if you don't need to pretty-print, you can skip the "indent/separators/sort_keys" bit
json_string_ex = json.dumps(data, indent=4, separators=(',', ': '), sort_keys=True)
print(json_string_ex)

# load json string into python objects
json_python_structure = json.loads(json_string_ex)
print(type(json_python_structure))
