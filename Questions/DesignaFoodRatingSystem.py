class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = foods
        self.cuisines = {}
        self.rating = {}
        self.heap = defaultdict(list)
        for f,c,r in zip(foods,cuisines,ratings):
            self.cuisines[f] = c
            self.rating[f] = r
            heapq.heappush(self.heap[c],(-r,f))

    def changeRating(self, food: str, newRating: int) -> None:
        self.rating[food] = newRating
        c = self.cuisines[food]
        heapq.heappush(self.heap[c],(-newRating,food))
        
    def highestRated(self, cuisine: str) -> str:
        heap = self.heap[cuisine]
        while heap:
            r,f = heap[0]
            if -r == self.rating[f]:
                return f
            heapq.heappop(heap)

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
