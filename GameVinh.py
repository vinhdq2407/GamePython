import pygame,sys,random

# hàm tạo sàn chạy liên tục liền mạch
def draw_floor():
    screen.blit(floor,(floor_x_pos,650))
    screen.blit(floor,(floor_x_pos+432,650))
    # vinh

# hàm tạo ống liên tục
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos-650))
    return bottom_pipe, top_pipe 

# hàm di chuyển ống
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5 
    return pipes
# hàm vẽ ống
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 768 : 
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)
pygame.init()
# set khung hình 
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
# trong luc
gravity = 0.25
bird_movement = 0

# chèn background
bg = pygame.image.load('C:/Users/Admin/OneDrive/Máy tính/FlappyBird_Project/imgV2/background-night.png').convert()
bg = pygame.transform.scale2x(bg)
# chèn sàn
floor = pygame.image.load('C:/Users/Admin/OneDrive/Máy tính/FlappyBird_Project/imgV2/floor.png').convert()
floor = pygame.transform.scale2x(floor)
# tạo chim
bird = pygame.image.load('C:/Users/Admin/OneDrive/Máy tính/FlappyBird_Project/imgV2/yellowbird-midflap.png').convert()
bird = pygame.transform.scale2x(bird)
# tạo khoảng chọn cho chim
bird_rect = bird.get_rect(center = (100,384))

# tao duong ong
pipe_surface = pygame.image.load('C:/Users/Admin/OneDrive/Máy tính/FlappyBird_Project/imgV2/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []

# tao timer (tao ong xuat hien ngau nhien)
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe,1200)
pipe_height = [200,300,400]

# tạo chuyển động background
floor_x_pos  = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if(event.type == pygame.KEYDOWN):
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement = -11
        if event.type == spawnpipe:
            pipe_list.extend(create_pipe())
    screen.blit(bg,(0,0))
    # chim
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird,bird_rect)
    # ống
    pipe_list = move_pipe(pipe_list)
    draw_pipe(pipe_list)
    # sàn
    floor_x_pos -= 1
    draw_floor()
# tạo sàn chạy liên tục liền mạch
    if floor_x_pos <= -432:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)