class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flight = [0] * (n+1)

        for f,l, s in bookings:
            flight[f - 1] += s
            if l<n:
                flight[l] -= s

        for i in range(1, n):
            flight[i] += flight[i - 1]
                
        return flight[:n]
        