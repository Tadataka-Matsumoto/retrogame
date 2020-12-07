class Settings:
    #エイリアン侵略の全設定を格納するクラス

    def __init__(self):
        #ゲームの初期設定
        #画面に関数設定
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #宇宙船の設定
        self.ship_speed = 1.5


        #弾の設定(p27)
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3#p32(弾の制限)









