from copy import deepcopy


def run():
    """
    全排列
    :return:
    """
    # [1, 2, 3, 4]

    # def perm(data, begin, end):
    #     if end - begin == 0:
    #         print(data)
    #     else:
    #         for i in range(begin, end):
    #             data[i], data[begin] = data[begin], data[i]
    #             perm(data, begin + 1, end)
    #             data[i], data[begin] = data[begin], data[i]
    #
    # arr = [1, 2, 3]
    # perm(arr, 0, len(arr))

    # def backtrack(path, nums):
    #     if not nums:
    #         print(path)
    #         return
    #
    #     for i in range(len(nums)):
    #         path.append(nums[i])
    #         backtrack(path, nums[:i] + nums[i + 1:])
    #         path.pop()
    #
    # backtrack([], [1, 2, 3])
    #
    # print("----")
    #
    # b = [1, 2, 3, 4, 5]
    # print(b[:1])
    # print(b[2:])

    a = "abcddac"

    res = {}

    def no_chongfu():
        """

        :return:
        """
        start = 0
        end = 0
        for i in range(len(a)):
            _pass = None


if __name__ == '__main__':

    """ main """

    run()
