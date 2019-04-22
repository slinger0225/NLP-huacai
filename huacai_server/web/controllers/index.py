# -*- coding: utf-8 -*-
from flask import Blueprint,request, json,jsonify

route_index = Blueprint( 'index_page',__name__ )

@route_index.route("/")
def index():
    #data = json.loads(request.form.get('data'))

    # lesson: "Operation System"
    # score: 100
    #lesson = data["lesson"]
    #score = data["score"]

    #info = dict()
    #info['name'] = "pengshuang"
    #info['lesson'] = "lesson"
    #info['score'] = "score"
    return "欢迎来到花菜音乐小程序"
