# !-*- encoding=utf-8 -*-
class Node:
    def __init__(self, key, value):
        # 链表里存放键值对
        self.key = key
        self.value = value
        # 需要具备上下两个节点的引用
        self.prev = Node
        self.next = Node

    def __str__(self):
        val = '{%d,%d}' % (self.key, self.value)
        return val

    def __repr__(self):
        val = '{%d,%d}' % (self.key, self.value)
        return val


class DoubleLinkedList:
    def __init__(self, capacity=0xffff):
        """
        需要头部指针head和尾部指针tail和容积
        size用来存放已存节点
        :param capacity: 默认int最大值65535
        :return:
        """
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0

    # 从头部添加节点
    def __add_head(self, node):
        # 链表无节点，添加的节点就是链表头节点和尾节点
        if not self.head:
            self.head = node
            self.tail = node
            self.head.prev = None
            self.head.next = None
        # 不为空时，node的next指向头节点，下一节点的prev指向node，并维护node为头节点让它的prev指向null
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = None
        # 维护size++
        self.size += 1
        return node

    # 往尾部添加节点
    def __add_tail(self, node):
        # 链表为空，添加的节点尾节点
        if not self.tail:
            self.head = node
            self.tail = node
            self.tail.prev = None
            self.tail.next = None
        # 不为空时，node的prev指向尾节点，上一节点的next指向node，并维护node为尾节点让它的next指向null
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.tail.next = None
        # 维护size++
        self.size += 1
        return node

    # 从head端删除节点
    def __del_head(self):
        if not self.head:
            return
        node = self.head
        # 如果节点有下一个节点
        if self.head.next:
            self.head = node.next
            self.head.prev = None
        else:
            self.head = self.tail = None

        self.size -= 1
        return node

    # 从尾部删除节点
    def __del_tail(self):
        if not self.tail:
            return
        node = self.tail
        # 如果节点有前一个节点
        if node.prev:
            self.tail = node.prev
            self.tail.next = None
        else:
            self.head = self.tail = None

        self.size -= 1
        return node

    # 删除任意节点
    def __remove(self, node):
        # 如果node为空，默认删除尾部节点
        if not node:
            node = self.tail
        if node == self.tail:
            self.__del_tail()
        elif node == self.head:
            self.__del_head()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
        return node

    """
    提供给外部使用的api
    """

    # 默认头部删除
    def pop(self):
        return self.__del_head()

    # 默认尾部添加
    def append(self, node):
        return self.__add_tail(node)

    # 头部添加节点
    def append_front(self, node):
        return self.__add_head(node)

    # 删除节点
    def remove(self, node=None):
        return self.__remove(node)

    # 打印当前链表
    def print(self):
        p = self.head
        line = ""
        # p不为空
        while p:
            line += "%s" % p
            p = p.next
            if p:
                line += "=>"
        print(line)


if __name__ == '__main__':
    link = DoubleLinkedList(10)
    nodes = []
    # 生成0-9的键值对数组用来测试
    for i in range(10):
        node = Node(i, i)
        nodes.append(node)

    link.append(nodes[0])
    link.append(nodes[1])
    link.append(nodes[2])
    link.print()

    link.pop()
    link.print()

    link.append(nodes[5])
    link.append_front(nodes[7])
    link.print()

    link.remove(nodes[5])
    link.print()


