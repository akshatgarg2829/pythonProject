# obj = open("message2.txt", "w")
# retu = obj.write("Hello this is Akshat garg")
# obj.close()

ls = ["Hello\n", "hii"]
obj = open("message2.txt", "w")
obj.writelines(ls)
obj.close()