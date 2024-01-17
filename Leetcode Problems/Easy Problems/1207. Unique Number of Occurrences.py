class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Count occurrences using a dictionary
        occ_map = {}
        for num in arr:
            occ_map[num] = occ_map.get(num, 0) + 1

        unique = set(occ_map.values())
        return len(unique) == len(occ_map)