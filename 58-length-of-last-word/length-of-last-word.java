class Solution {
    public int lengthOfLastWord(String s) {
        String arr[]=s.split("\\s+");
        int n=arr.length;
        int k=arr[n-1].length();
        return k;
        
    }
}