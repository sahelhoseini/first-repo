
# Online Python - IDE, Editor, Compiler, Interpreter
integer=int(input("inter your integer:"))
i=1;cunt=0;result=0
while i<=integer:
 result=integer%i
 if result==0:
  print(i)
  cunt+=1
 i+=1
if cunt==2:
    print("عدد اول")
else:
    print("عدد مرکب")