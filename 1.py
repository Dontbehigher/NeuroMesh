def minSub(source, target):
    sourceSet = set(source)
    for char in target:
        if char not in sourceSet:
            return -1
    count = 0
    index = 0
    while index < len(target):
        current_index = 0
        count += 1
        # 双指针遍历判断
        while current_index < len(source) and index < len(target):
            if source[current_index] == target[index]:
                index += 1
            current_index += 1
    return count

source = input("source :")
target = input("target:")
print(minSub(source,target))