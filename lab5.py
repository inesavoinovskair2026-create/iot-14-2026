def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"[my_decorator] Викликано метод: {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper


class Furniture:
    def __init__(self, name="Річ", coords=None):
        self.__name = name
        self.__coords = list(coords) if coords else [0, 0]

    def get_name(self):
        return self.__name

    def get_coords(self):
        return self.__coords

    def set_coords(self, coords):
        self.__coords = list(coords)

    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, value):
        self.__coords = list(value)

    def __str__(self):
        return f"{self.__name} {self.__coords}"

    def __repr__(self):
        return f"Furniture({self.__name!r}, {self.__coords!r})"

    def __del__(self):
        print(f"[деструктор] '{self.__name}' видалено")


class Bed(Furniture):
    def __init__(self, name="Ліжко", coords=None, size="двоспальне"):
        super().__init__(name, coords)
        self.size = size

    def __str__(self):
        return f"{super().__str__()}, розмір: {self.size}"


class Table(Furniture):
    def __init__(self, name="Стіл", coords=None, seats=4):
        super().__init__(name, coords)
        self.seats = seats

    def __str__(self):
        return f"{super().__str__()}, місць: {self.seats}"


class Room:
    def __init__(self, name="Кімната мрії"):
        self.__name = name
        self.__items = []

    @my_decorator
    def add_item(self, item):
        self.__items.append(item)

    @my_decorator
    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)

    @my_decorator
    def Rearrangement(self, dx=0, dy=0):
        for item in self.__items:
            x, y = item.coords
            item.coords = [x + dx, y + dy]

    def __str__(self):
        return f"Кімната '{self.__name}':\n" + "\n".join("  " + str(i) for i in self.__items)

    def __del__(self):
        print(f"[деструктор] кімнату '{self.__name}' видалено")


def main():
    room = Room()
    bed, table = Bed(coords=[1, 1]), Table("Стіл", [4, 2], 6)
    room.add_item(bed)
    room.add_item(table)

    print(room)
    room.Rearrangement(2, -1)
    print("\nПісля Rearrangement(2, -1):\n" + str(room))

    room.remove_item(table)
    del table
    print("\nПісля видалення столу:\n" + str(room))


if __name__ == "__main__":
    main()