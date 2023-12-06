from list import LinkedList
from node import Node
from pickle import dump, load, HIGHEST_PROTOCOL  
from sys import argv
from graph import Graph
def menu():
    menu = "(1) Load network\n(2) Set probabilities\n(3) Node operations" \
           "\n(4) Edge operations\n(5) New post\n(6) Display network" \
           "\n(7) Display statistics\n(8) Update\n(9) Save network\n(0) Exit\n>> "
    return input(menu)
def load_network(graph, network):
    network = open(network, "r")  
    for line in network:  
        line = line.rstrip().lstrip()  
        if ':' not in line:  
            graph.list.add_last(LinkedList(line))  
        else:  
            vertices = line.split(':')  
            vertices[0] = vertices[0].rstrip().lstrip()  
            vertices[1] = vertices[1].rstrip().lstrip()
            graph.connect(vertices[0], vertices[1])  
    network.close()  
def main():
    graph = Graph()  
    pro_like = 0  
    pro_follow = 0  
    time = 1  
    time_step = []  
    try:
        if not len(argv) >= 2:  
            print("Usage: SocialSim -s [network_file] [event_file] [prob_like] [prob_follow]")
            print("Usage: SocialSim -i")
            print("-i : interactive mode")
            print("-s : simulation mode")
            return
        if argv[1] == "-i":  
            while 1:  
                try:  
                    choice = int(menu())  
                    if choice is 1:  
                        user = int(input("(1) Load new network\n(2) Load saved network\n>> "))
                        if user is 1:  
                            network = input("\nEnter file name: ")
                            load_network(graph, network)
                        elif user is 2:  
                            f = input("\nEnter file name: ") + ".pkl"
                            f = open(f, "rb")  
                            graph = load(f)  
                            f.close()  
                        else:
                            print("Invalid choice. try again")
                    elif choice is 2:  
                        pro_like = float(input("\tEnter probablity of Like: "))
                        pro_follow = float(input("\tEnter probablity of Follow: "))
                    elif choice is 3:  
                        user = int(input("\t(1) Find \n\t(2) Insert\n\t(3) Remove\n\t>> "))
                        if user is 1:  
                            node = input("\tEnter node to find: ")
                            if graph.list.find_node(node) is not None:  
                                print("\t" + node + " found !")
                            else:
                                print("\t" + node + " not found")
                        elif user is 2:  
                            graph.list.add_last(LinkedList(input("\tEnter node to insert: ")))
                            print("\tNode added")
                        elif user is 3:  
                            node = input("\tEnter node to delete: ")
                            if graph.list.delete_node(
                                    node) is not None:  
                                graph.delete_node(node)
                                print("\t" + node + " deleted.")
                            else:
                                print("\t" + node + " can't be deleted.")
                        else:
                            print("Invalid choice. try again")
                    elif choice is 4:  
                        user = int(input("\t(1) Add \n\t(2) Remove\n\t>>  "))
                        if user is 2:  
                            node1 = input("\tEnter node1 : ")
                            node2 = input("\tEnter node2 : ")
                            if graph.delete_edge(node1, node2) is True:  
                                print("\tEdge Deleted")
                        elif user is 1:  
                            node1 = input("\tEnter node1 : ")
                            node2 = input("\tEnter node2 : ")
                            graph.connect(node1, node2)
                            print("\tEdge added")
                        else:
                            print("Invalid choice, try agian.")
                    elif choice is 5:  
                        node = input("\tEnter node: ")
                        node = graph.list.find_node(node)  
                        if node is not None:  
                            node.posts.append(input("\tEnter Post: "))  
                            time_step.append(node)  
                        else:
                            print("\tNode not found")
                    elif choice is 6:  
                        print(graph)  
                    elif choice is 7:  
                        likes = []  
                        person = graph.list.head
                        print("\t\t\tPeople in order of popularity.")
                        while person:
                            likes.append((person.likes, person.value, person.posts, person.fol, person.flrs))
                            person = person.next_node
                        likes.sort(key=lambda t: t[0], reverse=True)
                        for like in likes:
                            print("\t\tPeople: " + str(like[1].value) + " Total Likes: " + str(like[0]))
                        print("\t\t\tPosts in order of popularity.")
                        for like in likes:
                            post = like[2]
                            for p in post:
                                print("\t\tPost: " + str(p))
                        for like in likes:
                            print("\t\t" + str(like[1].value) + "'s record:\n\t\t\tPosts 
                            print("\t\t\tПодписчики 
                    elif choice is 8:  
                        print("\nTIME STEP 
                        if time_step:
                            if pro_like >= 0.5:
                                n = time_step[0].value.head
                                while n:
                                    node.likes += 1
                                    if pro_follow >= 0.5:
                                        n1 = graph.list.find_node(str(n.value))
                                        if n1 is not None:
                                            n1 = n1.value.head
                                            while n1:
                                                if node.value.find_node(str(n1.value)) is None:
                                                    graph.connect(str(node), str(n1.value))
                                                n1 = n1.next_node
                                    n = n.next_node
                                time_step = time_step[1:]
                        time += 1
                    elif choice is 9:  
                        f = input("\nEnter file name: ")
                        f = open(f + ".pkl", "wb")
                        dump(graph, f, HIGHEST_PROTOCOL)
                        f.close()
                    elif choice is 0:
                        break
                    else:
                        print("Invalid choice. try again")
                except Exception as ex:
                    print(ex)
                    print("Invalid input. try again")
        elif argv[1] == "-s":
            load_network(graph, argv[2])
            pro_follow = int(argv[5])
            pro_like = int(argv[4])
            event = open(argv[3], "r")
            for line in event:
                check = 0
                line = line.split(':')
                if line[0] == 'A':  
                    graph.list.add_last(LinkedList(line[1]))
                elif line[0] == 'F':  
                    graph.connect(line[1], line[2])
                elif line[0] == 'P':  
                    pass
                    
                    node = graph.list.find_node(line[1])
                    if node is not None:
                        node.posts.append(line[2])
                        time_step.append(node)
                        if time_step:
                            if pro_like >= 0.5:
                                n = time_step[0].value.head
                                while n:
                                    check += 1
                                    node.likes += 1
                                    if pro_follow >= 0.5:
                                        n1 = graph.list.find_node(str(n.value))
                                        if n1 is not None:
                                            n1 = n1.value.head
                                            while n1:
                                                if check > 100:
                                                    break
                                                check += 1
                                                if node.value.find_node(str(n1.value)) is None:
                                                    graph.connect(str(node), str(n1.value))
                                                n1 = n1.next_node
                                    n = n.next_node
                                time_step = time_step[1:]
                        time += 1
                elif line[0] == 'R':  
                    if graph.list.delete_node(line[1]) is not None:
                        graph.delete_node(line[1])
                elif line[0] == 'U':
                    graph.delete_edge(line[1], line[2])
                file = open("simulationM_Log.txt", "w")
                likes = []
                person = graph.list.head
                file.write("\t\t\tPeople in order of popularity.\n")
                while person:
                    likes.append((person.likes, person.value, person.posts, person.fol, person.flrs))
                    person = person.next_node
                likes.sort(key=lambda t: t[0], reverse=True)
                for like in likes:
                    file.write("\t\tPeople: " + str(like[1].value) + " Total Likes: " + str(like[0]) + "\n")
                file.write("\t\t\tPosts in order of popularity.\n")
                for like in likes:
                    post = like[2]
                    for p in post:
                        file.write("\t\tPost: " + str(p) + "\n")
                for like in likes:
                    file.write("\t\t" + str(like[1].value) + "'s record:\n\t\t\tPosts 
                    file.write("\t\t\tПодписчики 
                file.close()
            event.close()
    except Exception as ex:
        print(ex)
if __name__ == "__main__": main()
