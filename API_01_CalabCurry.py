# https://www.youtube.com/watch?v=qbLc5a9jdXo&t=1229s

# https://www.youtube.com/watch?v=1lxrb_ezP-g&t=2s (Corey Schafer)

import requests
import json
import time

# response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
response = requests.get('https://formulae.brew.sh/api/formula.json')
# print(response.json())
response_json = response.json()  # this is a list

response_str = json.dumps(response_json, indent=2)  # this is a string
# print(type(response_str))

print(len(response_json))
# print(response_str)
exit(0)
# package_name = response.json()[0]['name']
# package_desc = response.json()[0]['desc']

results = []
i = 0
t1 = time.perf_counter()
for package in response_json:
    package_name = package['name']
    package_desc = package['desc']
    package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'

    response = requests.get(package_url)

    response_json = response.json()
    installs_30 = response_json['analytics']['install_on_request']['30d'][package_name]
    installs_90 = response_json['analytics']['install_on_request']['90d'][package_name]
    installs_365 = response_json['analytics']['install_on_request']['365d'][package_name]
    # response_str = json.dumps(response_json, indent=2)

    data = {
        'name': package_name,
        'desc': package_desc,
        'url': package_url,
        'analytics': {
            '30d': installs_30,
            '90d': installs_90,
            '365d': installs_365
        }
    }
    results.append(data)
    # time.sleep(2)
    time.sleep(response.elapsed.total_seconds())
    # break
    i += 1
    if i > 10:
        break
t2 = time.perf_counter()

# print(json.dumps(results, indent=2))
print("TOTAL TIME:", t2 - t1, "SEC")

# SAVING results TO JSON FILE
with open('package_info.json', 'w') as f:
    json.dump(results, f, indent=2)


# CALLING TO LOAD previous JSON FILE

def install_sort(package):
    return package['analytics']['30d']


def call_to_load_json():
    with open("package_info.json", "r") as f1:
        data_load = json.load(f1)
    # print(json.dumps(data_load,indent=2))
    # data_load = [item for item in data_load if 'gai' in item['desc']]
    data_load.sort(key=install_sort, reverse=True)
    print(json.dumps(data_load, indent=2))
    for ii in data_load:
        print(ii['name'], ":", ii['desc'])


call_to_load_json()

exit(0)

print(response.json()['items'])
for data in response.json()['items']:
    print(data['title'])
    print(data['link'])
    print()
