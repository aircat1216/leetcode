class Solution:
    '''
    用了dict(hash)，本质2Sum的内核，实现简单，关键在不能有重复的答案
    先排序，然后遍历O(n^2),重复按3个和为0，2个和为0，一个和为0的遍历
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d={}
        result=[]
        for a in range (len(nums)):
            if nums[a] in d:
                d[nums[a]]+=1
            else:
                d[nums[a]]=1
        nums=sorted(set(nums))
        n=len(nums)
        if 0 in d and d[0]>2 :
            result.append([0,0,0])
        for a in range (n):
            for b in range(a+1,n):
                c=0-nums[a]-nums[b]
                if c in d:
                    if c==nums[a] and d[nums[a]]>=2:
                        result.append([nums[a],nums[b],c])
                    if c==nums[b] and d[nums[b]]>=2:
                        result.append([nums[a],nums[b],c])
                    elif c!=nums[a] and c!=nums[b] and c>nums[b]>nums[a]:
                        result.append([nums[a],nums[b],c])
                        
        return result
