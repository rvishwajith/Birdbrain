# About
BirdBrain is a personal programming project used to help understand neural networks and NLP better, using Twitter's opinions as a baseline.

## Languages
The language being used is **Python 3.7**, running on macOS ARM. The main libraries used are:
- **PyTorch:** Training the model and conducting analysis on the tests.
- **Pandas:** Processing the CSV files.
- **NumPy:** Augmenting data (undersampling) for training.

## Goal
The eventual goal of this topic is to use the model to:
1. Choose some trending topic on Twitter.
2. For that topic, get some plain-text tweets on it (find tweets based on hash-tag).
3. Guess what the user's sentiment is specifically towards the given topic.
4. If the tweet has replies, how do they feel towards the topic. How do they feel towards the user?

## References
All citations used for this project will go here.

### Training & Data Files Used
Training Data File:
https://raw.githubusercontent.com/ajayshewale/Sentiment-Analysis-of-Text-Data-Tweets-/master/data/train.csv
Testing Data File:
https://raw.githubusercontent.com/ajayshewale/Sentiment-Analysis-of-Text-Data-Tweets-/master/data/test.csv
Mapping of Emojis to Sentiment:
https://raw.githubusercontent.com/ajayshewale/Sentiment-Analysis-of-Text-Data-Tweets-/master/data/emoticons.txt