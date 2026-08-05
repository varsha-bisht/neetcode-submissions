func findMaxConsecutiveOnes(nums []int) int {
    result, count := 0, 0
    for _, num := range nums{
      if num == 1 {
          count+=1
      } else{
        count=0
      }
      if count > result {
        result = count
      }
    }
    return result

}
