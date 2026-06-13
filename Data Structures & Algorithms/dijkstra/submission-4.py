class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # src = start vertex
        # save an end vertex from 0 to n
        # if n not processed
        # find shortest neighbour
        # once found, add n to processed

        distances = {}
        costs = {}
        for i in range(n): # add arbitrary costs
            costs[i] = 9999

        # update src neighbour costs
        # !!! error might have to do with this only running once ??
        self.srcNeighCosts(src, edges, costs)

        for i in range(n):
            processed = [] # get's reset on every iteration (so the next searches don't skip everything)
            if src == i:
                distances.update({i:0})
            else:
                distances.update({i:self.dSearch(edges, costs, processed, i)})

        return distances


    # applies the correct source's neighbours costs
    def srcNeighCosts(self, src, edges, costs):
        for i in edges:
            #print(str(i[0]) + "hello")
            if i[0] == src:
                costs[i[1]] = i[2]


    def checkUnreachable(self, costs, end):
        if costs[end] == 9999:
            return True


    # find cheapest to vertex
    def findCheapest(self, costs, processed):
        lowest = 99999
        vert = None
        for i in costs:
            if costs[i] < lowest and i not in processed:
                lowest = costs[i]
                vert = i

        return vert

    def dSearch(self, edges, costs, processed, end):
        searchDone = False
        while not searchDone:
            cheapest = self.findCheapest(costs, processed)
            if cheapest == None: # find cheapest returns none if all has been processed
                searchDone = True
            elif cheapest == end:
                if self.checkUnreachable(costs, end): # first check if unreachable
                    return -1
                else:
                    return costs[cheapest] # otherwise return the cost
            else:
                cheapestNum = costs[cheapest]
                # search and update neighbour costs
                for i in edges:
                    if i[0] == cheapest and costs[i[1]] > cheapestNum + i[2]:
                        costs[i[1]] = cheapestNum + i[2]
                processed.append(cheapest)