def findRestaurant(list1: list[str], list2: list[str]) -> list[str]:
    index_sum = 0
    fav_restaurant = []
    first = True
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                if i + j == index_sum:
                    fav_restaurant.append(list1[i])
                    first = False
                elif i + j < index_sum or first:
                    fav_restaurant.clear()
                    fav_restaurant.append(list1[i])
                    index_sum = i + j
                    first = False
    return fav_restaurant
