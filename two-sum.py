class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [];
        index = len(nums) - 1;
        i = 0;
        while i < index:
            u = i+1
            while u < index:
                soma = nums[i] + nums[u]
                if(soma == target):
                    result.append(i);
                    result.append(u);
                    return result;
                u+=1
            soma = nums[i] + nums[u]
            if(soma == target):
                result.append(i);
                result.append(u);
                return result;
            i+=1
        


s = Solution();
nums = [3,2,3]; 
target = 6;

print(s.twoSum(nums, target))