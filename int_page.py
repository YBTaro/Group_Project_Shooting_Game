import random
from func import *
# 初始化面設計


WIDTH = 500
HEIGHT = 800
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CADMIUM_YELLOW = (253, 218, 13)
RED = (255, 0, 0)
GREEN = (0, 238, 118)
LIGHTGOLDEN = (255, 236, 139)


def draw_init(clock, win, background_img):

    while True:
        clock.tick(FPS)
        win.fill(BLACK)
        win.blit(background_img, (0, 0))
        draw_text(win, "這啥鬼遊戲?", 50, WIDTH/2, 150, CADMIUM_YELLOW)
        draw_text(win, "E->看玩法", 30, 110, 290, WHITE, "default")
        draw_text(win, "Q->看開發人員資訊", 30, 110, 390, WHITE, "default")
        draw_text(win, "ENTER->開始遊戲", 30, 110, 490, WHITE, "default")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.get_pressed()
                if key_pressed[pygame.K_RETURN]:
                    return True
                if key_pressed[pygame.K_e]:
                    if draw_rule(clock, win, background_img) == False:
                        return False
                if key_pressed[pygame.K_q]:
                    if draw_developer(clock, win, background_img) == False:
                        return False
        pygame.display.update()

# 顯示遊戲規則


def draw_rule(clock, win, background_img):
    while True:
        clock.tick(FPS)
        win.fill(BLACK)
        win.blit(background_img, (0, 0))
        draw_text(win, "你在宇宙中迷路了，可憐兮兮的樣子", 20, 30, 100, WHITE, "default")
        draw_text(win, "你很害怕", 20, 30, 130, WHITE, "default")
        draw_text(win, "害怕的是即使完成挑戰後，還是要繼續當社畜", 20, 30, 160, WHITE, "default")
        draw_text(win, "每天工作賺錢，養家活口", 20, 30, 190, WHITE, "default")
        draw_text(win, "買什麼股票什麼股票就跌停", 20, 30, 220, WHITE, "default")
        draw_text(win, "剛賣掉就漲停", 20, 30, 250, WHITE, "default")
        draw_text(win, "還沒有人愛你", 20, 30, 280, WHITE, "default")
        draw_text(win, "WASD：上下左右移動", 30, 100, 410, CADMIUM_YELLOW, "default")
        draw_text(win, "Z：使用防護罩", 30, 100, 460, CADMIUM_YELLOW, "default")
        draw_text(win, "空白鍵(Space)：射擊", 30, 100,
                  510, CADMIUM_YELLOW, "default")
        draw_text(win, "ESC->回上一頁", 25, WIDTH-100, 750, RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.get_pressed()
                if key_pressed[pygame.K_ESCAPE]:
                    return True

        pygame.display.update()

# 顯示開發人員


def draw_developer(clock, win, background_img):
    text_array = [
    "主程式架構與整合：昱博",   
    "圖片素材：皓翔、芳羽、宏霖、昱博、瓊慧", 
    "音效：芳羽、昱博", 
    "掉寶設計：昱博",
    "介面設計：昱博",
    "玩家設計：昱博",
    "爆炸動畫：昱博",
    "敵方單位-狂暴戰機海：皓翔",
    "敵方單位-基本戰機與子彈：昱博",
    "敵方單位-幽浮與追蹤彈：昱博",
    "敵方單位-衛星與雷射：昱博",
    "敵方單位-仙人掌與爆刺彈：昱博",
    "敵方單位-黑洞：昱博",
    "敵方單位-破壞災厄藍寶石與反射彈：宏霖",
    "敵方單位-鯉魚王與鮭魚卵：芳羽",
    "敵方單位-漂浮皮卡丘：芳羽",
    "敵方單位-肌肉殘暴皮卡丘：芳羽"
    ]
    while True:
        clock.tick(FPS)
        win.fill(BLACK)
        win.blit(background_img, (0, 0))
        draw_text(win, "開發人員名單", 35, WIDTH/2, 50, CADMIUM_YELLOW)
        for i in range(len(text_array)):
            draw_text(win, text_array[i], 25, 23, 90+32*i, WHITE, "default")

        draw_text(win, "感謝這段時間大家的付出！辛苦啦！", 25, WIDTH/2, 700, LIGHTGOLDEN)
        draw_text(win, "ESC->回上一頁", 25, WIDTH-100, 750, RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.get_pressed()
                if key_pressed[pygame.K_ESCAPE]:
                    return True

        pygame.display.update()


def draw_if_hidden_boss(clock, win, background_img):
    while True:
        clock.tick(FPS)
        win.fill(BLACK)
        win.blit(background_img, (0, 0))
        draw_text(win, "恭喜破關！", 60, WIDTH/2, 150, CADMIUM_YELLOW)
        draw_text(win, "是否挑戰隱藏關？", 35, WIDTH/2, 300, CADMIUM_YELLOW)
        draw_text(win, "Enter->挑戰", 30, WIDTH/2, 400, GREEN)
        draw_text(win, "Esc->放棄並回初始頁面", 30, WIDTH/2, 450, RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.get_pressed()
                if key_pressed[pygame.K_ESCAPE]:
                    return "NO"
                if key_pressed[pygame.K_RETURN]:
                    return "YES"
        pygame.display.update()


def draw_win(clock, win, background_img, win_img):
    while True:
        clock.tick(FPS)
        win.fill(BLACK)
        win.blit(background_img, (0, 0))
        win.blit(win_img, (100, 280))
        draw_text(win, "恭喜你完成隱藏的關卡！", 40, WIDTH/2, 170, CADMIUM_YELLOW)
        draw_text(win, "PIKA!PIKA!", 40, WIDTH/2, 250, CADMIUM_YELLOW)
        draw_text(win, "Enter->回到初始畫面", 25, WIDTH-150, 750, RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.get_pressed()
                if key_pressed[pygame.K_RETURN]:
                    return True
        pygame.display.update()


def draw_lose(clock, win, background_img, lose_img_array):
    index = random.randint(0, 2)
    while True:
        clock.tick(FPS)
        win.fill(BLACK)
        win.blit(background_img, (0, 0))
        win.blit(lose_img_array[index], (100, 280))
        draw_text(win, "輸爛了QQ", 40, WIDTH/2, 160, CADMIUM_YELLOW)
        draw_text(win, "請再接再厲！精神上支持你<3", 30, WIDTH/2, 230, CADMIUM_YELLOW)
        draw_text(win, "Enter->回到初始畫面", 25, WIDTH-150, 750, RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.get_pressed()
                if key_pressed[pygame.K_RETURN]:
                    return True
        pygame.display.update()
