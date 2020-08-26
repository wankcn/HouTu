from DoubleLinkedList import DoubleLinkedList, Node


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}  # 保存key与节点的映射关系
        self.list = DoubleLinkedList(self.capacity)

    def get(self, key):
        """
        如果节点在缓存里，把节点重新保存添加到头部，并删除原来节点
        """
        if key in self.map:
            node = self.map[key]
            self.list.remove(node)
            self.list.append_front(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        # key在缓存里 把节点拿出来更新
        if key in self.map:
            node = self.map.get(key)
            self.list.remove(node)
            node.value = value
            self.list.append_front(node)
        else:
            # 不在缓存创建新的节点
            node = Node(key, value)
            # 缓存已经满了且不再缓存里，删除掉尾部节点,变成了缓存未满
            if self.list.size >= self.list.capacity:
                old_node = self.list.remove()
                self.map.pop(old_node.key)
            self.list.append_front(node)
            self.map[key] = node

    def print(self):
        print(self.list.print())


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.print()
    cache.put(2, 2)
    cache.print()
    cache.put(3, 3)
    cache.print()

    print(cache.get(1))  # 此时1由于最少使用已经移除返回-1

    print(cache.get(2))  # 此时获取2已经是再次使用2，2放在头部
    cache.print()
