class Router:

    def __init__(self, memoryLimit: int):
        self.q = deque()
        self.limit=memoryLimit
        self.curStat=0
        self.seen = set()
        self.dest_map = defaultdict(SortedList)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination,timestamp) 
        if packet in self.seen:
            return False

        if self.curStat>=self.limit:
            old_packet = self.q.popleft()
            self.curStat-=1
            self.seen.remove(old_packet)
            self.dest_map[old_packet[1]].remove(old_packet[2])
        self.q.append(packet)
        self.seen.add(packet)
        self.dest_map[destination].add(timestamp)
        self.curStat+=1
        return True

    def forwardPacket(self) -> List[int]:
        if self.q and self.curStat>0:
            old_packet = self.q.popleft()
            self.curStat-=1
            self.seen.remove(old_packet)
            self.dest_map[old_packet[1]].remove(old_packet[2])
            return old_packet
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        # cnt=0
        # for s,d,t in self.q:
        #     if t>=startTime and t<=endTime  and d == destination:
        #         cnt+=1
        # return cnt
        time =self.dest_map[destination]
        l = time.bisect_left(startTime)
        r = time.bisect_right(endTime)
        return r-l
# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
