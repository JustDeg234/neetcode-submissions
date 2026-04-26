class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int) #key: element, value: freq
        for n in nums:
            hm[n] += 1
        
        #sort an array containing the num parsed by freq
        arr = []
        for n, freq in hm.items():
            arr.append([n, freq]) #if we insisit on this order, we can sort by freq by using lambda
        arr.sort(key = lambda x: x[1])
        #sorted(arr) generates a new list
        #arr.sort() #sorts original list

        k_list = []
        while len(k_list) < k:
            k_list.append(arr.pop()[0]) #[0] refers to first place in the element of array (list)
        return k_list