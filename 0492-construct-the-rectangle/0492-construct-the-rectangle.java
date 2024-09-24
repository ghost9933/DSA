class Solution {
    public int[] constructRectangle(int area) {
        int ans[]=new int[2];
        int j=(int)Math.sqrt(area);
        int l=1,w=1,diff=Integer.MAX_VALUE;
        for(int i=1;i<=j;i++){
            if (area%i==0){
                int a=i;
                int b=area/i;
                if (Math.abs(a-b)<diff){
                    diff=Math.abs(a-b);
                    l=Math.max(a,b);
                    w=Math.min(a,b);
                }
            }
        }
        ans[0]=l;
        ans[1]=w;
        return ans ;
    }
}