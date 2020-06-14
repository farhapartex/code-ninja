class Solution:
    def product_arr(self, index, init, nums):
        init = init * nums[index-1]
        if index == len(nums)-1:
            temp = nums[index]
            nums[index] = init
            end = temp
            return end
        end = self.product_arr(index+1, init, nums)
        temp = nums[index]
        nums[index] = end * init
        #print(end*init)
        end  =  end * temp
        
        return end
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        end = self.product_arr(1,1, nums)
        nums[0] = end
        return nums
        
        