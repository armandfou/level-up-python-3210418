def sort_string(str):
  return' '.join(sorted(str.split(" "), key=lambda s: s.lower()))

print(sort_string('banana ORANGE apple'))