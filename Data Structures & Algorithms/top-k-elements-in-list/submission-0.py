class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [0] * 2001
        for num in nums: 
            freq[num+1000] += 1
        count = []
        for idx, cnt in enumerate(freq):
            if cnt > 0:
                org_num = idx - 1000
                count.append((cnt, org_num))

        count.sort(reverse=True)

        ans = []

        for i in range(k): 
            ans.append(count[i][1])
        return ans