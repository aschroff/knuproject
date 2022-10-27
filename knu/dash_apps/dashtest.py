import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash import Dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash('Location', external_stylesheets=external_stylesheets)
mapbox_access_token = open("./finished_apps/mapbox_token.rtf").read()

fig = go.Figure(go.Scattermapbox(
    lat=['45.5017'],
    lon=['-73.5673'],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=14
    ),
    text=['Montreal'],
))

fig.update_layout(
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=45,
            lon=-73
        ),
        pitch=0,
        zoom=5
    )
)

app.layout = html.Div([
    dcc.Graph(id='maplocation', figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)


