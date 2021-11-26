"""https://www.youtube.com/watch?v=9N6a-VLBa2I"""

import json
from urllib.request import urlopen

# READ json FROM DICTIONARY
my_dict = {
    "people": [
        {
            "name": "Peter", "age": 50, "weight": 150
        },
        {
            "name": "June", "age": 45, "weight": 120
        },
        {
            "name": "John", "age": 17, "weight": 160
        },
    ]
}
data_json = json.dumps(my_dict, indent=2)
print(data_json)
exit(0)

# READING json FROM FILE
with open("states.json", "r") as f:
    data = json.load(f)

print(json.dumps(data, indent=2))
# print(type(data))
for state in data['states']:
    # print(state['name'],state['abbreviation'])
    del state['area_codes']

# WRITE json TO FILE
with open("new_states.json", "w") as f:
    json.dump(data, f, indent=2)

# READING json FROM URL
# https://www.youtube.com/watch?v=LosIGgon_KM
print("#################")
with urlopen("http://www.wikipedia.org/") as response:
    source = response.read()
    html = source.decode("UTF-8")
print(response.code, response.length)
print(type(html))
# exit(0)
data = json.loads(html)
print(json.dumps(data, indent=2))
