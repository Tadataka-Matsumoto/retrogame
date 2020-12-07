import sys

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    # ゲームのアセットと動作を管理する全体的なクラス(p6)

    def __init__(self):
        # ゲームを初期化し、ゲームのリソースを作成する(p6)
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)#p24
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("エイリアン侵略")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()#p29
        self.aliens = pygame.sprite.Group()#p39

        self._create_fleet()#p39

        # 背景色を設定する(p8)
        self.bg_color = (230, 230, 230)

    def run_game(self):
        # ゲームのメインループを開始する(p6)

        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()#33
            self._update_screen()

    def _update_bullets(self):#p33
        #弾の位置を更新し、古い弾を廃棄する
        #弾の位置を更新する
        self.bullets.update()#p29

        #見えなくなった弾を廃棄する(p32)
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # print(len(self.bullets))

    def _check_events(self):
        # キーボードとマウスのイベントに対応する(p6,p17)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)#p23
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)#p23

    def _check_keydown_events(self, event):  # p23
        # キーを押すイベントに対応する
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:#p24
            sys.exit()
        elif event.key == pygame.K_SPACE:#30
            self._fire_bullet()

    def _check_keyup_events(self, event):#p23
        #キーを離すイベントに対応する
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        #新しい弾を生成し、bulletsグループに追加するp30
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):#p39
        #エイリアンの艦隊を作成する
        #エイリアンを1匹作成し、1列のエイリアンの数を求める
        #各エイリアンの間にはエイリアン1匹分のスペースを空ける
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size#p44
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #画面に収まるエイリアンの列数を決定する
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                                (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #エイリアンの艦隊を作成する
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):#P43
        #エイリアンを1匹作成し列の中に配置する
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)


    def _update_screen(self):
        # ループを追加するたびに画面を再描画する(p8)
        # (表現変わる) 画面上の画像を更新し、あたらしい画面に切り替える(p15)
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)#p39

        # 最新の状態の画面を表示する(p7)
        pygame.display.flip()


if __name__ == '__main__':
    # ゲームのインスタンスを作成し、ゲームを実行する(p7)
    ai = AlienInvasion()
    ai.run_game()

