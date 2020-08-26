"""
实现FIFO缓存置换算法
"""
from DoubleLinkedList import DoubleLinkedList, Node


class FIFOCache:
    def __init__(self, capacity):
        """
        size记录已缓存大小
        map保存key和node的映射关系
        :param capacity: 当前缓存可容纳最大缓存数量
        """
        self.capacity = capacity
        self.size = 0
        self.map = {}
        self.list = DoubleLinkedList(self.capacity)

    def get(self, key):
        """
        判断key的节点是否在缓存里面，在返回value，不再返回-1
        :param key:
        :return:value或-1
        """
        if key not in self.map:
            return -1
        else:
            # 从map里拿出key所对应的node
            node = self.map.get(key)
            return node.value

    def put(self, key, value):
        """
        首先判断缓存容量 0直接返回说明缓存无法保存数据
        判断key是否已经存在缓存里
        存在把旧的node拿出来更新value 删除旧节点，添加新的节点
        不存在先判断缓存是否满 (满先pop头部节点，在添加尾部，不满直接添加尾部)
        :param key:
        :param value:
        :return:
        """
        if self.capacity == 0:
            return
        if key in self.map:
            node = self.map.get(key)
            # 删除旧节点
            self.list.remove(node)
            # 新节点默认添加尾部
            node.value = value
            self.list.append(node)
        else:
            if self.size == self.capacity:
                node = self.list.pop()
                # 在本地map映射中删除节点
                del self.map[node.key]
                self.size -= 1
            node = Node(key, value)
            self.list.append(node)
            # 同时本地映射缓存保存key和node
            self.map[key] = node
            self.size += 1

    def print(self):
        # 打印当前链表内容
        print(self.list.print())


if __name__ == '__main__':
    cache = FIFOCache(2)
    cache.put(1, 1)
    cache.print()
    cache.put(2, 2)
    cache.print()

    print(cache.get(1))

    cache.put(3, 3)
    cache.print()

    print(cache.get(4))  # 没有得到-1

    cache.put(4, 4)
    cache.print()
