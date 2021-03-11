counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

sample_list = ["a","b","c","d"]
dict1 = {}
i=0
for name in sample_list:
    dict1[name] = i
    i = i+1

print(dict1)
# for county in counties_dict.keys():
#     print(county)