![](https://github.com/rvishwajith/Birdbrain/blob/main/other/thumbnail.png?raw=true)

# About
BirdBrain is a programming project to help improve my understanding neural networks and natural language processing. I'm using a dataset of Tweets to build a PyTorch model for sentiment analysis, which is used to interpret the opinions of new tweets.

## Development
A documented version of the project's development history can be found at [UpdateNotes.md](/UpdateNotes.md).

## Languages & Libraries
The language being used is **Python 3.7**, running on macOS ARM.
### Libraries
The main libraries being used are:
- **PyTorch:** Training the model and conducting analysis on the tests.
- **Pandas:** Processing the CSV files.
- **NumPy:** Augmenting data (undersampling) for training.




## Project Goals
The eventual goal of this topic is to use the model to:
1. Choose some trending topic on Twitter.
2. For that topic, get some plain-text tweets on it (find tweets based on hash-tag).
3. Guess what the user's sentiment is specifically towards the given topic.
4. If the tweet has replies, how do they feel towards the topic. How do they feel towards the user?

## References
All citations and references that were used for this project will be listed here.
### Training & Data Files Used

**Original Training Dataset**

Link: https://raw.githubusercontent.com/ajayshewale/Sentiment-Analysis-of-Text-Data-Tweets-/master/data/train.csv

**Original Testing Dataset**

Link: https://raw.githubusercontent.com/ajayshewale/Sentiment-Analysis-of-Text-Data-Tweets-/master/data/test.csv

**Emoticons to Emotions Dataset**

Link: https://raw.githubusercontent.com/ajayshewale/Sentiment-Analysis-of-Text-Data-Tweets-/master/data/emoticons.txt