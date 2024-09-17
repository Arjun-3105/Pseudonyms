import collections

text = input("Enter a string for counting occurences of the letters: ")
res = dict()
leter_counter = collections.Counter(x.lower() for x in text if x.isalpha())
res.update(leter_counter)
result = dict()
for letter in res:
    temp = []
    for i in range(res[letter]):
        temp.append(letter)
    result[letter] = temp
sorted_res = dict(sorted(result.items()))
print(sorted_res)