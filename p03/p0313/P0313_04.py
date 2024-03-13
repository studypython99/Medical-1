#   다른 파일에 있는 함수를 사용할 때

from math import *  # 사용방법 mahe,floor() 이름.함수명()
# import lotto      #   이름사용가능
from lotto import *

import math as m #  모듈명을 줄여서 사용가능, 별칭부여
import lotto as lo #  모듈명을 줄여서 사용가능, 별칭부여


l = [0]*45

# while True:    
#     lotto.screen()
num_generate(l)
import math
print(math.ceil(12.2))      #   13  ceil:   올림
print(math.floor(12.2))     #   12  floor:  버림
print(round(12.6))          #   13  round:  반올림
print(dir(m))