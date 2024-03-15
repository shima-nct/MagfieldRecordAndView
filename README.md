各グリッドにおけるデータを直接プロットしようとするとデータ量が過剰になるので，測定データをファイルに保存するスクリプト`exsample_save_to_HDF5_file.py`と，ファイルから読み込んだデータを表示するスクリプト`read_from_HDF5_and_plot_by_plotly_dash.py`に分けています．


### 環境構築
1. 前提条件
    * ユーザーのドキュメントフォルダにプロジェクトのフォルダ（作りたいプログラムの置き場所，作業するためのフォルダ）を作ってあるとします．
    * Visual Studio Code（以下，vscode）を用います．
    * すでにvscodeでプロジェクトフォルダを開き，ターミナルウィンドウも開かれているとします．
1. Venv環境を作る
    * ターミナルからpyランチャーを使う場合
        ```
        py -3 -m venv .venv
        ```
    * Visual Studio Codeから行う場合
        * pythonのスクリプトを開く
        * 右下隅のpython環境をクリック
        * 「インタープリタの選択」，「+仮想環境の作成…」をクリック
        * 「Venv 現在のワークスペースに'.venv'仮想環境を作成します」をクリック
1. Venv環境のアクティベート
    * ターミナルで以下のコマンドを実行
        ```
        .venv\Scripts\Activate
        ```
1. パッケージのインストール
    * 必要なパッケージは`plotly`，`dasy`，`h5py`です．`test_plotly_dash.py`を実行する場合は`pandas`パッケージも必要となります．
    ```
    pip install plotly
    pip dash
    pip install h5py
    pip install pandas
    ```