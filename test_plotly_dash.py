import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import flask

# サンプルデータを読み込み
df = px.data.iris()  # Plotlyのirisデータセットを使用

# Dashアプリケーションを初期化
# server = flask.Flask(__name__)
# app = dash.Dash(__name__, server = server)
app = dash.Dash(__name__)

# アプリのレイアウトを定義
app.layout = html.Div([
    html.H1("Irisデータセットの散布図"),
    dcc.Dropdown(
        id='species-dropdown',
        options=[{'label': i, 'value': i} for i in df['species'].unique()],
        value='setosa'  # 初期選択値
    ),
    dcc.Graph(id='scatter-plot')
])

# コールバックを定義（Dropdownの選択に応じてグラフを更新）
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('species-dropdown', 'value')]
)
def update_graph(selected_species):
    filtered_df = df[df.species == selected_species]
    fig = px.scatter(filtered_df, x='sepal_width', y='sepal_length',
                     color='species', size='petal_length',
                     hover_data=['petal_width'])
    return fig

# サーバを起動
if __name__ == '__main__':
    # plotly dashのデフォルトポート8050だとブラウザで開いても
    # ERR_CONNECTION_RESETになるのでポートを変更する必要があります．
    app.run_server(host='localhost',port=8005)
