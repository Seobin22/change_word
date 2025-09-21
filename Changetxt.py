
# def fileopen(data, target):
 
#     with open(data,'r',encoding='cp949') as file:
    
#         text = file.read()
        
#         if target in text   :
        
#             flag = True
            
#             splitdata = text.split()
            
#         else :
        
#             flag = False
            
#             splitdata = None
 
#     return flag, splitdata

# def count_word(data,TargetText):
 
#     count = 0
    
#     for i in data :
    
#         if TargetText in i :
        
#             count += 1
            
#     return  count
# def rep(data,key,new):
#     with open(data,'r',encoding='cp949') as file:
#         my=file.read()
#         N=my.replace(key,new)
#         return N
#         # print(f'my{my}')
#         # for i in my:
#         #     print(f'i: {i}')
#         #     if key in i:
#         #         i.replace(key,new)
#         # print('이후my:',my)  
# def remov(path,what):
#     f=open(path,'w')
#     f.write("")
#     f.write(what)
#     f.close()


text_file_path = 'C:\\Users\\Owner\\Documents\\CODE\\p1\\change_box.txt'

target_word = ['\\']
new_word = '\\\\'


#target_word는 리스트로 해서 안에 문자열 목록들을 저장. new word 로 모두 변환하는 def new1_chtxt..   입력은 : 1. 파일명=change_box.txt 를 기본 2. targetword를 기본? 3. newword는 필수입력
def new1_chtxt(target_word, new_word,content='',text_file_path='C:\\Users\\Owner\\Documents\\CODE\\p1\\py_change\\change_box.txt'):
    if content!='':
       with open (text_file_path,'w',encoding='UTF8') as f:
         f.write(content)
    new_text_content = ''
    new_path='C:\\Users\\Owner\\Documents\\CODE\p1\\py_change\\new_box.txt'
    with open(text_file_path,'r',encoding='UTF8') as f:
        lines = f.readlines() ## 기존 텍스트파일에 대한 내용을 모두 읽는다.
        for l in (lines):
            new_string=l
            for i in target_word:
                new_string = new_string.replace(i,new_word)
            if new_string:
                new_text_content += new_string 
            # else:
            #     new_text_content += '\n'
    with open (text_file_path,'r',encoding='UTF8') as f:
        print('\n__________before____________\n')
        print(f.read())
    with open(new_path,'w+',encoding='UTF8') as f:
        f.write(new_text_content)

        
    print("-------------------최종결과--------------------")
    with open(new_path,'r',encoding='UTF8') as f:
        print(f.read())
content=r"C:\Users\Owner\Desktop\graph_save"
new1_chtxt(target_word, new_word,content)