#Programmer: Elizabeth Nocon
#Purpose:
#The purpose of this program is to read a text file of international cities and populations.
#The program will place the information of each city into a binary search tree.
#The program will then traverse the binary search tree to print the cities in order
#of population from smallest to largest.

#City Class
class city:
    #Creates city and assigns value to name and population.
    def __init__(self, name, population):
        self.name = name
        self.population = population

#Create Tree Node Class
class node:
    def __init__(self, city):
        self.left = None
        self.right = None
        self.value = city

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.value.population < node.value.population:
            if root.right is None:
                    root.right = node
            else:
                #call function again, to place node (use recursion)
                insert(root.right, node)
        else:
            #root is greater than node's population
             if root.left is None:
                root.left = node
             else:
                 #use recursion to call the function again
                insert(root.left, node)

def inOrderTraversal(root):
    if root:
        #left side recursion
        inOrderTraversal(root.left)
        #print the city information
        print(root.value.name + "\t" + str(root.value.population))
        #right side recursion
        inOrderTraversal(root.right)

#Read information from text file using a loop.
#Create city objects and nodes.
cityTreeRoot = None
with open("/home/enocon/PycharmProjects/Python_Projects_Feb2019/City_Populations", "r") as file:
    for line in file:
        cityInfo = line.split(" ")
        cityName = cityInfo[0]
        pop = cityInfo[1]
        cityPop = int(pop)
        newCity = city(cityName, cityPop)
        newNode = node(newCity)
        if cityTreeRoot is None:
            cityTreeRoot = newNode
        else:
            insert(cityTreeRoot, newNode)

#Print Table Heading
print("International Cities Listed by Population")
print("-----------------------------------------")
print("Listed from Lowest to Highest")
print("-----------------------------------------")

#Print Tree in order.
inOrderTraversal(cityTreeRoot)


