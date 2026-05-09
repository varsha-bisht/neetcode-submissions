func twoSum(nums []int, target int) []int {
 
ans := make([]int,0)
	for i, _ := range nums{
		for j, _ := range nums{
			if i !=j {
            if nums[i] + nums[j] == target{
            return append(ans, i, j)
		  }
			} 
		}
	}
return ans
}
