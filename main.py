from PyPDF2 import PdfReader
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash
import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc






external_stylesheets = [dbc.themes.DARKLY]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    dbc.Row([
        dbc.Col(html.Img(src="assets/Color logo - no background.png", height="90px")),
        dbc.Col(html.Img(src="assets/pillar.jpeg", height="90px"))
    ]),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),

    html.Div(id='output-data-upload', ),
])

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')
    all_text = []
    decoded = base64.b64decode(content_string)
    try:
        if 'pdf' in filename:
            # Assume that the user uploaded a CSV file
            reader = PdfReader(filename)
            page = reader.pages[0]

            for page in reader.pages:
                print(page.extract_text())
                t = page.extract_text()
                all_text.append(t)
        else:
            print("Unsupported file type")

    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H2(filename),
        html.H4(all_text),



        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])

@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

if __name__ == '__main__':
    app.run_server(debug=True)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run_server(debug=True)


