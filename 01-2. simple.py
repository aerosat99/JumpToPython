languages = ['python', 'perl', 'c', 'java']

for lang in languages :
    if lang in ['python', 'perl' ] :
        print("%6s need interpreter" % lang) 
    elif lang in ['c', 'java'] :
        print("%6s need complier" % lang)
    else :
        print("should not reach here")
'''
주석이 여러줄일때
name = ""
tel = ""
'''

# %6s = 문자열 포맷팅, 6칸 남겨놓고 %에서 지정한 문자열 lang 표시
