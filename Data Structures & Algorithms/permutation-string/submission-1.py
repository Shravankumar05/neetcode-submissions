class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # initialisation
        curr_map = {}
        target_map = Counter(s1)
        i = 0
        while i < len(s1):
            if s2[i] in curr_map:
                curr_map[s2[i]] += 1
            else:
                curr_map[s2[i]] = 1
            i += 1
        
        if curr_map == target_map:
            return True
        # iterate along until len(s2)-len(s1)
        i = 1
        while i <= (len(s2)-len(s1)):
            # remove the previous letter and add the new letter to the map
            prev_letter = s2[i-1]
            curr_map[prev_letter] -= 1
            if curr_map[prev_letter] == 0:
                del curr_map[prev_letter]


            new_char = s2[i+len(s1)-1]
            if new_char in curr_map:
                curr_map[new_char] += 1
            else:
                curr_map[new_char] = 1

            # check the map
            if curr_map == target_map:
                return True

            # iterate
            i += 1
        
        return False