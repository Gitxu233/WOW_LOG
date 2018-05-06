import sys
import os
import string
f1 = open("WoWChatLogANSI.txt",'r',encoding = 'ANSI')
f2 = open("result.txt",'w',encoding = 'ANSI')
str1="悄悄地说"
str2="Hchannel"
str3="频道"
str4="大脚任务进度"
str5="大脚组队"
str6="**"
str7="无食物效果"
str8="无合剂效果"
str9="(任务完成)"
str10="-"
n=0
mon=""
dat=""
for line in f1.readlines():
	mon=""
	dat=""
	if((line.find(str1)!=-1 or line.find(str2)!=-1) and (line.find(str3)==-1) and (line.find(str4)==-1)and (line.find(str5)==-1)and (line.find(str6)==-1)):
		if((line.find(str7)==-1)and (line.find(str8)==-1)and (line.find(str9)==-1)):
			line=line.replace("|Hchannel:RAID|h[团队]|h","[团队]")
			line=line.replace("|Hchannel:GUILD|h[公会]|h","[公会]")
			line=line.replace("|Hchannel:PARTY|h[小队]|h","[小队]")
			line=line.replace("|Hchannel:INSTANCE_CHAT|h[副本]|h","[副本]")
			line=line.replace("|Hchannel:RAID|h[团队领袖]|h","[团队领袖]")
			line=line.replace("|Hchannel:PARTY|h[队长]|h","[队长]")
			line=line.replace("|Hchannel:INSTANCE_CHAT|h[副本向导]|h","[副本向导]")
			for c in line[0:2]:
				if(c!='/'):
					mon=mon+c	#xx/xx 1/1 1/11 11/1 11/11 
			for c in line[2:5]:
				if(c!='/' and c!=' '):
					dat=dat+c
				if(c==' '):
					break
				
				f2=open("result"+'/'+mon+'_'+dat+".txt",'a',encoding='ANSI')
			if((line.count(str10))>=2):
				n=n+1
			else:
				f2.write(line)
				
f2.close()
f1.close()



