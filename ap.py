import pandas as pd 
import dash 
from dash import dcc, html 
from dash.dependencies import Input, Output 
import plotly.express as px 
 
# Load data 
df = pd.read_csv('C:/Users/ABHAY TRIPATHI/OneDrive/Desktop/javascript/combined_sales_data.csv') 
 
# Convert date column to datetime 
df['date'] = pd.to_datetime(df['date']) 
 
# Create Dash app 
app = dash.Dash(__name__) 
 
# Define layout 
app.layout = html.Div([ 
    html.H1('Pink Morsel Sales Visualizer', style={'textAlign': 'center'}), 
    dcc.RadioItems( 
        id='region-radio', 
        options=[ 
            {'label': 'North', 'value': 'north'}, 
            {'label': 'East', 'value': 'east'}, 
            {'label': 'South', 'value': 'south'}, 
            {'label': 'West', 'value': 'west'}, 
            {'label': 'All', 'value': 'all'} 
        ], 
        value='all', 
        style={'textAlign': 'center'} 
    ), 
    dcc.Dropdown( 
        id='chart-type-dropdown', 
        options=[ 
            {'label': 'Line Chart', 'value': 'line'}, 
            {'label': 'Bar Chart', 'value': 'bar'} 
        ], 
        value='line' 
    ), 
    dcc.Graph(id='sales-graph') 
]) 
 
# Create chart 
@app.callback( 
    Output('sales-graph', 'figure'), 
    [Input('region-radio', 'value'), 
     Input('chart-type-dropdown', 'value')] 
) 
def update_graph(region, chart_type): 
    if region == 'all': 
        if chart_type == 'line': 
            fig = px.line(df, x='date', y='sales', title='Pink Morsel Sales Over Time') 
        else: 
            fig = px.bar(df, x='date', y='sales', title='Pink Morsel Sales Over Time') 
    else: 
        filtered_df = df[df['region'] == region] 
        if chart_type == 'line': 
            fig = px.line(filtered_df, x='date', y='sales', title=f'Pink Morsel Sales in {region.capitalize()} Region') 
        else: 
            fig = px.bar(filtered_df, x='date', y='sales', title=f'Pink Morsel Sales in {region.capitalize()}  Region') 
    fig.update_layout(xaxis_title='Date', yaxis_title='Sales') 
    return fig 
 
# Run app 
if __name__ == '__main__': 
    app.run_server(debug=True)