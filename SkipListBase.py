import math
from random import randint

class SkipListBase:

    class Node:
        def __init__(self, key, left, right, below, above, value = None):
            self.key = key
            self.value = value
            self.left = left
            self.right = right
            self.above = above
            self.below = below

        def __repr__(self):
            return str(self.key)

    def __init__(self):
        #pamtim i levu i desnu granicu liste radi lagodnosti, iako u knjizi pise da je dovoljno samo levu
        self.leftBound = self.Node(-math.inf, None, None, None, None)
        self.rightBound = self.Node(math.inf, None, None, None, None)
        self.leftBound.right = self.rightBound
        self.rightBound.left = self.leftBound
        self.size = 0
        self.height = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    #algoritam za skip_search iz knjige
    def skip_search(self, k):
        left = self.leftBound
        row = self.leftBound
        while row.below is not None:
            left = left.below
            while left.right.key <= k:
                left = left.right
            row = row.below
        return left

    #algoritam iz knjige malo izmenjen jer mi nije bio jasan
    def add(self, k, v):
        left = self.skip_search(k)
        #ako smo nasli menjamo value i idemo ka gore i menjamo value
        if left.key == k:
            old = left.value
            left.value = v
            while left.above is not None and left.above.value == old:
                left.above.value = v
                left = left.above
            return left
        below = None
        i = -1
        below = self.insertAfterAbove(left, below, k, v)
        i += 1
        #insertujemo na donji nivo i dizemo granice na 2
        if i >= self.height:
            self.height += 1
            self.leftBound = self.insertAfterAbove(None, self.leftBound, -math.inf)
            self.rightBound = self.insertAfterAbove(self.leftBound, self.rightBound, math.inf)
            self.leftBound.right = self.rightBound
        self.size+=1
        #u while petlji nastavljamo da "bacamo novic" i da se penjemo i dizemo granice kad treba
        while randint(0, 1) == 1:
            i+=1
            if i >= self.height:
                self.height+=1
                self.leftBound = self.insertAfterAbove(None, self.leftBound, -math.inf)
                self.rightBound = self.insertAfterAbove(self.leftBound, self.rightBound, math.inf)
                self.leftBound.right = self.rightBound
            while left.above is None:
                left = left.left
            left = left.above
            below = self.insertAfterAbove(left, below, k, v)
        return below

    def insertAfterAbove(self, left, below, k, v = None):
        if left is not None:
            new = self.Node(k, left, left.right, below, None, v)
            if left.right is not None:
                left.right.left = new
            left.right = new
            if below is not None:
                below.above = new
            return new
        new = self.Node(k, None, None, below, None, v)
        below.above = new
        return new

    #skip search nadje node pa brisemo ka gore i prevezujemo svaki nivo usput
    def delete_node(self, k):
        curr = self.skip_search(k)
        if curr.key != k:
            raise ValueError("element not in map")
        while curr is not None:
            curr.left.right = curr.right
            curr.right.left = curr.left
            curr.right = None
            curr.left = None
            curr = curr.above
            if curr is not None:
                curr.below = None
        return curr

    def pop(self, k):
        curr = self.skip_search(k)
        if curr.key != k:
            return None
        while curr is not None:
            curr.left.right = curr.right
            curr.right.left = curr.left
            curr.right = None
            curr.left = None
            curr = curr.above
            if curr is not None:
                curr.below = None
        return curr

    def __iter__(self):
        left = self.leftBound
        right = self.rightBound
        while(left.below is not None):
            left = left.below
            right = right.below
        while left is not right:
            yield (left.key, left.value)
            left = left.right


    def __repr__(self):
        walk = self.leftBound
        lower = walk.below
        while lower is not None or walk is not None:
            while walk is not None:
                print(str(walk.key) + " ", end="")
                walk = walk.right
            print()
            walk = lower
            if lower is not None:
                lower = lower.below
        return ""
