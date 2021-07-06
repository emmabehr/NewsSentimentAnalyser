# News Sentiment Analyser

This script will search news sources for a keyword and then carry out sentiment analysis on the results to determine if the news articles are positive or negative and then will visualise the results using matplotlib

## Requirements
  newsapi
  
  nltk (vader sentiment lexicon)
  
  matplotlib
  
  pandas
  
  Create a file called api.conf with the api key stored in the format:
  ```
{
    "api_key": "<News Api key here>"
}
  ```
  
  &nbsp;
  &nbsp;
  
  
  
  
  
 <h2 align="center"> An example using the politician "Matt Hancock" as the keyword.</h2>
 
 ![Line graph displaying if the recent news for "Matt Hancock" has been positive or negative](https://github.com/emmabehr/NewsSentimentAnalyser/blob/master/img/Figure_1.png)
