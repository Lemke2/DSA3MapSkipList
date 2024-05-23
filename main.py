from SortedMap import SortedMap

if __name__ == '__main__':
   psl2 = SortedMap()
   psl2[10] = "a"
   psl2[7] = "b"
   psl2[1] = "c"
   psl2[2] = "d"
   psl2[8] = "e"
   psl2[6] = "ggg"
   psl2.delete_node(7)
   psl2.add(5, "f")
   print(psl2)
   print(psl2.keys())
   print(psl2.values())
   print(psl2.items())
   psl2[6] = "g"
   print(psl2)
   print(psl2.find_min())
   print(psl2.find_max())
   print(psl2.find_lt(8))
   print(psl2.find_le(8))
   print(psl2.find_gt(5))
   print(psl2.find_ge(5))
   for el in psl2.find_range(4,10):
      print(el, end="")
   print()
   #-------------------------------------------#
   psl = SortedMap()
   psl.add(10, "a")
   psl.add(7, "b")
   psl.add(1, "c")
   psl.add(2, "d")
   psl.add(8, "e")
   psl[6] = "g"
   psl.delete_node(7)
   psl.add(5, "f")
   print(psl)
   print(psl.__eq__(psl2))
   psl.clear()
   print(psl)