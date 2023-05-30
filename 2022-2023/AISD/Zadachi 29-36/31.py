    from typing import Dict, List

    class Exhibit:
        def __init__(self, name: str, rating: int):
            self.name = name
            self.rating = rating

    class Visitor:
        def __init__(self, first_name: str, last_name: str, date_visited: str):
            self.first_name = first_name
            self.last_name = last_name
            self.date_visited = date_visited
            self.exhibits: Dict[str, Exhibit] = {}

    class Node:
        def __init__(self, visitor: Visitor):
            self.visitor = visitor
            self.prev: Node = None
            self.next: Node = None

    class MuseumVisitors:
        def __init__(self):
            self.head: Node = None
            self.tail: Node = None

        def add_visitor(self, visitor: Visitor):
            node = Node(visitor)
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node

        def get_visitor_list(self) -> List[Dict]:
            visitor_list = []
            current_node = self.head
            while current_node is not None:
                visitor = {
                    "first_name": current_node.visitor.first_name,
                    "last_name": current_node.visitor.last_name,
                    "date_visited": current_node.visitor.date_visited,
                    "exhibits": current_node.visitor.exhibits
                }
                visitor_list.append(visitor)
                current_node = current_node.next
            return visitor_list

        def add_exhibit_rating(self, visitor: Visitor, exhibit_name: str, rating: int):
            if visitor in self.get_visitor_list():
                current_node = self.head
                while current_node is not None:
                    if current_node.visitor == visitor:
                        exhibit = Exhibit(exhibit_name, rating)
                        current_node.visitor.exhibits[exhibit_name] = exhibit
                        break
                    current_node = current_node.next
    museum = MuseumVisitors()

    visitor1 = Visitor("Mihail", "Gorshenev", "2023-05-01")
    visitor2 = Visitor("Till", "Lindemann", "2023-05-02")
    visitor3 = Visitor("Bob", "Dylan", "2023-05-03")

    museum.add_visitor(visitor1)
    museum.add_visitor(visitor2)
    museum.add_visitor(visitor3)

    visitor1.exhibits["Painting 1"] = Exhibit("Painting 1", 4)
    visitor1.exhibits["Sculpture 1"] = Exhibit("Sculpture 1", 5)
    visitor2.exhibits["Painting 1"] = Exhibit("Painting 1", 3)
    visitor2.exhibits["Sculpture 2"] = Exhibit("Sculpture 2", 4)
    visitor3.exhibits["Painting 2"] = Exhibit("Painting 2", 4)
    visitor3.exhibits["Sculpture 3"] = Exhibit("Sculpture 3", 3)

    visitor_list = museum.get_visitor_list()

    for visitor in visitor_list:
        print(f"{visitor['first_name']} {visitor['last_name']} visited on {visitor['date_visited']}")
        for exhibit_name, exhibit in visitor['exhibits'].items():
            print(f"\t{exhibit_name}: {exhibit.rating}")
