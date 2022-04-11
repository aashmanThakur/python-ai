from crypt import methods
from flask import Flask,request,jsonify
import csv

all_articles=[]

with open('articles.csv') as f:
    reader=csv.reader(f)
    data=list(reader)
    all_articles=data[1:]

liked_articles=[]
disliked_articles=[]
not_read_articles=[]

app=Flask(__name__)

@app.route('/get_articles')

def get_articles():
    return jsonify({
        'data':all_articles,
        'message':'success'
    })

@app.route('/liked_articles',methods=['POST'])

def liked_articles():
    article=all_articles[0]
    all_articles=all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        'message':'success'
    }),201

@app.route('/disliked_articles',methods=['POST'])

def disliked_article():
    article=all_articles[0]
    all_articles=all_articles[1:]
    disliked_articles.append(article)
    return jsonify({
        'message':'success'
    }),201

@app.route('/not_read_articles',methods=['POST'])

def not_read_article():
    article=all_articles[0]
    all_articles=all_articles[1:]
    not_read_articles.append(article)
    return jsonify({
        'message':'success'
    }),201

if(__name__=='__main__'):
    app.run()