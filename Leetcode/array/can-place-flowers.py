class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed)==1 and flowerbed[0]==0 and n > 0:
            flowerbed[0] = 1
            n -= 1
        for i in range(len(flowerbed)):
            if n==0:break
            if flowerbed[i] == 0:
                if i==0 and flowerbed[i+1]==0:
                    flowerbed[i] = 1
                    n -= 1
                elif i==len(flowerbed)-1 and flowerbed[i-1]==0:
                    flowerbed[i] = 1
                    n -= 1
                elif flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    flowerbed[i] = 1
                    n -= 1
        #print(n)            
        return True if n==0 else False
        