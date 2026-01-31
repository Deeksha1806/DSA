class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        ArrayList<Integer>arr=new ArrayList<>();
        for(int i:nums1)
        {
            for(int j:nums2)
            {
                if(i==j && !arr.contains(i))

                {
                  arr.add(i);
                }
            }
        }
        int [] l=new int[arr.size()];
        for(int i=0;i<arr.size();i++)
        {
            l[i]=arr.get(i);
        }

        return l;
        
    }
}