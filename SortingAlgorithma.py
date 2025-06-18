# Bubble Sort
def bubble_sort(nums):
    nums = list(nums)
    for __ in nums:
        for i in nums:
            if nums[i] >= nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums


# Insertion Sort
def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        curr = nums.pop(i)
        j = i -1
        while j >= 0 and nums[j] > curr:
            j -= 1
        nums.insert(j+1, curr)
    return nums


# Merge Sort
def merge(nums1, nums2):
    merged = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        elif nums1[i] >= nums2[j]:
            merged.append(nums2[j])
            j += 1
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]
    return merged + nums1_tail + nums2_tail


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    sorted_nums = merge(left_sorted, right_sorted)
    return sorted_nums


# Quick Sort
def partition(nums, start=0, end=None):
    if end is None:
        end = len(nums) - 1
    l, r = start, end - 1
    while r > l:
        if nums[l] <= nums[end]:
            l += 1
        elif nums[r] > nums[end]:
            r -= 1
        else:
            nums[l], nums[r] = nums[r], nums[l]
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end


def quicksort(nums, start=0, end=None):
    if end is None:
        nums = list(nums)
        end = len(nums) - 1
    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot - 1)
        quicksort(nums, pivot + 1, end)
    return nums


# Here we learn how to make custom comparison functions to sort objects
class Notebook:
    def __init__(self, title, username, likes):
        self.title, self.username, self.likes = title, username, likes

    def __repr__(self):
        return 'Notebook <"{}/{}", {} likes>'.format(self.username, self.title, self.likes)


nb0 = Notebook('pytorch-basics', 'aakashns', 373)
nb1 = Notebook('linear-regression', 'siddhant', 532)
nb2 = Notebook('logistic-regression', 'vikas', 31)
nb3 = Notebook('feedforward-nn', 'sonaksh', 94)
nb4 = Notebook('cifar10-cnn', 'biraj', 2)
nb5 = Notebook('cifar10-resnet', 'tanya', 29)
nb6 = Notebook('anime-gans', 'hemanth', 80)
nb7 = Notebook('python-fundamentals', 'vishal', 136)
nb8 = Notebook('python-functions', 'aakashns', 74)
nb9 = Notebook('python-numpy', 'siddhant', 92)

notebooks = [nb0, nb1, nb2, nb3, nb4, nb5,nb6, nb7, nb8, nb9]


def compare_likes(nb1, nb2):
    if nb1.likes > nb2.likes:
        return 'lesser'
    elif nb1.likes == nb2.likes:
        return 'equal'
    else:
        return 'greater'


def default_compare(x, y):
    if x < y:
        return 'less'
    elif x == y:
        return 'equal'
    else:
        return 'greater'


def merge_objs(left, right, compare):
    i, j, merged = 0, 0, []
    while i < len(left) and j < len(right):
        result = compare(left[i], right[j])
        if result == 'lesser' or result == 'equal':
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]


def merge_sort_objs(objs, compare=default_compare):
    if len(objs) < 2:
        return objs
    mid = len(objs) // 2
    return merge_objs(merge_sort_objs(objs[:mid], compare), merge_sort_objs(objs[mid:], compare), compare)


sorted_notebooks = merge_sort_objs(notebooks, compare_likes)
print(sorted_notebooks)