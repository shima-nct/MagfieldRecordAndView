import h5py
import numpy as np

# HDF5ファイルの準備
with h5py.File('incremental_frequency_data.h5', 'w') as f:
    # 空のデータセットを作成
    # データタイプと形状を指定し、圧縮を有効にする
    dset = f.create_dataset("frequency_data", (10, 10, 10, 4096), dtype='f', compression="gzip", compression_opts=9)

    # 各格子点における周波数データを順番に生成してファイルに保存

    #
    # z軸の初期位置に移動
    #
    for i in range(10):  # z軸のインデックス
        #
        # y軸の初期位置に移動
        #
        for j in range(10):  # y軸のインデックス
            #
            # x軸の初期位置に移動
            #
            for k in range(10):  # x軸のインデックス
                # 周波数データの生成
                frequency_data = np.random.rand(4096).astype('f')
                # データセットの更新
                dset[k, j, i, :] = frequency_data

                #
                # x軸方向に1グリッド移動
                #
            #
            # y軸方向に1グリッド移動
            #
        #
        # z軸方向に1グリッド移動
        #

print("各点毎に周波数データを生成し、HDF5ファイルに保存しました。")
