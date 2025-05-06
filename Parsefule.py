import re

def extract_matches_from_file(filename, pattern):
    results = []
    regex = re.compile(pattern)

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            match = regex.search(line)
            if match:
                results.append(match.groupdict() or match.groups())

    return results
  
  # Пример строки: "User: alice, ID: 123"
pattern = r"User: (?P<username>\w+), ID: (?P<id>\d+)"

matches = extract_matches_from_file('example.txt', pattern)

for m in matches:
    print(m)
[{'username': 'alice', 'id': '123'}, {'username': 'bob', 'id': '456'}]
