"""
Developer: Harrison Hughes, Truman State University 2024

Receive input from result.php, run an A* informed search algorithm over the specified 
source and destination objects to find the optimal route between the two buildings, and
print a JSON encoded result of the path and the path length to allow PHP access.

Search algorithm adapted from https://llego.dev/posts/implementing-the-a-search-algorithm-python/
and https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/a-star-search-algorithm/
"""
import svgpathtools as pathTools
import math
import sys
import Nodes
import json

class Node:
    """
    To define the unit of which the overall graph will operate over. This node class
    is designed to hold all necessary informaiton for an A** search algorithm to 
    operate under
    """
    
    def __init__(self, path, position, pathLen, heuristicLen):
        """
        To create a node based on specified values for all required 
        information necessary for the A* search algorithm
        
        Args:
            path (String): SVG path description of current node
            position (Tuple): Tuple containing x and y coordinated of node
            pathLen (Float): Current length of the path traversed so far
            heuristicLen (Float): Euclidean distance from node to closest destination node
        """
        
        self.path = path
        self.position = position
        self.pathLen = pathLen
        self.heuristicLen = heuristicLen
        self.totalLen = pathLen + heuristicLen

    def __lt__(self, other):
        """
        Specify the less than function to allow for sorting of a list containing nodes. Less than
        is decided by total length of the Nodes path, summing traversed and estimated distance to finish
        
        Args:
            other (Node): Node with which to compare total path length with

        Returns:
            Boolean: True if current node has shorter length than parameter node, false else
        """
        
        return self.totalLen < other.totalLen

    def __eq__(self, other):
        """
        Specify the equal to function to allow for sorting of a list containing nodes. Equality
        is decided by position of the node
        
        Args:
            other (Node): Node with which to compare total path length with

        Returns:
            Boolean: True if current node has same position as parameter node, false else
        """
        
        return self.position == other.position

