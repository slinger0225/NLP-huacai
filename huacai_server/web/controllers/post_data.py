# -*- coding: utf-8 -*-
from flask import Blueprint,request
from common.libs.sent_all import sent_rec
from common.libs.sent_all_test import sent_rec as sent_rec_test
import json

route_post = Blueprint('post', __name__)


@route_post.route("/data", methods=['POST'])
def index():
    #userID = request.values.get("userID")
    #userID = json.loads(userID)
    userInputStory = request.values.get("userInputStory")
    userInputStory = json.loads(userInputStory)
    rec_result = {}
    rec_result = sent_rec(userInputStory)
    print(rec_result)
    return json.dumps(rec_result, ensure_ascii=False)

@route_post.route("/test", methods=['POST'])
def index():
    #userID = request.values.get("userID")
    #userID = json.loads(userID)
    userInputStory = request.values.get("userInputStory")
    userInputStory = json.loads(userInputStory)
    rec_result = {}
    rec_result = sent_rec_test(userInputStory)
    print(rec_result)
    return json.dumps(rec_result, ensure_ascii=False)
