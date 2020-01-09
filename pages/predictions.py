# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
from numpy import arange

# Imports from this application
from app import app
print('Pipeline loaded!')
#Load Pipeline
pipeline = load('assets/pipeline (4).joblib')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
       
        #dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('#### Longitude'), 
        dcc.Slider(
            id='Longitude', 
            min=-73.981159, 
            max=-73.949722, 
            step=0.0005, 
            value=-73.967238, 
            marks={n: str(n) for n in arange(-73.981159,-73.949722,.0005)}, 
            className='mb-4', 
        ), 
        dcc.Markdown('#### Latitude'),
        dcc.Slider(
            id='Latitude', 
            min=40.764911, 
            max=40.800119, 
            step=0.0005, 
            value=40.780775, 
            #marks={n: str(n) for n in range(1960,2060,20)}, 
            className='mb-4', 
        ),
        dcc.Markdown('#### Primary Fur Color'), 
        dcc.Dropdown(
            id='Primary_Fur_Color', 
            options = [
                {'label': 'Gray', 'value': 'Gray'}, 
                {'label': 'Cinammon', 'value': 'Cinammon'}, 
                {'label': 'Black', 'value': 'Black'}, 
            ], 
            value = 'Gray', 
            className='mb-4', 
        ), 
        dcc.Markdown('#### Highlight Fur Color'), 
        dcc.Dropdown(
            id='Highlight_Fur_Color', 
            options = [
                {'label': 'Cinammon', 'value': 'Cinammon'}, 
                {'label': 'White', 'value': 'White'}, 
                {'label': 'Cinammon, White', 'value': 'Cinammon, White'}, 
                {'label': 'Gray', 'value': 'Gray'}, 
                {'label': 'Gray, White', 'value': 'Gray, White'}, 
                {'label': 'Black', 'value': 'Black'},
                {'label': 'Black, Cinammon, White', 'value': 'Black, Cinammon, White'}, 
                {'label': 'Black, White', 'value': 'Black, White'}, 
                {'label': 'Black, Cinammon', 'value': 'Black, Cinammon'},
                {'label': 'Gray, Black', 'value': 'Gray, Black'},
            ], 
            value = 'Cinammon', 
            className='mb-4', 
        ), 

        
    ],
    md=4,
)

column2 = dbc.Col(
    [
        #dcc.Markdown('## .', className='mb-5'),
        dcc.Markdown('#### Time of Day'), 
        dcc.Dropdown(
            id='Shift', 
            options = [
                {'label': 'AM', 'value': 'AM'}, 
                {'label': 'PM', 'value': 'PM'}, 
            ], 
            value = 'AM', 
            className='mb-4', 
        ),

        dcc.Markdown('#### Foraging'), 
        dcc.Dropdown(
            id='Foraging', 
            options = [
                {'label': 'True', 'value': 'True'}, 
                {'label': 'False', 'value': 'False'}, 
            ], 
            value = 'True', 
            className='mb-4', 
        ),

         dcc.Markdown('#### Eating'), 
        dcc.Dropdown(
            id='Eating', 
            options = [
                {'label': 'True', 'value': 'True'}, 
                {'label': 'False', 'value': 'False'}, 
            ], 
            value = 'True', 
            className='mb-4', 
        ),
     
     
    ]
)

column3 = dbc.Col(
    [

        html.H2('Squirrel Behavior', className='mb-5'), 
        html.Div(id='prediction-image', className='lead'),
        html.Div(id='prediction-content', className='lead') 

    #daq.Gauge(
    #d='my-daq-gauge',
    #min=0,
    #max=10,
    #value=6
    #),  

      
     
     
    ]
)

layout = dbc.Row([column1, column2, column3])


import pandas as pd

@app.callback(
    Output('prediction-content', 'children'),
    [Input('Shift', 'value'), Input('Foraging', 'bool'), Input('Longitude', 'value'), Input('Latitude', 'value'), 
    Input('Primary_Fur_Color', 'value'), Input('Eating', 'bool'), Input('Highlight_Fur_Color', 'value') ],
)
def predict(Shift, Foraging, X, Y, Primary_Fur_Color, Eating, Highlight_Fur_Color):
    df = pd.DataFrame(
        columns=['Shift', 'Foraging', 'Longitude', 'Latitude', 'Primary_Fur_Color', 'Eating', 'Highlight_Fur_Color'], 
        data=[[Shift, Foraging, X, Y, Primary_Fur_Color, Eating, Highlight_Fur_Color]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred}'

@app.callback(
    Output('prediction-image', 'children'),
    [Input('Shift', 'value'), Input('Foraging', 'bool'), Input('Longitude', 'value'), Input('Latitude', 'value'), 
    Input('Primary_Fur_Color', 'value'), Input('Eating', 'bool'), Input('Highlight_Fur_Color', 'value') ],
)

def predict(Shift, Foraging, X, Y, Primary_Fur_Color, Eating, Highlight_Fur_Color):
    df = pd.DataFrame(
        columns=['Shift', 'Foraging', 'Longitude', 'Latitude', 'Primary_Fur_Color', 'Eating', 'Highlight_Fur_Color'], 
        data=[[Shift, Foraging, X, Y, Primary_Fur_Color, Eating, Highlight_Fur_Color]]
    )
    y_pred = pipeline.predict(df)[0]
    if y_pred == True:
        return html.Img(src='assets/squirrel_approach.png',className='img-fluid', style = {'height': '300px'})
    else:
        return html.Img(src='assets/squirrel_runs.png',className='img-fluid', style = {'height': '300px'})

