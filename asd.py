
for i in range (2,21):
    table= ''
    for j in range(1,11):
        table += f"{i} X {j} = {i*j}\n"
    
    with open(f"tables/{i}.txt",'w') as f:
        f.write(table)