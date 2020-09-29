# 排序

## 快速排序
1. 参考 https://www.cnblogs.com/MOBIN/p/4681369.html
2. 
```python
def quick_sort_abc():
    """

    :return:
    """

    """
    选一个基准数字，
    从右边找到比基准小的数，放在左边指针处
    从左边找到比基准大的数，放在右边指针处
    不断把左右指针 往中间移动 
    """

    def run(arr_num, i, j):
        """

        :param arr_num:
        :param i: 开始索引
        :param j: 结束索引
        :return:
        """
        if i >= j:
            return

        pio = arr[i]
        low = i
        high = j

        while low < high:

            # 从右边拆一个数比较, 找到比 基准小的数
            while low < high and arr_num[high] > pio:
                high -= 1
            arr_num[low] = arr_num[high]

            # 然后从左边取一个数, 找到比 基准大的数
            while low < high and arr_num[low] < pio:
                low += 1
            arr_num[high] = arr_num[low]

        # 基准归位
        arr_num[low] = pio

        run(arr_num, i, low)
        run(arr_num, low + 1, j)

    arr = [12, 9, 2, 6, 7, 8, 3, 36, 22]
    run(arr, 0, len(arr) - 1)

    print(arr)
```

## 冒泡排序

1. 参考： https://blog.csdn.net/zcl_love_wx/article/details/83576962
2. 
```python
def maopao_sort():
    """
    冒泡排序
    :return:
    """

    def run(arr_num):
        """

        :param arr_num:
        :return:
        """

        for i in range(len(arr_num) - 1):
            for j in range(len(arr_num) - 1 - i):

                if arr_num[j] > arr_num[j + 1]:
                    arr_num[j], arr_num[j + 1] = arr_num[j + 1], arr_num[j]

        return arr_num

    arr = [12, 9, 2, 6, 7, 8, 3, 36, 22]
    run(arr)
    print(arr)
```

## 选择排序
1. https://www.jianshu.com/p/5223afa8796c
2. 
```python
def xuanze_sort():
    """
    
    :return:
    """

    def run(arr_num):
        """

        :return:
        """
        for i in range(len(arr_num)):

            for j in range(i + 1, len(arr_num)):

                if arr_num[i] > arr_num[j]:
                    arr_num[i], arr_num[j] = arr_num[j], arr_num[i]

    arr = [12, 9, 2, 6, 7, 8, 3, 36, 22]
    run(arr)
    print(arr)
```

## 找出最小的不重复的子字符串和长度 -- 滚动窗口
1. 比如在 "abcdaebf" 找到 最长的子串 "cdaebf"

```python
def main():
    """

    :return:
    """
    # data_str = "rgflkafmngoDALDPFKMACr".lower()
    data_str = "abcdaebf"

    start, end = 0, 0
    res = []
    res_dict = {}

    while end < len(data_str):
        last = res_dict.get(data_str[end])
        res_dict[data_str[end]] = end
        # 重复的时候,左边界加一
        if last is not None:
            start = last + 1
        else:
            res.append(data_str[start:end+1])
        end += 1

    max_len = 0
    for r in res:
        max_len = max(max_len, len(r))
    
    return res, max_len
```

## 斐波那契

