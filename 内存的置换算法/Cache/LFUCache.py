from DoubleLinkedList import DoubleLinkedList, Node


class LFUNode(Node):
    """
    满足最不经常使用算法的节点,继承自Node
    """

    def __init__(self, key, value):
        """
        重写构造方法
        新增freq记录频次
        """
        self.freq = 0
        super(LFUNode, self).__init__(key, value)


class LFUCache:
    def __init__(self, capacity):
        """
        freq_map 频率的map 保存每一个频率以及它对应的双向链表
        """
        self.capacity = capacity
        self.size = 0
        self.map = {}
        # key: 频率, value: 频率对应的双向链表
        self.freq_map = {}

    def __update_freq(self, node):
        """
        更新频次
        """
        # 先获取频次
        freq = node.freq

        # 把节点从原来的双向链表中删除
        node = self.freq_map[freq].remove(node)
        if self.freq_map[freq].size == 0:
            # 如果链表为0 删除链表
            del self.freq_map[freq]

        # 更新频次并添加节点
        freq += 1
        node.freq = freq
        # 新频次不在freq_map中，需要新建链表
        if freq not in self.freq_map:
            self.freq_map[freq] = DoubleLinkedList()
        self.freq_map[freq].append(node)

    def get(self, key):
        # 如果key不在映射
        if key not in self.map:
            return -1
        node = self.map.get(key)
        # 更新节点频率 返回新的节点值
        self.__update_freq(node)
        return node.value

    def put(self, key, value):
        # 容量为0 返回
        if self.capacity == 0:
            return

        # 缓存命中 节点从映射中拿出来更新value（更新频次，在新的链表操作）
        if key in self.map:
            node = self.map.get(key)
            node.value = value
            self.__update_freq(node)

        # 缓存没有命中
        else:
            # 缓存满了淘汰节点
            if self.capacity == self.size:
                # 取出频率最低
                min_freq = min(self.freq_map)
                # 摘掉频率最低链表的头部节点
                node = self.freq_map[min_freq].pop()
                # 同步本地映射
                del self.map[node.key]
                self.size -= 1
            # 未满新建LFUNode 频次默认为1
            node = LFUNode(key, value)
            node.freq = 1
            # 缓存中保存node
            self.map[key] = node
            # 不在频次链表中，需要新建链表
            if node.freq not in self.freq_map:
                self.freq_map[node.freq] = DoubleLinkedList()
            # 在频次链表中，新增一个节点
            node = self.freq_map[node.freq].append(node)
            self.size += 1

    def print(self):
        print("##########")
        for k, v in self.freq_map.items():
            print("freq = {} : {}".format(k, self.freq_map[k].print()))
        print("##########")
        print()


if __name__ == '__main__':
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.print()

    print(cache.get(1))  # 获取1时使用1  1更新频次为2
    cache.print()

    cache.put(3, 3)  # 添加3时，移除频次为1的2，3频次为1
    cache.print()

    print(cache.get(2))  # 2以及移除，返回-1
    cache.print()

    print(cache.get(3))  # 获取3，3和1的频次都是2
    cache.print()

    cache.put(4, 4)  # 此时添加4，这时，3，1频次相同 FIFO删除1 并更新4频次为1
    cache.print()
