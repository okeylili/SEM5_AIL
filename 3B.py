states = {
  "MH" : ["GJ","GA","KA","MP","TG"],
  "KA" : ["MH", "TG", "GA"],
  "GA" : ["MH","KA"],
  "GJ" :["RJ","MH", "MP"],
  "TG" : ["MH", "KA"],
  "MP" : ["GJ", "RJ", "MH"],
  "RJ" : ["GJ", "MP"]
}

colors = ["Red", "Blue", "Green"]

color = {}

def solve(state):
  if state == len(states):
    return True
  s = list(states.keys())[state]
  for c in colors:
    if all(color.get(n) != c for n in states[s]):
      color[s]=c
      if solve(state+1):
        return True
      del color[s]
  return False

while(True) :
  print("\n1. color map")
  print("2. Show map")
  print("3. Exit")
  ch = int(input("Enter your choice: "))

  if ch == 1:
    color = {}
    if solve(0):
      print("Map coloured successfully")
    else:
      print("No solution")

  elif ch == 2:
    for s in color:
      print(s, "->", color[s])

  elif ch == 3:
    break

  else:
    print("Invalid choice")
