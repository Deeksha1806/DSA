class Solution {
    public String capitalizeTitle(String title) {
        String [] arr=title.split(" ");
        for(int i=0;i<arr.length;i++)
        {
            if(arr[i].length()<=2)
            {
                arr[i]=arr[i].toLowerCase();
            }
            else
            {
               arr[i]=arr[i].substring(0,1).toUpperCase()+arr[i].substring(1).toLowerCase();
             }
         } String result = String.join(" ",arr);
            return result;
        }
        
    }
        
    
