# 改良１慣性の法則の適応
import pygame

# 初期化
pygame.init()

# 画面設定
width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("四角を操作")

# 四角の初期設定
rect_color = (93, 192, 0)         # 赤色
rect_x, rect_y = 50, 50          # 初期位置
rect_width, rect_height = 15, 15
speed = 0.3                      # 移動速度

# フレームレート管理用
clock = pygame.time.Clock()

# 色々な変数
friction = {"x": 0.08, "y": 0.08} # 摩擦係数
acceleration = {"x": 0, "y": 0} # 加速度
maxspeed = 9                   # 最大速度

running = True
while running:
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # キーの状態を取得
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and acceleration["x"] > -maxspeed:
        acceleration["x"] -= speed
    if keys[pygame.K_RIGHT] and acceleration["x"] < maxspeed:
        acceleration["x"] += speed
    if keys[pygame.K_UP] and acceleration["y"] > -maxspeed:
        acceleration["y"] -= speed
    if keys[pygame.K_DOWN] and acceleration["y"] < maxspeed:
        acceleration["y"] += speed

    # 位置の更新
    rect_x += acceleration["x"]
    rect_y += acceleration["y"]

    # 摩擦を適応
    if acceleration["x"] > 0:
        acceleration["x"] -= friction["x"]
        if acceleration["x"] < 0:  # 逆符号になったら 0
            acceleration["x"] = 0
    elif acceleration["x"] < 0:
        acceleration["x"] += friction["x"]
        if acceleration["x"] > 0:  # 逆符号になったら 0
            acceleration["x"] = 0
    if acceleration["y"] > 0:
        acceleration["y"] -= friction["y"]
        if acceleration["y"] < 0:
            acceleration["y"] = 0
    elif acceleration["y"] < 0:
        acceleration["y"] += friction["y"]
        if acceleration["y"] > 0:
            acceleration["y"] = 0

    # 画面更新処理
    screen.fill((255, 255, 255))  # 背景を白で塗りつぶす
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
    pygame.display.update()

    # 60FPSに設定
    clock.tick(60)

# 終了処理
pygame.quit()
