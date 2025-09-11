# 리스트변수 인덱싱
# 여러개의 값 저장, 값을 변경, []
# append() insert() remove() pop() sort() reverse() clear()
# 인덱싱 포함[::] in 미포함 not in

# food = ["햄버거", "탕수육", "피자", "간장게장", "만두", "초밥"]
# print(food)
# food.append("김치찜")
# print(food)
# food.insert(3,"계란찜")
# print(food)
# food.remove("피자")
# print(food)
# food.pop(5)
# print(food)
# food.sort()
# print(food)
# food.reverse()
# print(food)
# food.clear()
# print(food)

# 문자열변수 인덱싱
name_list = ["강준상", "김현진", "배규찬", "이민우", "이종윤", "이현서"]
print(name_list)
print(name_list[4])
name_list[2] = "정유환"
print(name_list)
print(name_list[0:4])
print(name_list[1:4])
print(name_list[4:6])
print(name_list[::2])
print(name_list[3:])
print(name_list[:3])
print(name_list[:-2])
print(len(name_list))

print("이종윤" in name_list)
print("황지후" not in name_list)
print("이현서" not in name_list)
print("최병모" in name_list)

i = [5, 4, 6, 3, 7]
print(9 in i)
print(3 not in i)