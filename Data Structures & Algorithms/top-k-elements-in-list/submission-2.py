class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Solution was utilising bucket sort, which requires you
        splitting the original input list into 'buckets', sorting
        each of those buckets, and merging them back into a full
        list.

        Though I don't think we need the 'sorting' step here. The
        point is to put the frequency counts as the 'buckets',
        and put the numbers in thier respective buckets, keeping
        the top k buckets.
        """

        counts_hash: dict[int, int] = {}
        for i in nums:
            if i not in counts_hash:
                counts_hash[i] = 1
            else:
                counts_hash[i] += 1

        print(counts_hash)
        # create ordered list, which will be our 'buckets'
        # 0 up to the highest count
        max_count: int = 0
        for i in counts_hash.keys():
            if counts_hash[i] > max_count:
                max_count = counts_hash[i]
        
        print(max_count)
        # lists are mutable (can change value in memory), so doing [[]] * max_count
        # creates 3 lists with the same memory, so changing 1 list changes them all.
        # hence we do list comprehension (with 3 seperate lists)
        bucket: list[list[int]] = [[] for _ in range(max_count)]
        print(bucket)
        # this doesn't consider if 2 different nums have same count
        # but will go ahead to see what the tests say
        # now got to consider it lol..
        for i in counts_hash.keys():
            bucket[counts_hash[i] - 1].append(i) # count of 3 is at index 2

        print(bucket)
        # need to remove all empty lists
        non_empty_bucket_list: list[list[int]] = []
        for l in bucket:
            if len(l) != 0:
                non_empty_bucket_list.append(l)
        
        # double loop, but still O(n)
        flat_list: list[int] = [num for bucket in non_empty_bucket_list for num in bucket]
        print(flat_list)
        return flat_list[-k:]











