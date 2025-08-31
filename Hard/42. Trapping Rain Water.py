class Solution:
    def trap(self, height: list[int]) -> int:
        start = 0
        pockets = []
        total_water = 0
        for curr_height in height:
            if curr_height >= start:
                for pocket in pockets:
                    curr_water = start - pocket
                    total_water += curr_water if curr_water > 0 else 0
                start = curr_height
                pockets = []
            else:
                pockets.append(curr_height)
        while len(pockets) > 0:
            last = max(pockets)
            last_index = pockets.index(last)
            for pocket in pockets[:last_index]:
                curr_water = last - pocket
                total_water += curr_water if curr_water > 0 else 0
            if last_index +1 >= len(pockets):
                break
            pockets = pockets[last_index+1:]
        return total_water