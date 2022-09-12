def Insert_Element(list2):
    num = int(input("Enter the number,you can insert in array:"))
    position = int(input("Enter the position where you can insert the number: "))
    print(f"Before insert:{list2}")
    list2.insert(position - 1, num)
    return list2


def Delete_Element(list2):
    number = int(input("Enter the number,you can delete in array:"))
    print(f"Before delete:{list2}")
    list2.remove(number)
    return list2


list1 = [int(x) for x in input("Enter the elements for list:").split()]
while 1:
    t = int(input("Enter 1 for insert or 2 for delete:"))
    if t == 1:
        list3 = Insert_Element(list1)
        print(f"After insert:{list3}")
    else:
        list3 = Delete_Element(list1)
        print(f"After delete:{list3}")
