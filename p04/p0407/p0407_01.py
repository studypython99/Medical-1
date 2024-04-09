import pygame
import random

# 1. pygame 초기화
pygame.init()

# 2. 게임창 설정
size = [400, 900]  # 게임 화면 크기 설정
screen = pygame.display.set_mode(size)  # 화면 생성

title = "My game"
pygame.display.set_caption(title)  # 게임 창 타이틀 설정

# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()  # 게임 시간 관리를 위한 Clock 객체 생성

class obj:
    def __init__(self):
        self.x = 0  # 객체의 x 좌표
        self.y = 0  # 객체의 y 좌표
        
    def put_img(self, address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()  # PNG 이미지를 불러와서 알파 채널을 포함하여 이미지 로드
        else:
            self.img = pygame.image.load(address)  # PNG가 아닌 경우 일반적으로 이미지 로드
        self.sx, self.sy = self.img.get_size()  # 이미지 크기 저장
        
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))  # 이미지 크기 조정
        self.sx, self.sy = self.img.get_size()  # 이미지 크기 갱신
        
    def show(self):
        screen.blit(self.img, (self.x, self.y))  # 화면에 이미지 그리기
        
# 우주선 객체 생성 및 설정
ss = obj()        
ss.put_img("ss.png")  # 우주선 이미지 불러오기
ss.change_size(50, 80)  # 이미지 크기 조정
ss.x = round(size[0] / 2 - ss.sx / 2)  # 화면 가로 중앙에 우주선 위치
ss.y = size[1] - ss.sy - 15  # 화면 하단에 우주선 위치
ss.move = 5  # 우주선 이동 속도

# 키보드 입력 관련 변수 초기화
left_go = False
right_go = False
space_go = False

# 미사일과 적 우주선 목록 초기화
m_list = []  # 미사일 목록
a_list = []  # 적 우주선 목록

# 색상 정의
black = (0, 0, 0)

# 게임 루프
running = True
while running:
    # 4-1. FPS 설정
    clock.tick(60)  # 초당 60프레임으로 설정
    
    # 4-2. 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # 종료 버튼을 누르면 게임 루프 종료
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_go = True  # 왼쪽 화살표 키 누름
            elif event.key == pygame.K_RIGHT:
                right_go = True  # 오른쪽 화살표 키 누름
            elif event.key == pygame.K_SPACE:
                space_go = True  # 스페이스바 키 누름
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_go = False  # 왼쪽 화살표 키 뗌
            elif event.key == pygame.K_RIGHT:
                right_go = False  # 오른쪽 화살표 키 뗌
            elif event.key == pygame.K_SPACE:
                space_go = False  # 스페이스바 키 뗌
    
    # 4-3. 입력 및 게임 로직 처리
    if left_go:
        ss.x -= ss.move  # 왼쪽 이동
        if ss.x <= 0:
            ss.x = 0
    elif right_go:
        ss.x += ss.move  # 오른쪽 이동
        if ss.x >= size[0] - ss.sx:
            ss.x = size[0] - ss.sx
    
    # 미사일 발사 로직
    if space_go:
        mm = obj()
        mm.put_img("yellow.png")  # 미사일 이미지 불러오기
        mm.change_size(5, 15)  # 미사일 크기 조정
        mm.x = round(ss.x + ss.sx / 2 - mm.sx / 2)  # 우주선 중앙에서 발사
        mm.y = ss.y - mm.sy - 10
        mm.move = 15  # 미사일 이동 속도
        m_list.append(mm)
    
    # 미사일 이동 처리
    d_list = []
    for i in range(len(m_list)):
        m = m_list[i]
        m.y -= m.move
        if m.y <= -m.sy:
            d_list.append(i)
    d_list.reverse()
    for d in d_list:
        del m_list[d]
        
    # 적 우주선 생성
    if random.random() > 0.98:
        aa = obj()
        aa.put_img("aa.png")  # 적 우주선 이미지 불러오기
        aa.change_size(40, 40)  # 적 우주선 크기 조정
        aa.x = random.randrange(0, size[0] - aa.sx - round(ss.sx / 2))  # 화면 내 임의 위치에서 생성
        aa.y = 10  # 화면 상단에서 생성
        aa.move = 1  # 적 우주선 이동 속도
        a_list.append(aa)
    
    # 적 우주선 이동 처리
    d_list = []
    for i in range(len(a_list)):
        a = a_list[i]
        a.y += a.move
        if a.y >= size[1]:
            d_list.append(i)
    d_list.reverse()
    for d in d_list:
        del a_list[d]
        
    # 4-4. 화면 그리기
   
