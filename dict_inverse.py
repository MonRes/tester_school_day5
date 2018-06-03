mapping = {'bar': 'foo', 'baz': 'foo', 'spam': 'eggs', 'b': 'eggs'}

reversed_map = {}

for key, value in mapping.items():
    if value not in reversed_map:
        reversed_map[value] = [key]
    else:
        reversed_map[value].append(key)

print(reversed_map)
