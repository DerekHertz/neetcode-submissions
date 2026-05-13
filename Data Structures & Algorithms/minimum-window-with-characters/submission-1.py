class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_count = {}
        for i in t:
            t_count[i] = t_count.get(i, 0) + 1

        # number of unique characters
        required = len(set(t))
        formed = 0
        l = 0

        res = [float("inf"), 0, 0]
        min_len = float("inf")

        window_count = {}
        for r in range(len(s)):
            char_r = s[r]
            window_count[char_r] = window_count.get(char_r, 0) + 1
            if char_r in t_count and window_count[char_r] == t_count[char_r]:
                formed += 1

            # 3. Contract the window (only when valid)
            while formed == required:
                curr_len = r - l + 1
                # A. Update the minimum window found so far
                if curr_len < min_len:
                    min_len = curr_len
                    res = [l, r]
                # B. Get the character leaving the window
                char_l = s[l]
                # C. Decrease the count for char_l in the window_count map
                window_count[char_l] -= 1
                # D. Check if removing char_l breaks the 'formed' condition
                #    If it does, decrement formed.
                if char_l in t_count and window_count[char_l] < t_count[char_l]:
                    formed -= 1
                # E. Shrink the window
                l += 1
        if min_len == float("inf"):
            return ""
        else:
            return s[res[0]:res[1] + 1]
