"""
imagine we have a robot for walking

"""
command = ["right 20", "right 30", "left 50", "up 10", "down 20"]

x = 0
y = 0

for i in range(len(command)):

  if command[i].startswith("r"): x += int(command[i].split()[1])

  elif command[i].startswith("l"): x -= int(command[i].split()[1])

  elif command[i].startswith("u"): y += int(command[i].split()[1])

  elif command[i].startswith("d"): y -= int(command[i].split()[1])

[x, y]   # we can read print as a coordinate

