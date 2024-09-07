def index_all(array, search):
  print("array " , array)
  tab = []
  for i, value in  enumerate(array):
    if (type(value) == list and value != search):
        tabList = []
        a = index_all(value, search)
        if (a):
          for n in  a:
            if (type(n) == list):
              n.append(i)
              tabList.append(n)
            else:
              tabList.append([i,n])
          for tabListItem in tabList:
            tab.append(tabListItem)
          print("ddd tab " , tab, "array " , array, "value" , value, " a = " , a)
    else:
      if (value == search):
        tab.append(i)
  print("array " , array, "tab " , tab, "value" , value)
  return tab
      
# example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
print(index_all(example, 2))  # [[0, 0, 1], [0, 1], [1, 1]]
print(index_all(example, [1, 2, 3]))  # [[0, 0], [1]]