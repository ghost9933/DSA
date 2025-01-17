class Solution:
    def maxArea(self, height: List[int]) -> int:
        vol=-math.inf
        # for i  in range(len(height)):
        #     for j in range(len(height)):
        #         if i!=j:
        #             h=min(height[i],height[j])
        #             w=abs(i-j)
        #             vol=max(vol,h*w)
        # return vol
        start=0
        end=len(height)-1
        while start<=end:
            h=min(height[start],height[end])
            w=end-start
            vol=max(vol,h*w)
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        return vol

            