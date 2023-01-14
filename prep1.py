n = int(input())
nums = list(map(int,input().split()))
q = int(input())
commands = []
for i in range(q):
    commands.append(list(map(int,input().split())))
for c in commands:
    if c[0]==1:
        nums[c[1]-1]=c[2]
        print(sum(nums))
    elif c[0]==2:
        nums1=nums[-c[1]:]
        nums2=(nums[:n-c[1]])
        nums=nums1
        nums.extend(nums2)
        print(sum(nums))
