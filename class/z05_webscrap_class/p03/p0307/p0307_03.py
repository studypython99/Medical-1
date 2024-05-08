students = {"stNo":1,"stuName":"홍길동","tel":"010-0000-0000","gender":"male","id":"aaa","pw":1111}

#   nicName: 길동스
students["stNo"] = students["stNo"]+1
#   if students["studentsNo"] = students["studentsNo"]+1
#   없는걸 변경하려하면 keyerror 가 뜬다
if "studentNo" in students:
    print("key가 있습니다.")
    students["studentsNo"] = students["studentsNo"]+1
    print(students["studentsNo"])
else:
    print("key가 없습니다.")



