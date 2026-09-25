def get_data_type(data):
    dataType = type(data)
    return (f"({data}, {dataType})")


print(get_data_type(10))
print(get_data_type("Hello"))
print(get_data_type(5.5))
print(get_data_type(True))
print(get_data_type((1, 2, 3)))
print(get_data_type([1, 2, 3]))
print(get_data_type({1, 2, 3}))
print(get_data_type({"name": "Kiran", "age": 40}))
