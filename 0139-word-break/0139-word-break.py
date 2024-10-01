class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s))
        for i in range(len(s)):
            for word in wordDict:
                # Handle out of bounds case
                if i < len(word) - 1:
                    continue
                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1 : i + 1] == word:
                        dp[i] = True
                        break
        return dp[-1]

        # for i,x in enumerate(list(s)):
        #     word+=x 
        #     print(s[0:i],i)
        #     if word in set(wordDict) or s[:i] in set(wordDict):
        #         if word in set(wordDict):
        #             word=''
        #             dp[i]=True
        #             continue
        #         if s[:i] in set(wordDict):
        #             dp[i]=True
        #             continue
            

            

        print(dp)
        if word!='':
            for i in range(len(dp)):
                if dp[i]==True and s[i+1:] in wordDict:
                    return True
            return False
        return True
