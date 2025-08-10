impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut num_elements: usize = nums.len();
        let mut to_return: Vec<i32> = Vec::new();
        let mut index_1 : i32 = 0;
        loop {
            let element_1 :i32 = nums[index_1 as usize];
            let element_2_diff:i32 = target - element_1;
            let mut index_2 : i32 = index_1 + 1;
            loop {
                if nums[index_2 as usize] == element_2_diff {
                    to_return.push(index_1);
                    to_return.push(index_2);
                    return to_return;
                }
                index_2 += 1;
                if index_2 as usize == num_elements {
                    break;
                }
            }
            index_1 += 1;
        }
        return to_return;    
    }
}
