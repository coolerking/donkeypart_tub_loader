# -*- coding: utf-8 -*-
"""
Tubディレクトリ上のTubデータを連番の昇順にVehicleフレームワーク上のメモリへ
展開する Donkey パーツ TubLoader を提供する。
また、Vehicleフレームワーク上のメモリデータの運転情報部分をCSV型式で標準出力へ
表示する Donkey パーツ TubPrinter を提供する。
"""
from .data import Tubs

class TubLoader:
    def __init__(self, tub_dir):
        """
        Tubデータを連番昇順に取得するTubsオブジェクトを生成し、
        インスタンス変数へ格納する。

        引数
            tub_dir         Tubデータディレクトリのパス
        戻り値
            なし
        例外
            Tubディレクトリパスの妥当性検査に不合格の場合
        """
        self.tubs = Tubs(tub_dir)
        self.index = 0
    
    def run(self):
        """
        Tubデータを連番昇順に１件読み込むジェネレータ関数。

        引数
            なし
        戻り値
            i                   イメージデータ（バイナリ）
            r['user/mode']      運転モード
            r['user/angle']     手動操作のアングル値
            r['user/throttle']  手動操作のスロットル値
            r['pilot/angle']    オートパイロットのアングル値
            r['pilot/throttle'] オートパイロットのスロットル値
            r['angle']          採用されたアングル値
            r['throttle']       採用されたスロットル値
        例外
            StopIteration   Tubデータディレクトリパスの妥当性検査に失敗した場合
        """
        total = self.tubs.total()
        if self.index < total:
            r, i = self.tubs.indexOf(self.index)
            user_mode = r['user/mode']
            user_angle = r['user/angle']
            user_throttle = r['user/throttle']
            pilot_angle = r['pilot/angle']
            pilot_throttle = r['pilot/throttle']
            angle = r['angle']
            throttle = r['throttle']
            self.index += 1
            return i, user_mode, user_angle, user_throttle, pilot_angle, pilot_throttle, angle, throttle
        else:
            raise StopIteration()

class TubPrinter:
    """
    Vehiecleフレームワーク上から取得したTubデータをCSV型式で表示する。
    """
    def __init__(self):
        """
        カウンタをセットする。

        引数
            なし
        戻り値
            なし
        """
        self.index = 0
        print('\"no\", \"user/mode\", \"user/angle\", \"user/throttle\", \"pilot/angle\", \"pilot/throttle\", \"angle\", \"throttle\"')

    def run(self, image, user_mode, user_angle, user_throttle, pilot_angle, pilot_throttle, angle, throttle):
        """
        Vehiecleフレームワーク上から取得したTunデータを表示する。

        引数
            image               イメージデータ（バイナリ）
            user_mode           運転モード
            user_angle          手動運転のアングル値
            user_throttle       手動運転のスロットル値
            pilot_angle         オートパイロットのアングル値
            pilot_throttleangle オートパイロットのスロットル値
            angle               採用されたアングル値
            throttle            採用されたスロットル値
        戻り値
            なし
        """
        print('{}, \"{}\", {}, {}, {}, {}, {}, {}'.format(
            str(self.index), user_mode,
            str(user_angle), str(user_throttle), str(pilot_angle), str(pilot_throttle),
            str(angle), str(throttle)
        ))
        self.index += 1


        
