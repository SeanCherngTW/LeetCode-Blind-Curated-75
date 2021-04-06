class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        base_idx = ord('a')
        counter = [0] * 26
        for char in s:
            char_idx = ord(char) - base_idx
            counter[char_idx] += 1

        for char in t:
            char_idx = ord(char) - base_idx
            counter[char_idx] -= 1

        for count in counter:
            if count != 0:
                return False

        return True
