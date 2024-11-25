import pandas as pd
import pickle
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# Load the saved Holt-Winters model
with open('Saved_Models/hw_fitted_model.pkl', 'rb') as file:
    hw_model = pickle.load(file)

# Load the saved Auto ARIMA model
with open('Saved_Models/auto_sarima_model.pkl', 'rb') as f:
    auto_sarima_model = pickle.load(f)

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Customer Complaints Forecasting', style={'textAlign': 'center', 'color': '#333', 'fontSize': '36px'}),

    # Date Range Picker
    html.Div([
        html.Label('Select the date range for forecasting:', style={'fontSize': '18px'}),
        dcc.DatePickerRange(
            id='date-picker-range',
            start_date=pd.Timestamp.now().strftime('%Y-%m-%d'),
            end_date=(pd.Timestamp.now() + pd.Timedelta(days=79)).strftime('%Y-%m-%d'),
            display_format='YYYY-MM-DD',
            style={'margin': '10px', 'fontSize': '16px'}
        ),
    ], style={'marginBottom': '20px', 'textAlign': 'center'}),

    # Dropdown for model selection
    html.Div([
        html.Label('Select Forecasting Model:', style={'fontSize': '18px'}),
        dcc.Dropdown(
            id='model-dropdown',
            options=[
                {'label': 'Holt-Winters', 'value': 'holt_winters'},
                {'label': 'Auto ARIMA', 'value': 'auto_arima'},
                {'label': 'Compare Both', 'value': 'both'}
            ],
            value='holt_winters',  # Default model
            style={'width': '300px', 'marginLeft': '220px', 'marginTop': '15px'}
        ),
    ], style={'marginBottom': '20px', 'textAlign': 'center'}),

    # Progress indicator
    dcc.Loading(id="loading-forecast", type="circle", children=[
        html.Button('Forecast', id='forecast-button', n_clicks=0, style={'margin': '10px', 'fontSize': '16px'}),
        dcc.Graph(id='forecast-graph', style={'height': '60vh', 'marginBottom': '20px'})  # Adding bottom margin
    ]),
], style={'padding': '20px', 'backgroundColor': '#f9f9f9', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)'})

# Callback to update the forecast graph
@app.callback(
    Output('forecast-graph', 'figure'),
    [Input('forecast-button', 'n_clicks'),
     Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date'),
     Input('model-dropdown', 'value')]
)
def update_graph(n_clicks, start_date, end_date, model):
    if n_clicks > 0:  # Only update when the button is clicked
        # Validate the date range
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        if start_date >= end_date:
            return go.Figure().update_layout(title="End date must be later than start date.")

        # Calculate the number of steps for forecasting
        steps = (end_date - start_date).days + 1  # Include end date

        try:
            fig = go.Figure()

            if model == 'holt_winters' or model == 'both':
                # Generate forecast using Holt-Winters
                holt_winters_forecast = hw_model.forecast(steps=steps)
                forecast_index = pd.date_range(start=start_date, periods=steps, freq='D')
                fig.add_trace(go.Scatter(x=forecast_index, y=holt_winters_forecast,
                                         mode='lines+markers', name='Holt-Winters Forecast'))

            if model == 'auto_arima' or model == 'both':
                # Generate forecast using Auto ARIMA
                auto_arima_forecast = auto_sarima_model.predict(n_periods=steps)
                forecast_index = pd.date_range(start=start_date, periods=steps, freq='D')
                fig.add_trace(go.Scatter(x=forecast_index, y=auto_arima_forecast,
                                         mode='lines+markers', name='Auto ARIMA Forecast'))

            # Update layout
            fig.update_layout(
                title=f'{model.replace("_", " ").title()} Forecast' if model != 'both' else 'Comparison of Forecasts',
                xaxis_title='Date',
                yaxis_title='Forecasted Value',
                template='plotly_white',
                height=400
            )

            return fig

        except Exception as e:
            return go.Figure().update_layout(title=f"Error generating forecast: {str(e)}")

    # Return empty figure initially
    return go.Figure()

if __name__ == '__main__':
    app.run_server(debug=True)