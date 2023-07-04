#İçindeki bigileri json yapısına çevirince string bir ifade olmasına rağmen işlem yapabiliyoruz.
#Dosyayı okumak istiyorsak load - loads değil.

# import json



# Kimlikler={
#     "Ad":"Burak",
#     "Soyad":"Sen",
#     "Yas":23
# }

# döndür=json.dumps(Kimlikler) #jsona çevirme işlemi

# with open("C:/Users/Dell User/Desktop/Json2.txt","w",encoding="utf_8") as Dosya: #Cevir isimli json yapısını dosyaya göndereceğiz. (dump)gönderme
#     json.dump(döndür,Dosya)

# Students={
#     students1:{"Name":"Merve","Surname":"Calisi","Age":25,"Grades":[10,20,30]},
#     students2:{"Name":"Berk","Surname":"Gorsel","Age":17,"Grades":[20,20,20]}

# }

import json

def update_json(new_data, filename="data.json"):
    # YOUR CODE HERE #
    with open(filename,"r+") as file:
        file_data=json.load(file)
    file_data["emp_details"].append(new_data)
    file.seek(0)
    json.dump(file_data,file,indent=4)

    # pass
    
    # with open("data.json", "w") as js:
    #     js.write(json.dumps(out, indent=4))

# TEST YOUR CODE #
new_student = {"Name":"Deniz",
               "Surname": "Gezer",
               "Age": 32,
               "Grades": [25,6,42]
              }
update_json(new_student)
# update_json(new_data="data.json", new_student=new_student) 



