from app import app
from flask import request
from requestApi import createPersonGroup, createPerson, addImageForPerson, detectedFace, identifyPerson, trainPersonGroup, getGroups
from flask import jsonify, make_response


@app.route('/createNewGroup', methods=['GET'])
def createNewGroupId():
    personGroupId = request.args.get('groupId', type=str, default=None)
    name = request.args.get('name', type=str, default = None)
    userData = request.args.get('userData', type=str, default = None)

    status = createPersonGroup(name, userData, personGroupId)
    if status == 200:
        return make_response('Новая группа успешно создана')
    else:
        return make_response('Новая группа не создана' + status)


@app.route('/createPerson', methods=['GET'])
def createNewPerson():
    personGroupId = request.args.get('groupId', type=str, default=None)
    name = request.args.get('name', type=str, default = None)
    userData = request.args.get('userData', type=str, default = None)
    
    image = request.args.get('image', type=str, default = None)

    if image == None:
        personID = createPerson(name, userData, personGroupId)
    else:
        personID = createPerson(name, userData, personGroupId) 
        addImageForPerson(personID, personGroupId, image)
        
    return make_response(jsonify(personID))


@app.route('/detect')
def createNewFaceId():
    image = request.args.get('image', type=str, default=None)

    return make_response(jsonify(detectedFace(image)))
    

@app.route('/addFace', methods=['GET'])
def addFace():
    personGroupId = request.args.get('groupId', type=str, default=None)
    personId = request.args.get('personId', type=str, default=None)
    imageURl = request.args.get('image', type=str, default=None)

    return make_response(jsonify(addImageForPerson(personId, personGroupId, imageURl)))

    
@app.route('/getUserByImage', methods=['GET'])
def getUser():
    image = request.args.get('image', type=str, default = None)
    groupId = request.args.get('groupId', type=str, default = None)
    
    return make_response(jsonify(identifyPerson(image, groupId)))


@app.route('/training', methods=['GET'])
def train():
    groupId = request.args.get('groupId', type=str, default=None)

    return make_response(jsonify(trainPersonGroup(groupId))) 


@app.route('/groups')
def getGroup():
    return make_response(jsonify(getGroups()), 200)