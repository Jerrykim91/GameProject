# import
import pygame, sys
import random
import numpy as np
import pandas as pd
from pygame.locals import QUIT,KEYDOWN,Rect
from RBG import *
from hwLib import *


# 맵 클래스 생성
class Map:
    # 맴버변수
    gMapData = None

    def __init__(self,path='./data/site3.0.csv'):
        self.agv = Agv()
        self.reward = Reward()
        self.game_loadMap(path)
        self.game_init()
        self.game_free()
        # self.map_data()

    # step1 게임 초기화
    def game_init(self):
        log('step1 게임 초기화 OK')
        pygame.init()


    # step2 맵 데이터 로드
    def game_loadMap(self, path):
        try:
            self.gMapData = pd.read_csv('./data/site3.0.csv')
        except Exception as e:
            log('맵 데이터를 불러오지 못했습니다. 종료합니다.', e)
            self.game_free()
        else:
            log('step2 맵 데이터 로드 OK')
        finally:
            pass


    def draw(self):
        # 수치값 및 이미지 경로는 향후 전부 바깥으로 뺀다
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.MARGIN = MARGIN
        self.WINDOW_W, self.WINDOW_H = (WINDOW_SIZE_W, WINDOW_SIZE_H)
        # 배경 이미지 생성
        self.backgroundImg = pygame.image.load(RES_PATH + BG_IMG)
        # 윈도우 생성
        self.screen = pygame.display.set_mode((self.WINDOW_W, self.WINDOW_H))
        # 드로잉이 로드가 걸리므로, 랜더링의 딜레이를 위한값 획득
        self.CLOCK = pygame.time.Clock()
        # 윈도의 제목 설정
        pygame.display.set_caption(WINDOW_CAPTION)
        # 게임 구동 플레그값
        self.Run = True

    def process_turn(self):pass

    def put_new_reward(self):pass
    def game_run(self):
        while self.Run:
            self.CLOCK.tick(27)
            EVENTS = pygame.event.get()
            for event in EVENTS:
                if event.type == QUIT:
                    Run = False



    # step9 게임 종료
    def game_free(self):
        log('step9 게임 종료 OK')
        pygame.quit()
        import sys
        sys.exit()
#

# Agv 클래스
class Agv:pass
    # # 맴버변수
    # color = GRAY  # Agv의 색
    #
    # # 생성자
    # def __init__(self):
    #     self.map = Map()
    #     # self.positions = [(길 주소[0], 길 주소[1])]  #  Agv 위치(길위)
    #    # self.direction = ''  # Agv 의 방향  => 시계방향
    #
    #
    # #Agv 화면에 그린다.
    # def draw(self, screen): pass
    #
    # def move(self):pass
    #
    #
    # # 게임 오버 판정
    # def is_game_over(slef) :pass
    #     #agv 가 충돌하면 에러




# 보상 클래스
class Reward(object):pass
    # def __init__(self):pass
    #
    #
    # def draw(self, screen):pass


#
#

if __name__ == '__main__':
    works = map()
    if works:
        # step2 맵 데이터 로드
        # step3 윈도우 생성및 초기화
        # step4 윈도우에 지형지물 배치
        # step5 AGV 생성 및 드로잉
        # step6 AGV에 딥러닝을 적용한 이동 시뮬레이션 처리, 로그기록(고민)
        # step7 조작 컨트롤러(일시정지, 제개, 등등..) 생략가능
        # step8 게임 종료
        # ai.game_free()
        pass