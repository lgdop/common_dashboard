#!/usr/local/bin/python2.7
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import os
from flask import Flask

server = Flask(__name__)

app = dash.Dash(__name__,url_base_pathname='/innovation-tools/',server=server)
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
app.config['suppress_callback_exceptions'] = True
app.layout = html.Div([
    #Including local stylesheet
    html.Link(href='/static/common_dashboard_layout.css', rel='stylesheet'),
        html.Div([
        html.Img(
        src='/img/Accenture-logo-red.png',
        style={
            'height' : '100%',
            'width' : '12%',
            'display':'inline-block',
            'float':'left',
            'padding-right':'10px',
            'padding-left':'20px'
        }
       ),
        html.Div([
             html.H1(children='INNOVATION TOOLS',style={'textAlign': 'center','color': '#000000'})
           ],style={'padding-left':'340px','display':'inline-block','float':'left'}),
    #html.Br(),
        html.Img(
        src='/img/logo-client-liberty-color.jpg',
        style={
            'height' : '100%',
            'width' : '12%',
            'display':'inline-block',
            'float':'right',
            'padding-right':'20px'
        }
       )],className='head-conatiner'),
    html.Div([
    #html.Br(),
    html.Div([
        dcc.Tabs(
            id="tabs",
            #parent_className='custom-tabs',
            #className='custom-tabs-container',
            #20B2AA
            style={"height":"20",'textAlign': 'center','color': '#000000','fontWeight':'bold','cursor': 'pointer','align-items': 'center','justify-content': 'center','fontSize': 20},
            #style=tabs_styles,
            children=[
                dcc.Tab(label="BSS", value="bss_tab",selected_style={'color': '#FFFFFF','backgroundColor': '#7F8C8D','fontWeight':'bold',"border": "#A52A2A"}),
                dcc.Tab(label="OSS", value="oss_tab",selected_style={'color': '#FFFFFF','backgroundColor': '#7F8C8D','fontWeight':'bold',"border": "#A52A2A"}),
                ],
            value="bss_tab",
            colors={
                "border": "#FFFFFF",
                "primary": "#F5F5DC",
                "background": "#A6ACAF"
                }
            #vertical="vertical",
            )],style={'textAlign':'center'}
            ),
    html.Br(),
    html.Div(id="tab_content", style={'textAlign':'center'})
    ],className='main-container')
    ])

bss_layout=html.Div([
        html.Br(),
        html.Br(),
        html.Button(id='cdc',
                    n_clicks=0, children = html.A('Code Consolidation & De-Consolidation',href='/cdc/',style={'color':'#000000','fontSize':18,'fontWeight':'bold'}),
                    style={'padding-top':'5px','padding-bottom':'5px','color':'#8B008B','backgroundColor':'#F8C471','width':'300px','borderRadius':'4px'}),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Button(id='dc',
                    n_clicks=0, children = html.A('Dependency Check',href='/dependency_check',style={'color':'#000000','fontSize':18,'fontWeight':'bold'}),
                    style={'padding-top':'5px','padding-bottom':'5px','color':'#00FA9A','backgroundColor':'#F8C471','width':'300px','borderRadius':'4px'}),
       # html.Br(),
       # html.Br(),
       # html.Br(),
       # html.Button(id='sc',
       #             n_clicks=0, children = html.A('Schema Change',href='/schema-change/',style={'color':'#000000','fontSize':18,'fontWeight':'bold'}),
       #             style={'padding-top':'5px','padding-bottom':'5px','color':'#008080','backgroundColor':'#F8C471','width':'300px','borderRadius':'4px'}),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Button(id='rdh',
                    n_clicks=0, children = html.A('Release History',href='/release-history/',style={'color':'#000000','fontSize':18,'fontWeight':'bold'}),
                    style={'padding-top':'5px','padding-bottom':'5px','color':'#008080','backgroundColor':'#F8C471','width':'300px','borderRadius':'4px'}),
        ])

oss_layout=html.Div([
        html.Br(),
        html.Br(),
        html.Button(id='rdh',
                    n_clicks=0, children = html.A('Release History',href='/release-history/',style={'color':'#000000','fontSize':18,'fontWeight':'bold'}),
                    style={'padding-top':'5px','padding-bottom':'5px','color':'#008080','backgroundColor':'#F8C471','width':'300px','borderRadius':'4px'}),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Button(id='sql',
                    n_clicks=0, children = html.A('SQL Table Revision',href='/table-revision/',style={'color':'#000000','fontSize':18,'fontWeight':'bold'}),
                    style={'padding-top':'5px','padding-bottom':'5px','color':'#008080','backgroundColor':'#F8C471','width':'300px','borderRadius':'4px'}),
        ])
@app.callback(Output("tab_content", "children"), [Input("tabs", "value")])
def render_content(tab):
    if tab == "bss_tab":
        return bss_layout
    elif tab == "oss_tab":
        return oss_layout
    else:
        return

if __name__ == '__main__':
    server.run(debug=True)

