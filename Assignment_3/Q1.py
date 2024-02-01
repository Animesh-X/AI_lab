import json


f1 = open("data.txt", 'w')
f1.write("""1, John, 25
2, Jane, 30
3, Bob, 22
4, Alice, 28""")
f1.close()

def remove(string):
    return string.replace(" ", "")

def read_data():
    list_of_dict=[]
    with open("data.txt") as f:
        while f:
            data = f.readline()
            if not data:
                break
            data = remove(data)
            data = data.split(",")
            dict1={}
            dict1["Id"] = data[0]
            dict1["Name"] = data[1]
            dict1["Age"] = data[2]
            list_of_dict.append(dict1)


    return list_of_dict 


def write_data(filename, data):
    with open(filename, 'w') as f:
        for content in data:
            json.dump(content, f)
            f.write("\n")


def update_age(filename, id, new_age):
    with open(filename) as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = remove(lines[i])
        data = lines[i].split(",")
        if data[0] == str(id):
            data[2] = str(new_age)
            data[2]+="\n"
            lines[i] = ",".join(data)
    

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)

            


list_of_dict = read_data()
print(list_of_dict)
write_data("test.txt", list_of_dict)
update_age("data.txt", 1, 50)