class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count_map = Counter(hand)
        hand.sort()

        for num in hand:
            if not count_map[num]:
                continue
            curr_size = 0
            curr_num = num
            while curr_size != groupSize:
                if count_map[curr_num]:
                    curr_size += 1
                    count_map[curr_num] -= 1
                    curr_num += 1
                else:
                    return False

        return True


