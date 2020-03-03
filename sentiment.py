from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):

    score = analyser.polarity_scores(sentence)
    compound_score = score['compound']
    return compound_score
