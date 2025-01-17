class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        skip=0
        for i in range(len(nums)):
            x=nums.pop(0)
            print(x)
            if x==0:
                skip+=1
            else:
                nums.append(x)
            # i+=1
        for i in range(skip):
            nums.append(0)
        return nums