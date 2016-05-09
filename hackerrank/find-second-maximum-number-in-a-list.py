n = int(input())
nums = sorted(list(set(map(int, input().split()))))

print(nums[len(nums)-2])