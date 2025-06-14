# ポンゲームを作ってみる
# 作成開始日：2025/02/22
# 作成者：花音♬
# 協同作成者(AI)：GitHub Copilot

# 改善点リスト
"""
1. プレイヤーの反射の時に、プレイヤーの座標から離れているほど角度を大きくする（中心0度, 最大45度）おｋ
2. ボールを少しずつ加速させる。ただし、プレイヤーが跳ね返した時のみ。また、一試合ごとにリセットさせるおｋ
3. ボールとプレーヤーが一体化しないようにするおｋ
4. 一人用にほどほどに勝てそうな対戦相手(bot)を作るおｋ
5. 演出をもっと考える(追加)
"""

import pygame
import sys
import random
import math
import time

# 初期化
pygame.init()

# 画面を作成
screen = pygame.display.set_mode((800, 600))

# タイトル
pygame.display.set_caption("Pong Game")

# 時間管理
clock = pygame.time.Clock()

# 色
Object_color = (227, 169, 255)
Background_color = (79, 118, 77)

# 物体
player_A = pygame.Rect(50, 250, 8, 90)
player_B = pygame.Rect(740, 250, 8, 90)
ball = pygame.Rect(395, 295, 18, 18)

# 速度と角度
ball_speed_init = 7
ball_speed = ball_speed_init
player_speed = 10
ball_angle = random.uniform(0.25, 2 * math.pi)
ball_dx = ball_speed * math.cos(ball_angle)
ball_dy = ball_speed * math.sin(ball_angle)

# スコア
score = {"player_A": 0, "player_B": 0}
font = pygame.font.Font(None, 74)

# 画面の更新など(初回)
screen.fill(Background_color)
pygame.draw.rect(screen, Object_color, player_A)
pygame.draw.rect(screen, Object_color, player_B)
pygame.draw.ellipse(screen, Object_color, ball)
score_surface = font.render(f"{score['player_A']} : {score['player_B']}", True, Object_color)
screen.blit(score_surface, (300, 10))
pygame.display.flip()

# 起動して待つ
time.sleep(3)

# 本編
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # キー入力
    keys = pygame.key.get_pressed()
    # プレイヤーA（プレイヤーと同じ条件で打ち返すCPU, ボールより少し遅らせて反応させる）
    if ball.y < player_A.y:
        player_A.y -= player_speed * 0.6
    if ball.y > player_A.y:
        player_A.y += player_speed * 0.6
    # プレイヤーB
    if keys[pygame.K_UP]:
        player_B.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_B.y += player_speed

    # プレイヤーAの移動
    if player_A.top <= 0:
        player_A.top = 0
    if player_A.bottom >= 600:
        player_A.bottom = 600
    # プレイヤーBの移動
    if player_B.top <= 0:
        player_B.top = 0
    if player_B.bottom >= 600:
        player_B.bottom = 600

    # ボールの移動
    ball.x += ball_dx
    ball.y += ball_dy

    # ボールの当たり判定
    if ball.top <= 0 or ball.bottom >= 600:
        ball_dy *= -1
        ball_speed += 0.75  # 上下の壁に当たった時に加速
        ball_angle = math.atan2(ball_dy, ball_dx)  # 角度を更新
        ball_dx = ball_speed * math.cos(ball_angle)
        ball_dy = ball_speed * math.sin(ball_angle)

    if ball.colliderect(player_A):
        ball_Difference = (ball.centery - player_A.centery) / (player_A.height / 2)
        ball_angle_deg = ball_Difference * 45  # 最大45度の範囲で角度を設定
        ball_angle = math.radians(ball_angle_deg)
        ball_dx = ball_speed * math.cos(ball_angle)
        ball_dy = ball_speed * math.sin(ball_angle)
        ball_dx = abs(ball_dx)  # Ensure the ball moves to the right

    if ball.colliderect(player_B):
        ball_Difference = (ball.centery - player_B.centery) / (player_B.height / 2)
        ball_angle_deg = ball_Difference * 45  # 最大45度の範囲で角度を設定
        ball_angle = math.radians(ball_angle_deg)
        ball_dx = ball_speed * math.cos(ball_angle)
        ball_dy = ball_speed * math.sin(ball_angle)
        ball_dx = -abs(ball_dx)  # Ensure the ball moves to the left

    if ball.left <= 0:
        score["player_B"] += 1
        ball.x = 395
        ball.y = 295
        ball_speed = ball_speed_init  # 左右の壁で元の速度に戻す
        ball_angle_deg = random.uniform(10, 350)  # 角度を度で表す
        ball_angle = math.radians(ball_angle_deg)  # 度をラジアンに変換
        ball_dx = ball_speed * math.cos(ball_angle)
        ball_dy = ball_speed * math.sin(ball_angle)

    if ball.right >= 800:
        score["player_A"] += 1
        ball.x = 395
        ball.y = 295
        ball_speed = ball_speed_init  # 左右の壁で元の速度に戻す
        ball_angle_deg = random.uniform(10, 350)  # 角度を度で表す
        ball_angle = math.radians(ball_angle_deg)  # 度をラジアンに変換
        ball_dx = ball_speed * math.cos(ball_angle)
        ball_dy = ball_speed * math.sin(ball_angle)

    # 画面の更新など
    screen.fill(Background_color)
    pygame.draw.rect(screen, Object_color, player_A)
    pygame.draw.rect(screen, Object_color, player_B)
    pygame.draw.ellipse(screen, Object_color, ball)
    score_surface = font.render(f"{score['player_A']} : {score['player_B']}", True, Object_color)
    screen.blit(score_surface, (300, 10))
    pygame.display.flip()
    clock.tick(60)

# 終了
pygame.quit()
sys.exit()
