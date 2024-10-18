class Solution {
    public boolean canPermutePalindrome(String s) {
        HashMap<Character,Integer> charMap=new HashMap<>();

        for(char c:s.toCharArray()){
            charMap.put(c,charMap.getOrDefault(c,0)+1);
        }
        int oddCount=0;
        for(int val:charMap.values()){
            if (val%2!=0){
                oddCount+=1;
            }
        }
        return oddCount<=1;
    }
}