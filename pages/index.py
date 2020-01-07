# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Can you trust that squirrel in Central Park? 

            Squirrels of Central Park is an app that lets you safely gauge if a squirrel will run away when approached by a person. One should never endanger themselves or squirrels while using this app. 

            This app is not to be used lightly, given the power of knowing if a squirrel will run or not is practically a super power and with great power, comes great responsibility. 

            """
        ),
        dcc.Link(dbc.Button('See if that is a good squirrel', color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])