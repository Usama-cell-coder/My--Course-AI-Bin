customer_name='Tim kate'
age=12
height=6.12
print("name of customer is ",customer_name)
print("my age is",age)
print("height is",height)
print(type(customer_name))
print(type(age))
print(type(height))
customer_value=age+height
print(customer_value)
age+=5
customer_company='abc_inc'
print(age)
customer_info='Tim kate is a prime customer. he lives in california'
print(customer_info)
print(type(customer_info))
print(len(customer_info))
for char in customer_info:
    print(char)
print(customer_info[2:])
customer_list=["tim kate",54,6.12,2,"abc_inc"]
print(customer_list)
print(type(customer_list))
print(customer_list[2])
customer_list.append(30000)
print(customer_list)
customer_list.insert(1, "lahore")
print(customer_list)
customer_list.remove(54)
customer_list.pop(0)
print(customer_list)
print(len(customer_list))
for c in customer_list:
    print(c)
customer_list[0]="RYK"
print(customer_list)
Customer_tuple1=("tim kate",12,6.12,"abc_inc")
print(len(Customer_tuple1))
print(type(Customer_tuple1))
for c in Customer_tuple1:
    print(c)
print(Customer_tuple1[0])
print(type(Customer_tuple1[0]))


customer_set={"time kate",12,6.12,"abc_inc"}
print(customer_set)
print(type(customer_set))
print(len(customer_set))
for c in customer_set:
    print(c)
customer_set.add("lahore city")
print(customer_set)
customer_set.discard("abc_inc")
print(customer_set)
customer_dict={"name":"tim kate","age":12,"height":6.12}
print(customer_dict)
customer_dict["name"]="tom kate"
print(customer_dict)
print(len(customer_dict))
print(type(customer_dict))
for c in customer_dict:
    print(c)
customer_dict.update({"name":"usama"})
print(customer_dict)
