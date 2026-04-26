class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #sort
        freq = {} #key: element, value: freq
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        arr = [] #List of tuple containing freq and number
        for n, freq in freq.items():
            arr.append([freq, n])
        arr.sort() #sort by frequency

        output = []
        while k > 0:
            output.append(arr.pop()[1])
            k -= 1
        return output