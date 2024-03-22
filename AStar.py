import svgpathtools as pathTools
import math
import sys
import Nodes

class Node:
    def __init__(self, path, position, pathLen, heuristicLen):
        self.path = path
        self.position = position
        self.pathLen = pathLen
        self.heuristicLen = heuristicLen
        self.totalLen = pathLen + heuristicLen

    def __lt__(self, other):
        return self.totalLen > other.totalLen

    def __eq__(self, other):
        return self.position == other.position

class AStarSearch:
    def __init__(self):
        self.nodes = Nodes.nodes
        self.discovered = []
        self.visited = []

    def search(self, source, dest):
        #Insert beginning nodes into list of discovered nodes
        for i in self.nodes[source]:
            
            closestDest = float('inf')
            for j in self.nodes[dest]:
                closestDest = min(closestDest, self.calcEuclideanDist(i, j))

            pathAnchor = 'M' + str(i[0]) + ',' + str(i[1]) + ' ' 
                
            node = Node(pathAnchor, i, 0, closestDest)
            self.discovered.append(node)
            
        while self.discovered:
            self.discovered.sort()
            
            currentNode = self.discovered.pop()
            self.visited.append(currentNode)

            for i in self.nodes[dest]:
                if currentNode.position == i:
                    #print(pathTools.parse_path(currentNode.path).length())
                    return currentNode.path
            
            for i in self.nodes[currentNode.position]:
                path = currentNode.path + str(i) + ' '
                
                coordShift = pathTools.parse_path(i).end
                xShift = coordShift.real
                yShift = coordShift.imag
                newPosition = (round(currentNode.position[0] + xShift, 2), round(currentNode.position[1] + yShift, 2))
                
                newPathLen = pathTools.parse_path(i).length() + currentNode.pathLen

                closestDest = float('inf')
                for j in self.nodes[dest]:
                    closestDest = min(closestDest, self.calcEuclideanDist(newPosition, j))

                newNode = Node(path, newPosition, newPathLen, closestDest)

                if newNode not in self.visited:
                    if newNode not in self.discovered:
                        self.discovered.append(newNode)
                    else:
                        repeatNodeIx = self.discovered.index(newNode)
                        if self.discovered[repeatNodeIx].totalLen > newNode.totalLen:
                            self.discovered[repeatNodeIx] = newNode
                        
        return None
            

    def calcEuclideanDist(self, source, dest):
        dist = math.sqrt((abs(source[0] - dest[0]) ** 2 + abs(source[1] - dest[1]) ** 2))
        return dist


if __name__ == '__main__':        
    new = AStarSearch()
    print(new.search(sys.argv[1], sys.argv[2]))

#key = '428,487'
#best = dpShortest(nodes, 'M' + key +'l0,0', [], "Mcclain")
#print(best)

#for key in nodes:
#   for i in nodes[key]:
#        path = draw.Path(d='M0,0' + i, stroke='navy', stroke_width=2, fill='none', transform='translate(' + key + ')')
#        d.append(path)

#for key in nodes:
#    d.append(draw.Circle(0, 0, 2, fill='red', stroke='none', transform='translate(' + key + ')'))
#path = draw.Path(d=best, stroke='navy', stroke_width=2, fill='none', transform='translate(' + key + ')')



#search algorithm adapted from https://llego.dev/posts/implementing-the-a-search-algorithm-python/
#and https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/a-star-search-algorithm/
