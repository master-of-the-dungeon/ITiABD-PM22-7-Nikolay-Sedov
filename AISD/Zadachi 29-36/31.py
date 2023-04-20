class VisitorNode:
    def __init__(self, name, surname, date, exhibits, ratings):
        self.name = name
        self.surname = surname
        self.date = date
        self.exhibits = exhibits
        self.ratings = ratings
        self.prev = None
        self.next = None


class MuseumVisitorList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add_visitor(self, name, surname, date, exhibits, ratings):
        new_node = VisitorNode(name, surname, date, exhibits, ratings)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def get_visitor_info(self, visitor_node):
        return {
            'name': visitor_node.name,
            'surname': visitor_node.surname,
            'date': visitor_node.date,
            'exhibits': visitor_node.exhibits,
            'ratings': visitor_node.ratings
        }

    def get_visitors_by_date(self, date):
        visitors = []
        current_node = self.head
        while current_node is not None:
            if current_node.date == date:
                visitors.append(self.get_visitor_info(current_node))
            current_node = current_node.next
        return visitors

    def get_average_rating(self, exhibit_name):
        total_rating = 0
        num_visitors = 0
        current_node = self.head
        while current_node is not None:
            if exhibit_name in current_node.exhibits:
                exhibit_index = current_node.exhibits.index(exhibit_name)
                total_rating += current_node.ratings[exhibit_index]
                num_visitors += 1
            current_node = current_node.next
        if num_visitors > 0:
            return total_rating / num_visitors
        else:
            return None

visitor_list = MuseumVisitorList()
visitor_list.add_visitor('John', 'Doe', '2023-04-15', ['paintings', 'sculptures'], [4, 5])
visitor_list.add_visitor('Jane', 'Doe', '2023-04-14', ['paintings', 'photography'], [3, 4])
visitor_list.add_visitor('Bob', 'Smith', '2023-04-14', ['sculptures', 'photography'], [5, 4])

print(visitor_list.get_visitors_by_date('2023-04-14'))
print(visitor_list.get_average_rating('paintings'))
