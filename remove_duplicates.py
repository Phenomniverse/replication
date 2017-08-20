def remove_duplicates(items):
  duplicates_removed = []
  for i in items:
    if i not in duplicates_removed:
      duplicates_removed.append(i)
  return duplicates_removed

print remove_duplicates(['a','b','c','d','a','e','b','x','a'])
a =['a','b','c','d','a','e','b','x','a']
print 'b' not in a
print 't' not in a
