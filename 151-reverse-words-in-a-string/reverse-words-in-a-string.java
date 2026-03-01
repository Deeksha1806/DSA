class Solution {
    public String reverseWords(String s) {
        
        String[] arr= s.trim().split("\\s+");
         int n=arr.length-1;
        String [] a= new String[arr.length];
        for(int i=0;i<a.length;i++)
        {
           a[i]=arr[n-i];
        }
        String k= String.join(" ",a);
        return k;
    }
}