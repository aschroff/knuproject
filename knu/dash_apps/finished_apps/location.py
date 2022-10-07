import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from django_plotly_dash import DjangoDash
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('Location', external_stylesheets=external_stylesheets)

mapbox_access_token = open("./knu/dash_apps/finished_apps/mapbox_token.rtf").read()


fig = go.Figure(go.Scattermapbox(
    lat=['49.176074434586205'],
    lon=['8.61769561139786'],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=14
    ),
    text=['Ubstadt-Weiher'],
))

fig.update_layout(
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=49.176074434586205,
            lon=8.61769561139786
        ),
        pitch=0,
        zoom=12
    )
)

app.layout = html.Div([
    dcc.Graph(id='map', figure=fig),

])



#
#
# @app.callback(
#                Output('map', 'figure'),
#               [Input('slider-updatemode', 'value')])
#
# def display_value(value):
#     print('----------TEST')
#     fig = go.Figure(go.Scattermapbox(
#         lat=['45.5017'],
#         lon=['-73.5673'],
#         mode='markers',
#         marker=go.scattermapbox.Marker(
#             size=14
#         ),
#         text=['Montreal'],
#     ))
#
#     fig.update_layout(
#         hovermode='closest',
#         mapbox=dict(
#             accesstoken=mapbox_access_token,
#             bearing=0,
#             center=go.layout.mapbox.Center(
#                 lat=45,
#                 lon=-73
#             ),
#             pitch=0,
#             zoom=value
#         )
#     )
#
#     return fig





