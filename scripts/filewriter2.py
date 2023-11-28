from collections import defaultdict

result = defaultdict(list)

for dic in d:
  id = dic.pop("serviceID")
  result[id].append(dic)