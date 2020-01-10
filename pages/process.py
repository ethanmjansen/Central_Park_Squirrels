# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [


            

            dcc.Markdown(
            """
            
            # Process  


            #### The Big Question  
             
             
            Squirrels are curious creatures and that helps a Data Scientist expore their creative side when it comes to building a
            predictive model around their behavior. How many squirrels will be born in Spring or Fall? Do Squirrels eat a lot when
            they are nervous? Is a squirrel more likely to attack you in Idaho or Iowa? Most of the questions and their answers are 
            contingent upon the data that is collected. For this dataset I chose the following question:  
            **If you approach a squirrel in Central Park, will it run away from you?**  

            #### Regression or Classification?  
             
             
            Choosing whether or not this was a regression or classification problem wasn't hard to do given the nature of the question. 
            If the question was predicting a continous number, like number of squirrel offspring, then I would have chosen regression. 
            Since this model is predicting a binary answer, whether or not the squirrel runs away from you, classification seemed like 
            the best route.  

            #### Defining the Target  
             
             
            The dataset I found didn't have a target column easily accessible. These are the columns that I was given:  
            
            
            'Longitude', 'Latitude', 'Unique_Squirrel_ID', 'Hectare', 'Shift',
            'Date', 'Hectare_Squirrel_Number', 'Age', 'Primary_Fur_Color',
            'Highlight_Fur_Color', 'Combination_of_Primary_and_Highlight_Color',
            'Color_notes', 'Location', 'Above_Ground_Sighter_Measurement',
            'Specific_Location', 'Running', 'Chasing', 'Climbing', 'Eating',
            'Foraging', 'Other_Activities', 'Kuks', 'Quaas', 'Moans', 'Tail_flags',
            'Tail_twitches', 'Approaches', 'Indifferent', 'Runs_from',
            'Other_Interactions', 'Lat/Long', 'Zip_Codes', 'Community_Districts',
            'Borough_Boundaries', 'City_Council_Districts', 'Police_Precincts','Target'  

            Not exactly user friendly when it comes to selecting a target. I ended up dropping the instances where a squirrel 
            was true for all of the following columns: Approaches, Indifferent, and Runs from. After that I combined 
            Approaches and Runs from, into a Target column and dropped the three previous columns so that a squirrel either 
            approached or ran from someone in a single column.  


            #### Metric and Baseline  
             
             
            After defining the target it became a simple matter of choosing a metric and baseline to go off of. To start, I realized that 
            squirrels were friendly in 1,581 observations and ran away in 1,410. This would mean that the baseline estimate someone could 
            guess would be that a squirrel would be friendly 52.9 percent of the time and the remaining 47.1 percent it would run away. 
            That just leaves choosing a metric to score my model on. I picked accuracy as my metric because if I could beat the baseline 
            accuracy, I would be able to see how useful my model was.   


            #### Leakage and Usefulness  
             
             
            There were no features that gave leakage into my target column in fact when I dropped the inital 3 columns: Approaches, 
            Indifferent, and Runs from. I was able to eliminate all leakage and so my model is watertight when its predictions 
            are made. The usefulness of this model is in the eye of the beholder. Perhaps a scientist would like to figure out why 
            a certain color of squirrel is more prone to running or why squirrels in northern centrall park respond differently 
            than the ones in the southern part. My intention of making the model was to make it fun for park goers.                  
              
              




            """
                ),

    ],
    #md=9,
)

layout = dbc.Row([column1])