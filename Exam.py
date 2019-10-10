r = str(input())
r = (r + "|")
t = open("/home/student/Desktop/1.log", "r")
k = open("/home/student/Desktop/error.log", "w")
l = open("/home/student/Desktop/l.txt", "w")
for text in t:
    if(text.find("ERROR") != -1):
        print(text)
        k.write(text)
    if(text.find(r) != -1):
       print(text)
       l.write(text)
t.close
