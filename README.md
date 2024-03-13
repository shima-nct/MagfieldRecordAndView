各グリッドにおけるデータを直接プロットしようとするとデータ量が過剰になるので，測定データをファイルに保存するスクリプト`exsample_save_to_HDF5_file.py`と，ファイルから読み込んだデータを表示するスクリプト`read_from_HDF5_and_plot_by_plotly_dash.py`に分けています．


** 環境構築
1. venv環境を作る
1. `pip install plotly dash`
1. `pip install h5py`