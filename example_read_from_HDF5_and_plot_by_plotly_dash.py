import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import h5py
import numpy as np

# HDF5ファイルから周波数データの平均値を読み込む
with h5py.File('incremental_frequency_data.h5', 'r') as f:
    # 全周波数データの平均値を計算（ここではメモリの使用量を考慮して一例としています）
    frequency_means = f['frequency_data'][:].mean(axis=3)

# Dashアプリケーションの初期化
app = dash.Dash(__name__)

# アプリケーションのレイアウト
app.layout = html.Div([
    dcc.Graph(id='frequency-map'),
    html.P("Z Index:"),
    dcc.Slider(
        id='z-slider',
        min=0,
        max=frequency_means.shape[2]-1,
        value=0,
        step=1,
        marks={i: str(i) for i in range(frequency_means.shape[2])}
    )
])

# コールバックの定義
@app.callback(
    Output('frequency-map', 'figure'),
    [Input('z-slider', 'value')]
)
def update_figure(selected_z):
    # 選択されたZ平面のデータを取得
    z_slice = frequency_means[:, :, selected_z]
    
    # 2Dマップのプロット
    fig = go.Figure(data=go.Heatmap(
        z=z_slice,
        colorscale='Viridis'
    ))
    
    # プロットのレイアウト設定
    fig.update_layout(
        title=f'Frequency Data at Z Index {selected_z}',
        autosize=False,
        width=600,  # グラフの幅
        height=600,  # グラフの高さ（幅と同じ値に設定して正方形に）
        margin=dict(l=50, r=50, b=50, t=50),  # マージンの設定
    )
    return fig

# アプリケーションの実行
if __name__ == '__main__':
    # plotly dashのデフォルトポート8050だとブラウザで開いても
    # ERR_CONNECTION_RESETになるのでポートを変更する必要があります．
    app.run_server(port=8005, debug=True, use_reloader=False, dev_tools_hot_reload=False)
