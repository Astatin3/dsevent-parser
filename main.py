import sys
import re

def split_with_xml_tags(text):
  pattern = r'(<[^/][^>]*>)|([^<]+)'
  matches = re.findall(pattern, text)
  return [match[0] if match[0] else match[1] for match in matches]

array = []

with open(sys.argv[1], 'r') as f:
  data = f.read()
  log_data = split_with_xml_tags(data)

  data = [None, None, None]
  type_id = -1
  for i, log in enumerate(log_data):
    match log:
      case "<TagVersion>":
        type_id = 0
        continue
      case "<time>":
        type_id = 1
        continue
      case "<message>":
        type_id = 2
        continue

    if type_id == 0:
      array.append(data)
      data = [None, None, None]

    data[type_id] = log


for line in array:

  if None in line:
    continue

  if not "Drive" in line[2]:
    continue

  if not sys.argv[2] in line[2].split(",")[0]:
    continue
  if not sys.argv[3] in line[2].split(",")[0]:
    continue

  for i, col in enumerate(line):
    match i:
      case 0:
        print(col.split(" ")[0], end=',')
        continue
      case 1:
        print(col.split(" ")[1], end=',')
        continue
      case 2:
        print(col.split(" ")[4], end=',')
        continue

  print("\n", end='')