
for i in range(2,21):
    f=open(f"tables/{i}.txt","w")
    for j in range(0,11):
        f.write(f"{i}*{j}={i*j}\n")
       

