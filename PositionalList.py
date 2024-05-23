from SkipListBase import SkipListBase

class PositionalListMap(SkipListBase):

    class Position:
        def __init__(self, container, node):
            self.container = container
            self.node = node

        def element(self):
            return (self.node.key, self.node.value)

        def __eq__(self, other):
            return type(other) is type(self) and other.node is self.node

        def __ne__(self, other):
            return not self == other

        def __repr__(self):
            return str(self.node)

    def validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("Position p must be type Position")
        if p.container is not self:
            raise ValueError("Position p does not belong to this container")
        if p.node.next is None:
            raise ValueError("Position p is no longer valid")
        return p.node

    def make_position(self, node):
        if node is self.leftBound or node is self.rightBound:
            return None
        else:
            return self.Position(self, node)

    def __getitem__(self, item):
        node = self.skip_search(item)
        if node.key != item:
            raise ValueError("item not found in map")
        return self.make_position(node)

    def __setitem__(self, key, value):
        node = self.add(key, value)
        return self.make_position(node)

    def __delitem__(self, key):
        node = self.delete_node(key)

    def __contains__(self, item):
        node = self.skip_search(item)
        if node.key == item:
            return True
        return False

    def get(self, k):
        node = self.skip_search(k)
        if node.key != k:
            return None
        return self.make_position(node)

    def pop(self, k):
        node = self.pop(k)
        return self.make_position(node)

    def popItem(self):
        node = self.leftBound.below.right
        self.pop(node.key)
        return self.make_position(node)

    def clear(self):
        node = self.leftBound
        below = self.rightBound
        while node.below is not None:
            node = node.below
            below = below.below
        node = node.right
        walk = node.right
        while node is not below:
            self.delete_node(node.key)
            node = walk
            walk = walk.right

    def keys(self):
        sett = set()
        node = self.leftBound
        below = self.rightBound
        while node.below is not None:
            node = node.below
            below = below.below
        node = node.right
        while node is not below:
            sett.add(node.key)
            node = node.right
        return sett

    def values(self):
        sett = set()
        node = self.leftBound
        below = self.rightBound
        while node.below is not None:
            node = node.below
            below = below.below
        node = node.right
        while node is not below:
            sett.add(node.value)
            node = node.right
        return sett

    def items(self):
        sett = set()
        node = self.leftBound
        below = self.rightBound
        while node.below is not None:
            node = node.below
            below = below.below
        node = node.right
        while node is not below:
            sett.add((node.key, node.value))
            node = node.right
        return sett

    def __eq__(self, other):
        node = self.leftBound
        below = self.rightBound
        node2 = other.leftBound
        below2 = other.rightBound
        while node.below is not None:
            node = node.below
            below = below.below
        while node2.below is not None:
            node2 = node2.below
            below2 = below2.below
        node = node.right
        node2 = node2.right
        while node is not below:
            if node.key is not node2.key or node.value is not node2.value:
                return False
            node = node.right
            node2 = node2.right
        return True

    def __ne__(self, other):
        return not self.__eq__(self, other)