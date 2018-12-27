# Donkeypart Tub Loader

Donkey Carをrecordモードで運転すると、Tubディレクトリ上に
JSONファイルおよびJPG型式のイメージファイルが格納される。

このTubディレクトリ上のすべてのデータを連番の昇順に1件づつ読み込み、
Vehicleフレームワークが管理しているメモリ上に展開するパーツクラス TubLoader を提供する。

# インストール

1. donkeypart_tub_loader パッケージをインストール
   ```bash
   git clone https://github.com/coolerking/donkeypart_tub_loader.git
   pip install -e ./donkeypart_tub_loader
   ```
2. `~/mycar/manage.py` を編集
   ```python

    V = dk.vehicle.Vehicle()
    :

    # Vehicleインスタンス生成から
    # start()実行の間の行内の適当に
    # 次のコードを挿入

    # Tubデータを1件づつ取得
    from donkeypart_tub_loader import TubLoader
    loader = TubLoader(cfg.TUB_PATH)
    v.add(loader, outputs=[
        'cam/image_array',
        'user/mode',
        'user/angle',
        'user/throttle',
        'pilot/angle',
        'pilot/throttle',
        'angle',
        'throttle'])
    
    :
    # run the vehicle
    V.start(rate_hz=cfg.DRIVE_LOOP_HZ,
            max_loop_count=cfg.MAX_LOOPS)
    :
    '''

> デフォルトTubディレクトリパス(`~/mycar/tub`)以外を指定したい場合は、`cfg.TUB_PATH`を修正する。

# 実行

`manage.py` を `drive` モードで実行します。

```bash
python manage.py drive --js
```

# ライセンス

[MIT ライセンス](./LICENSE) 準拠とする。
