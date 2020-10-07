from sys import argv
class LA:


    def __init__(self,file_object):
        self.file_object=file_object #输入文件
        self.noOfLine=0 #读取到第几行
        self.Token = {
            'BEGIN': 'Begin',
            'END': 'End',
            'FOR': 'For',
            'IF': 'If',
            'THEN': 'Then',
            'ELSE': 'Else'
        }
        self.value=''
    def Scanner(self):
        #读取每行
        for line in self.file_object:
            line=line.strip("\n")  #去掉换行符
            self.noOfLine+=1   #行号加1
            lenOfLine=len(line)  #每行的长度
            i=0
            tmp_str=''
            #读取每行的每个字符
            while i<lenOfLine:
                self.value=''
                cur=line[i]
                #空格
                if cur.isspace():
                    i+=1
                    continue
                #加号
                elif cur == '+':
                    self.value='Plus'
                    print(self.value)
                #乘号
                elif cur == '*':
                    self.value = 'Star'
                    print(self.value)
                #逗号
                elif cur == ',':
                    self.value = 'Comma'
                    print(self.value)
                #左括号
                elif cur == '(':
                    self.value = 'LParenthesis'
                    print(self.value)
                #右括号
                elif cur == ')':
                    self.value = 'RParenthesis'
                    print(self.value)
                #冒号
                elif cur ==':' :
                    self.value='Colon'
                    i+=1
                    if(i<lenOfLine):
                        cur=line[i]
                        if cur == '=':
                            self.value= 'Assign'
                        else:
                            i-=1
                    print(self.value)

                #字母
                elif cur.isalpha():
                    tmp_str+=cur
                    i+=1
                    while(i<lenOfLine):
                        cur=line[i]
                        if cur.isalpha()or cur.isdigit():
                            tmp_str=tmp_str+cur
                            i+=1
                        else:break
                    i-=1
                    if(tmp_str in self.Token):
                        print(self.Token.get(tmp_str))
                    else:
                        print("Ident("+tmp_str+")")
                    tmp_str=''
                #数字
                elif cur.isdigit():
                    tmp_str += cur
                    i += 1
                    while (i < lenOfLine):
                        cur = line[i]
                        if  cur.isdigit():
                            tmp_str = tmp_str + cur
                            i += 1
                        else:
                            break
                    i -= 1 #回退
                    print ("Int("+str(int(tmp_str))+")")
                    tmp_str=''
                #其他字符
                else:
                    print('Unknown')
                    return 1
                i+=1


if __name__ == "__main__":
    input=open(argv[1])
    la=LA(input)
    la.Scanner()