class AStarSearch:
    """
    A pathfinding algorithm to find the shortest graphical distance between two objects.
    The algorithm has been modified to search from several starting locations and end 
    locations depending on the number of entrances of the specified object, rather than 
    the traditional one start and one end node
    """
    
    def __init__(self, nodeSet):
        """
        Create an instance of the search algorithm given a dictionary of nodes that 
        each hold their corresponding edges

        Args:
            nodeSet (Dictionary()): A dictionary of nodes to hold all path intersections and doorways, 
            where the value of each is a list of edges from that specific node
        """
        
        self.nodes = nodeSet
        self.discovered = []
        self.visited = []

    def search(self, source, dest):
        """
        Search the stored node set for the optimal path between the two parameter objects. These
        objects should correspond in name with keys in the node set to serve as starting and 
        ending nodes

        Args:
            source (String): Name of the beginning object of the path
            dest (String): Name of the ending object of the path

        Returns:
            String: The path of the optimal route between the two objects, else return None
        """
        
        #Insert source object beginning nodes into list of discovered nodes
        for i in self.nodes[source]:
            
            #Calculate closest end node of destination object
            closestDest = float('inf')
            for j in self.nodes[dest]:
                closestDest = min(closestDest, self.calcEuclideanDist(i, j))

            #Create SVG path anchor to begin dynamic path construction of this node
            pathAnchor = 'M' + str(i[0]) + ',' + str(i[1]) + ' ' 
                
            #Create new node with preliminary parameters, and add to the list of discovered nodes
            node = Node(pathAnchor, i, 0, closestDest)
            self.discovered.append(node)
            
        #While the list of discovered nodes is not empty
        while self.discovered:
            
            #Sort list by total path length, and select the node with the shortest possible path
            self.discovered.sort()
            currentNode = self.discovered.pop(0)
            
            #Add selected node to list of visited nodes to prevent multiple visits to same node
            self.visited.append(currentNode)

            #Check if the current node is an end node for the destination object
            for i in self.nodes[dest]:
                if currentNode.position == i:
                    
                    #If reached, we have found the optimal path
                    return currentNode.path

            #Otherwise, explore all edges from current node
            for i in self.nodes[currentNode.position]:
                
                #Append new edge to current path
                path = currentNode.path + str(i) + ' '
                
                #Parse new edge to gather length and displacement data
                newEdge = pathTools.parse_path(i)
                
                #Calculate the new position of the neighbor node given the new edge displacement
                coordShift = newEdge.end
                xShift = coordShift.real 
                yShift = coordShift.imag
                newPosition = (round(currentNode.position[0] + xShift, 2), round(currentNode.position[1] + yShift, 2))
                
                #Calculate path length of node with new edge attached
                newPathLen = newEdge.length() + currentNode.pathLen

                #Calculate closest end node of destination object
                closestDest = float('inf')
                for j in self.nodes[dest]:
                    closestDest = min(closestDest, self.calcEuclideanDist(newPosition, j))

                #Create new node with data derived above
                newNode = Node(path, newPosition, newPathLen, closestDest)

                #If node has not been visited before
                if newNode not in self.visited:
                    
                    #If new node has not even been discovered, add it to the discovered list
                    if newNode not in self.discovered:
                        self.discovered.append(newNode)
                        
                    #Else, we must check if the current route to get to this new node was shorter than the previously saved route
                    else:
                        #Get index of the new node within the discovered list
                        repeatNodeIx = self.discovered.index(newNode)
                        
                        #If out current path to the new node is quicker than the old one, we must replace it within our discovered
                        #list with the current route. This ensures we store the optimal route to all nodes at all times
                        if self.discovered[repeatNodeIx].totalLen > newNode.totalLen:
                            self.discovered[repeatNodeIx] = newNode
                 
        #If the discovered nodes list runs empty, no path was able to be formed between the two locations       
        return None
            
    def calcEuclideanDist(self, source, dest):
        """
        Calculate euclidean, or straight line distance between two nodes

        Args:
            source (Tuple): Position on the SVG file of the source node
            dest (Tuple): Position on the SVG file of the destination node

        Returns:
            Float: Euclidean distance between the two nodes
        """
        
        dist = math.sqrt((abs(source[0] - dest[0]) ** 2 + abs(source[1] - dest[1]) ** 2))
        return dist


if __name__ == '__main__':  
    """
    Run the search algorithm with parameters received from the result.php file.
    JSON encode both the optimal path, and the calcualted path distance, and
    print them for capture by the php file.
    """      
    
    NO_CLASSROOM = '-1';
    
    nodeSet = Nodes.nodes
    source = sys.argv[1]
    dest = sys.argv[2]
    
    #If the file specifies a source classroom, update the source variable
    if sys.argv[3] != NO_CLASSROOM:

        #Dynamically import the corresponding classroom node set, and update the generic node set with this data
        newBuilding = sys.argv[1] + 'Nodes'
        newBuilding = newBuilding.replace(" ", "")
        buildingNodes = __import__(newBuilding)
        nodeSet.update(buildingNodes.nodes)
        
        #Update source object
        source = sys.argv[3]
        
    #If the file specifies a destination classroom, update the destination variable
    if sys.argv[4] != NO_CLASSROOM:
        
        #Update the destination object
        dest = sys.argv[4]
        
        #If the destination building is not the same as the source building
        if sys.argv[1] != sys.argv[2]:
            
            #Dynamically import the corresponding classroom node set, and update the generic node set with this data
            newBuilding = sys.argv[2] + 'Nodes'
            newBuilding = newBuilding.replace(" ", "")
            buildingNodes = __import__(newBuilding)
            nodeSet.update(buildingNodes.nodes)

        
    new = AStarSearch(nodeSet)
    route = new.search(source, dest)
    dist = pathTools.parse_path(route).length()
    print(json.dumps((route, dist)))