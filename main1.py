def block(num):
    for i in range(0,len(blocks)):
        first=blocks[i][0]
        if(first[0]==str(num)):
            return i
    
r=open('input.txt', 'r')
rule=r.read()
rule=rule.split("\n")
print()
for i in range(0,len(rule)):
    rule[i]=rule[i].split()
leader=[0]

for i in range(1,len(rule)-1):
    if("goto" in rule[i]):
        index=rule[i].index("goto")
        ruleNumber=int(rule[i][index+1])
        leader+=[ruleNumber-1]
        if("if" in rule[i]):
            leader+=[i+1]
leader.sort()

print("Leader Rules :\n")
for i in leader:
    print(*rule[i])
blocks=[[]for i in range(0,len(leader))]
leader.append(len(rule))

print("\nBlocks :")
for i in range(1,len(leader)):
    print("\nBlock",i,)
    for j in range(leader[i-1],leader[i]):
        blocks[i-1].append(rule[j])
        print(*rule[j])

dic={}
for i in range(0,len(blocks)):
    dic[i]=[]
for i in range(0,len(blocks)-1):
    last=blocks[i][-1]
    if("goto" not in last):
        dic[i].append(i+1)
    else:
        if("if" in last):
            index=last.index("goto")
            val2=block(int(last[index+1]))
            dic[i]+=[i+1,val2]
        else:
            index = last.index("goto")
            value = block(int(last[index+1]))
            dic[i]+=[value]

print("\nControl Flow Graph")
for i in dic:
    print("B"+str(i+1)+":",end=" ")
    for j in dic[i]:
        print("B"+str(j+1),end=" ")
    print("\t")
