# -*- coding: utf-8 -*-
"""
テストクラス、正常終了の場合はTubディレクトリ上のデータを標準出力に表示する。

git clone https://github.com/coolerking/donkeypart_tub_loader.git
pip install -e ./donkeypart_tub_loader
pip install pytest
cd donkeypart_tub_loader/tests
pytest test_tub.py

CSVデータを表示させるには、pytestではなく通常の実行を行う必要がある。

python test_tub.py
"""
import pytest

class TubTester:
    """
    テストクラス
    """
    def __init__(self):
        """
        正解データ、カウンタを
        """
        self.expected =[
            #"user/mode", "user/angle", "user/throttle", "pilot/angle", "pilot/throttle", "angle", "throttle"
            ["user", -0.2, 0.8, 0.0, 0.0, -0.2, 0.8],
            ["user", 0.2, 1.0, 0.0, 0.0, 0.2, 1.0],
            ["user", 0.678, -0.345, 0.0, 0.0, 0.678, -0.345],
            ["user", 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            ["user", 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            ["user", -0.213, 0.099, 0.0, 0.0, -0.213, 0.099]]
        self.index = 0

    def run(self, image_array, user_mode, user_angle, user_throttle, pilot_angle, pilot_throttle, angle, throttle):
        self.test_tub(image_array, user_mode, user_angle, user_throttle, pilot_angle, pilot_throttle, angle, throttle)

    def test_tub(self, image_array, user_mode, user_angle, user_throttle, pilot_angle, pilot_throttle, angle, throttle):
        import numpy as np
        assert type(image_array) is np.ndarray
        assert image_array.dtype == 'uint8'
        assert image_array.shape == (120, 160, 3)
        assert len(self.expected) > self.index
        exp = self.expected[self.index]
        assert user_mode == exp[0]
        assert user_angle == exp[1]
        assert user_throttle == exp[2]
        assert pilot_angle == exp[3]
        assert pilot_throttle == exp[4]
        assert angle == exp[5]
        assert throttle == exp[6]
        self.index += 1


def test():
    import donkeycar as dk
    from donkeypart_tub_loader import TubLoader, TubPrinter

    # テスト用Vehicleオブジェクトの生成
    v = dk.vehicle.Vehicle()

    tubitems = [
        'cam/image_array',
        'user/mode',
        'user/angle',
        'user/throttle',
        'pilot/angle',
        'pilot/throttle',
        'angle',
        'throttle']

    # Tubデータを1件づつ取得
    loader = TubLoader('tub')
    v.add(loader, outputs=tubitems)

    # テストパーツの挿入
    tester = TubTester()
    v.add(tester, inputs=tubitems)

    # TubデータをCSV型式で出力
    printer = TubPrinter()
    v.add(printer, inputs=tubitems)

    try:
        v.start(rate_hz=20, max_loop_count=100000)
    except StopIteration:
        # OK
        assert tester.index == len(tester.expected)

if __name__ == '__main__':
    test()