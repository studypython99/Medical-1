
id = 'admin'
pw = '1111'

uid = input('id를 입력해주세요 >>')
upw = input('pw를 입력해주세요 >>')

#   id 입력, pw 입력 > id or pw 일치하지 않습니다 > 로그인 되었습니다 > 다시 입력해주세요 
print(uid)
if id == uid:
    print(upw)
    if pw == upw:
        print('로그인 되었습니다.')
    else:
        print('비밀번호를 다시 입력해주세요.')
        print(upw)
else:
    print('id를 다시 입력하세요.')
    print(uid)