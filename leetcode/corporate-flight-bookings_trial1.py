class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flight = [0] * (n+1)

        for f,l, s in bookings:
            for i in range(f,l+1):
                flight[i]+=s
                
        return flight[1:]
        