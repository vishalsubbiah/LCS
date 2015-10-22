import numpy
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   

text1=open('1.txt','r')
text1=text1.read().split(' ')

text2=open('2.txt','r')
text2=text2.read().split(' ')
Sol=numpy.zeros((len(text1)+1,len(text2)+1))
Key1 = []
Key2 = []
LC=[] 
for i in range(1,len(text1)+1):
    for j in range(1,len(text2)+1):
        if(text1[i-1]==text2[j-1]):
            Sol[i][j]=Sol[i-1][j-1]+1
            Key1.append(i-1)
            Key2.append(j-1)             
                           
        else:
            Sol[i][j]=max(Sol[i-1][j],Sol[i][j-1])     

text1Fin=list(text1)
text2Fin=list(text2)

for l in set(Key1):
    text1Fin[l]=color.RED +text1[l] +color.END

for k in set(Key2):     
    text2Fin[k]=color.RED +text2[k] +color.END      

Ans1=' '.join(text1Fin)
Ans2=' '.join(text2Fin)

print color.BOLD+ "Text1: "+color.END+" \n" 
print Ans1
print color.BOLD+ "-------------------------------------------------"+color.END
print color.BOLD+ "Text2: "+color.END+" \n" 
print Ans2

