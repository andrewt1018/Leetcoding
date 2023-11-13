# https://leetcode.com/problems/seat-reservation-manager/description/?envType=daily-question&envId=2023-11-06
class SeatManager:

    def __init__(self, n: int):
        self.num = n
        self.top = 1
        self.holes = []

    def reserve(self) -> int:
        if self.holes != []:
            ret = self.holes[0]
            self.holes = self.holes[1:]
            return ret
        else:
            ret = self.top
            self.top += 1
            return ret

    def unreserve(self, seatNumber: int) -> None:
        self.holes.append(seatNumber)
        self.holes.sort()
        
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)