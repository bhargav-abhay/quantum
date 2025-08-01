import pandas as pd 
import dash 
from dash import dcc, html 
from dash.dependencies import Input, Output 
import plotly.express as px 
 
# Load data 
df = pd.read_csv('C:/Users/ABHAY TRIPATHI/OneDrive/Desktop/javascript/combined_sales_data.csv') 
 
# Convert date column to datetime 
df['date'] = pd.to_datetime(df['date']) 
 
# Sort data by date 
df = df.sort_values(by='date') 
 
# Create Dash app 
app = dash.Dash(__name__) 
 
# Define layout 
app.layout = html.Div([ 
    html.H1('Pink Morsel Sales Visualizer'), 
    dcc.Graph(id='sales-graph') 
]) 
 
# Create line chart 
@app.callback( 
    Output('sales-graph', 'figure'), 
    [Input('sales-graph', 'id')] 
) 
def update_graph(id): 
    fig = px.line(df, x='date', y='sales', title='Pink Morsel Sales Over Time') 
    fig.update_layout(xaxis_title='Date', yaxis_title='Sales') 
    return fig 
 
# Run app 
if __name__ == '__main__': 
    app.run()