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
