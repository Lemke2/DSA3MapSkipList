from PositionalList import PositionalListMap
import math

class SortedMap(PositionalListMap):

    #O(log(n)) jer je min na prvom mestu posle headera skroz donjeg nivoa, znaci samo visinu pretrazujemo
    def find_min(self):
        node = self.leftBound
        right = self.rightBound
        while node.below is not None:
            node = node.below
            right = right.below
        node = node.right
        if node is not right:
            return self.make_position(node)
        return None

    #analogno findmin samo s desne strane (zbog ovoga izmedju ostalog pamtim rightbound u skipListBase)
    def find_max(self):
        node = self.leftBound
        right = self.rightBound
        while node.below is not None:
            node = node.below
            right = right.below
        right = right.left
        if right is not node:
            return self.make_position(right)
        return None

    #skipsearch nalazi <= element, ako jednako idemo ka levo jer trazimo strogo manji
    def find_lt(self, k):
        node = self.skip_search(k)
        if node.key == k:
            node = node.left
        if node.key == -math.inf:
            return None
        return self.make_position(node)

    #ovde skipsearch vraca tacno sta trazimo
    def find_le(self, k):
        node = self.skip_search(k)
        if node.key == -math.inf:
            return None
        return self.make_position(node)

    #skipsearch vraca <= pa moramo ka desno, da bi bili strogo veci
    def find_gt(self, k):
        node = self.skip_search(k)
        node = node.right
        if node.key == math.inf:
            return None
        return self.make_position(node)

    #skipsearch vraca <= pa gledamo =, ili idemo desno
    def find_ge(self, k):
        node = self.skip_search(k)
        if node.key == k:
            return self.make_position(node)
        node = node.right
        if node.key == math.inf:
            return None
        return self.make_position(node)


    def find_range(self, start, stop):
        if start is None:
            start = -math.inf
        if stop is None:
            stop = math.inf
        node = self.skip_search(start)
        if node.key < start:
            node = node.right
        if node == math.inf:
            yield None
        while node.key >= start and node.key < stop:
            node = node.right
            yield (node.key, node.value)

    #Iter samo idemo po donjem nivou
    def iter(self):
        left = self.leftBound
        right = self.rightBound
        while (left.below is not None):
            left = left.below
            right = right.below
        while left is not right:
            yield (left.key, left.value)
            left = left.right

    #Isto, samo s desna ka levo
    def __reversed__(self):
        left = self.leftBound
        right = self.rightBound
        while (left.below is not None):
            left = left.below
            right = right.below
        while right is not left:
            yield (right.key, right.value)
            right = right.left



