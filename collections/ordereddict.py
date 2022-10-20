from collections import OrderedDict

n = int(input());
ordered_dict = OrderedDict();

for i in range(n):
    item = input().split()
    item_price = int(item[-1])
    item_name = " ".join(item[:-1])
    if(ordered_dict.get(item_name)):
        ordered_dict[item_name] += item_price
    else:
        ordered_dict[item_name] = item_price

for i in ordered_dict.keys():
    print(i, ordered_dict[i])