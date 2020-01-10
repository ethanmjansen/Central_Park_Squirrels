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
        
            # Insights  


            #### The Linear Model  


            I used a logistic regression CV model from scikit-learn to fit a linear model to my data. Despite performing better than a 
            baseline accuracy, it only worked 62 percent of the time when I scored it on my validation test set. I knew that this 
            would be a classification model anyway but it was nice to test it out and see how it performed. Using this model would 
            only give someone a slightly better advantage at prediction than flipping a coin. Feeling like a random forest classifier
            could do better, I set out to fit that model instead.  


            #### The Classification Model  
             
             
            It seems like poetic justice that the model called a random forest classifier would be the eventual winner in the linear vs. 
            classification battle for a squirrel model. The basic random forest classifier using all of the features that wouldn't allow 
            leakage proved to be better than the linear one. When scored on the validation test set it was 67.2 percent accurate!
            It beat the baseline by approximatley 15 percent and I liked that. However, making an app that had a ton of different inputs 
            wouldn't be practical for most people, so I narrowed it down to seven after looking at the feature permutations.

            """
        ), 

        html.Img(src='assets/Permutations.PNG', className='img-fluid', style = {'height': '400px'}),

        dcc.Markdown(

            '''
            It can be seen that many of the different features didn't hold very much weight in how they effected the model. I opted 
            to keep only the "fun" ones. Those seven features are:  
            'Shift', 'Foraging', 'Longitude', 'Latitude', 'Primary_Fur_Color', 'Eating', 'Highlight_Fur_Color'  
            Most of the features are pretty self explanatory except for Shift, which I replaced on the app inputs with "Time of Day" 
            The new model was faster and actually scored better on the validation test set with 67.4 percent. 
            '''


                ),

        dcc.Markdown(

            '''
            #### Model Explanation  


            Longitude and Latitude seemed to have some of the most impact on the model's effectivness. I wanted to make partial 
            dependence plots for both of them to see what they could tell someone about their position in Central Park and its 
            effect on squirrel behavior. 



            '''

        ), 
        html.Img(src='assets/pdp_longitude.png', className='img-fluid', style = {'height': '400px'}),
        html.Img(src='assets/pdp_latitude.png', className='img-fluid', style = {'height': '400px'}), 

        dcc.Markdown(

        '''
        The partial dependence plots can tell us some insightful things about the model. The one for Longitude seems to suggest that 
        there is a squirrel dead zone between -73.970 and -73.965. What could be causing this dead zone? I have no idea but 
        I do know that that zone has a particular effect on the model. If you move the slider into that dead zone you will see what 
        I mean. The second plot about Latitude clearly says that the higher in latitude you go, the less squirrels there are. Again, 
        for reasons unknown to myself but if you move the slider up into the higher latitude numbers the squirrels are more likely to 
        bolt. Perhaps the best way to tell how accurate the model is is by showing a map of Central Park along side a Longitude and 
        Latitude heat map. 
        
        '''


                ),

        html.Img(src='assets/central_park.png', className='img-fluid', style = {'height': '400px'}),
        html.Img(src='assets/double_pdp.png', className='img-fluid', style = {'height': '400px'}),

        dcc.Markdown(


            '''
            I couldn't be more proud that my model accuratley predicted that you won't see squirrels in the lake part of Central Park. 
            I was just pulling your leg about the squirrel dead zone in the Longitude visual, that was the lake!
            It makes sense now that there wouldn't be that many squirrels in that area. A picture is worth a thousand words, and these 
            graphs help us see how accurate the model is, even without it being scored.  

            '''



        ),

        dcc.Markdown(


        '''
        #### The Final Verdict  
         
         
        Now comes the worst part about real world data, it is subject to random chance. I reserved a little bit of my data known as the 
        test set to give a final hoorah and see how my model would react to observations it wasn't trained on. Unfortunatley it didn't 
        do great. My precious squirrel model only scored 60.4 percent on the test set... I was less than pleased but I understand that 
        with more data that I can collect and train on, the better my model would become. I have ploted a confusion matrix to show the 
        false positives and false negatives my model struggled with during the final prediction.  

        '''



        ), 

        html.Img(src='assets/confusion_matrix.png', className='img-fluid', style = {'height': '400px'}), 

 

    ],
)

layout = dbc.Row([column1])
