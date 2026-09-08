class Solution {
    public int thirdMax(int[] nums) {
        int largest=Integer.MIN_VALUE;
        int second=Integer.MIN_VALUE;
        int third=Integer.MIN_VALUE;
        HashSet<Integer> p=new HashSet<>();
        for(int num:nums)
        {
            p.add(num);
        }
        int def=p.iterator().next();
        for(int num:p)
        {
            if(num>def)
            def=num;
        }

        if(p.size()<3)
        return def;

        
        for(int num:p)
        {
            if(num==largest||num==second||num==third)
            continue;
            if(num>largest){
            third=second;
            second=largest;
            largest=num;
            }
            else if(num>second)
            {
                third=second;
                second=num;
            }
            else if(num>third)
            {
                third=num;
            }
            
        }
        return third;
    }
}