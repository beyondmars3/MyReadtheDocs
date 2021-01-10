
def quanpailie():
    """
    全排列
    :return:
    """

    def run(data, begin, end):
        """
        [1, 2, 3, 4]
        :param data:
        :param begin:
        :param end:
        :return:
        """
        if begin >= end:
            print(data)
            return data

        for i in range(begin, end):
            data[i], data[begin] = data[begin], data[i]
            # print(data)
            run(data, begin+1, end)
            data[i], data[begin] = data[begin], data[i]

    run([1, 2, 3], 0, 3)


def erchashu():
    """
    二叉树
    :return:
    """

    class Node:
        def __init__(self, elem):
            self.elem = elem
            self.l_child = None
            self.r_child = None

    class Tree:
        """

        """

        def __init__(self):
            self.head = None

        def add(self, elem):
            """

            :param elem:
            :return:
            """
            node = Node(elem)
            if not self.head:
                self.head = node
                return

            # 找到最下面的节点，然后添加，从上到下，从左到右
            q = [self.head]
            while q:
                current = q.pop(0)
                if not current.l_child:
                    current.l_child = node
                    return
                if not current.r_child:
                    current.r_child = node
                    return
                q.append(current.l_child)
                q.append(current.r_child)

        def cengci(self):
            """
            层次遍历
            从上到下，从左到右
            :param current:
            :return:
            """
            current = self.head
            q = [current]
            while q:
                current = q.pop(0)
                print(current.elem)
                if current.l_child:
                    q.append(current.l_child)
                if current.r_child:
                    q.append(current.r_child)

        def qianxu(self, current):
            """
            前序遍历 根节点->左子树->右子树
            :return:
            """
            # current = self.head
            # q = [current]
            # while q:
            #     current = q.pop()
            #     print(current.elem)
            #     if current.r_child:
            #         q.append(current.r_child)
            #
            #     if current.l_child:
            #         q.append(current.l_child)

        def qianxu2(self, current):
            """
            递归 --
            :param current:
            :return:
            """
            if not current:
                return

            print(current.elem)
            self.qianxu2(current.l_child)
            self.qianxu2(current.r_child)

        def zhongxu2(self, current):
            """
            中序遍历 左子树->根节点->右子树
            :param current:
            :return:
            """
            if not current:
                return

            self.zhongxu2(current.l_child)
            print(current.elem)
            self.zhongxu2(current.r_child)

        def houxu2(self, current):
            """
            后序遍历 左子树->右子树->根节点
            :param current:
            :return:
            """
            if not current:
                return

            self.houxu2(current.l_child)
            self.houxu2(current.r_child)
            print(current.elem)

    t = Tree()

    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    t.add(6)
    t.add(7)

    # t.cengci()

    # t.qianxu2(t.head)

    # t.zhongxu2(t.head)

    t.houxu2(t.head)


def kuaipai():
    """
    快排 取出一个数，小的放左边，大的放右边
    :return:
    """

    def run(data):
        """
        快排 -- 递归实现
        :param data:
        :return:
        """
        if len(data) <= 1:
            return data

        first = data[0]
        left_arr = []
        right_arr = []
        for i in data:
            if i < first:
                left_arr.append(i)
            elif i > first:
                right_arr.append(i)

        left = run(left_arr)
        right = run(right_arr)
        res = left + [first] + right

        return res

    def run1(data, start, end):
        """
        快排 -- 优化实现 -- 拆东补西
        :param data:
        :param start:
        :param end:
        :return:
        """
        if start >= end:
            return

        low = start
        high = end
        first = data[low]
        while low < high:

            # 先从右边取出一个数子，和基准比较
            while low < high and data[high] > first:
                high -= 1
            data[low] = data[high]

            # 先从左边取出一个数子，和基准比较
            while low < high and data[low] < first:
                low += 1
            data[high] = data[low]

        # 然后补充基准
        data[low] = first

        run1(data, start, low)
        run1(data, low + 1, end)

    a = [11, 2, 16, 8, 10, 9]
    run1(a, 0, 5)
    print(a)


def maopao():
    """
    冒泡排序 -- 2个相邻的数比较
    :return:
    """

    def run(data):
        """
        pass
        :param data:
        :return:
        """
        for i in range(len(data)):
            for j in range(len(data) - i - 1):
                # 相邻的2个数比较
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]

        print(data)

    a = [11, 2, 16, 8, 10, 9]
    run(a)


def test():
    import os
    os.makedirs("/opt/a/b/c/d", exist_ok=True)


if __name__ == '__main__':
    """ __main__ """

    # quanpailie()

    # erchashu()

    # kuaipai()

    # maopao()

    test()
