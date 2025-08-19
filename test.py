import math
from functools import reduce
from collections import Counter, deque, defaultdict
from datetime import datetime
import json

# numbers = [1, 5, 54, 12, 66]
# evens = filter(lambda x: x%2 == 0, numbers)
# squares = map(lambda x: math.pow(x,2), evens)
# sum = reduce(lambda a, b: a+b, squares)

# print(sum)

word = "mississippi"
letters = []
group = defaultdict(list)
    
for w in word:
    group[w[0]].append(w)

print(group)
print(Counter(word))

data = {
    "name": "namura",
    "skills": "none"
}

print(json.dumps(data))
print(datetime.now())

