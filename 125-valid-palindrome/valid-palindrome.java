class Solution {
    public boolean isPalindrome(String s) {
       String s1="";
        for(char c: s.toCharArray())
        {
            if (Character.isLetterOrDigit(c))
            {
                s1+=Character.toLowerCase(c);
            }
        }
        return s1.equals(new StringBuilder(s1).reverse().toString());
        
    }
}