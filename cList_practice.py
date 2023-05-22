import ctypes


class CList:
    def __init__(self):
        self.capacity = 2
        self.array = (self.capacity * ctypes.c_int)()
        self.size = 0

    def add_element(self, el: int):
        if self.size == self.capacity:
            old_array = self.array
            self.capacity *= 2
            self.array = (self.capacity * ctypes.c_int)()
            for i in range(self.size):
                self.array[i] = old_array[i]
            self.array[self.size] = el
            self.size += 1
        else:
            self.array[self.size] = el
            self.size += 1

    def remove_last_element(self):
        self.array[self.size - 1] = 0
        self.size -= 1
        if self.size == self.capacity // 4:
            old_array = self.array
            self.array = (2 * self.size * ctypes.c_int)()
            for i in range(self.size):
                self.array[i] = old_array[i]
            self.capacity = self.capacity // 2

    def insert_el(self, index: int, el: int):
        if self.size == self.capacity:
            old_array = self.array
            self.array = (2 * self.capacity * ctypes.c_int)()
            for i in range(index):
                self.array[i] = old_array[i]
            self.array[index] = el
            self.size += 1
            for i in range(index + 1, self.size):
                self.array[i] = old_array[i]
        else:
            old_array = self.array
            self.array[index] = el
            for i in range(index + 1, self.size + 1):
                self.array[i] = old_array[i]


# class CList:
#     def __init__(self):
#         self.capacity = 2
#         self.array = (self.capacity * ctypes.c_int)()
#         self.size = 0
#
#     def add_element(self, el):
#         if self.size == self.capacity:
#             new_arr = (2 * self.capacity * ctypes.c_int)()
#             for i in range(self.capacity):
#                 new_arr[i] = self.array[i]
#             self.array = new_arr
#             self.array[self.size] = el
#             self.size += 1
#             self.capacity = 2 * self.capacity
#
#         else:
#             self.array[self.size] = el
#             self.size += 1
#
#     def remove_last_element(self):
#         self.array[self.size - 1] = 0
#         self.size -= 1
#         if self.size == self.capacity / 4:
#             new_array = (self.size * 2 * ctypes.c_int)()
#             for i in range(self.size):
#                 new_array[i] = self.array[i]
#             self.array = new_array
#             self.capacity = int(self.capacity / 2)
#
#     def insert_el(self, el, index):
#         if self.size == self.capacity:
#             new_array = (2 * self.capacity * ctypes.c_int)()
#             for i in range(self.capacity):
#                 new_array[i] = self.array[i]
#             self.array = new_array
#             for i in range(self.size - 1, index - 1, -1):
#                 self.array[i] = self.array[i + 1]
#             self.array[index] = el
#             self.size += 1
#         else:
#             for i in range(self.size - 1, index - 1, -1):
#                 self.array[i + 1] = self.array[i]
#             self.array[index] = el
#             self.size += 1


def main():
    l = CList()
    l.add_element(4)
    l.add_element(5)
    l.add_element(6)
    l.add_element(7)
    l.insert_el(3, 1)
    print(l.array[0])
    print(l.array[1])
    print(l.array[2])
    print(l.array[3])
    print(l.size)
    print(l.capacity)


if __name__ == '__main__':
    main()
