'''
문자열 안에 ' 있을 때는 전체 문자열을 " "
or 문자열 안에 \' 하고 전체 문자열을 ''
문자열 안에 " 있을 때는 전체 문자열을 ' ' 
or 문자열 안에 \" 하고 전체 문자열을 " "
'''

food1 = "Python's favorite food is perl"
print(food1)

food2 = 'Python\'s favorite food is perl'
print(food2)

print(food1 == food2)

"""
문자열 여러줄이면 
줄 바꾸고 싶은 부분에 \n
or ''' or """


multiline1 = 'Life is too short,\nyou need python'
print(multiline1)

multiline2 = '''
Life is too short,
you need python'''
print(multiline2)
