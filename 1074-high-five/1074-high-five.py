class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students={}
        for item in items:
            
            if item[0] in students:
                heappush(students[item[0]], item[1])
                if len(students[item[0]])>5:
                    x=heappop(students[item[0]])
                    print('added',item[1],'removed',x)
            else:
                students[item[0]]=[item[1]]
        # # 
        # for x in students:
        #     # print(x,students[x])
        ans=[]
        def topKavg(heap,k):
            sum=0
            c=0
            heapify(heap)
            for i in range(k):

                if not heap:
                    break
                c+=1
                kth=-heappop(heap)
                # print(c,kth)
                sum+=kth
            if c:
                return sum//c
            return 0
        for student in students:
            print('curr student',student)
            print(students[student])
            x=sum(students[student])//len(students[student])
            # x=topKavg(students[student],5)
            ans.append([student,x])
        return sorted(ans,key=lambda x:x[0])
            