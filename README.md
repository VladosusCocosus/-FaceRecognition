# -FaceRecognition

## Настройка для начала роботы: ##
Устанавливаем azure cognitiveservices vision face - pip install azure-cognitiveservices-vision-face

Открываем файл 'settingApi.py' и меняем ENDPOINT, KEY, headers. ENDPOINT можно и KEY получаем в https://portal.azure.com/
<br/>Пример:
![Пример](https://sun3-11.userapi.com/FCRt7AQ_Lg9-I2TzEiYMIrVahne5RaghuG6SpA/RdjQhxN-T9A.jpg)

## Docker ##
sudo docker build -t name:v . <br/>
sudo docker run name:v

## API ##
### Создание новой группы ###
GET /createNewGroup - Создание новой группы<br/>
Аргументы: groupId, name(Название группы), groupData(Описание группы)<br/>
Пример конечной ссылки:
<br/> host/createNewGroup?groupId=ID_группы&name=Название_группы&groupData=Описание_группы

### Создание нового пользователя ###
GET /createPerson<br/>
Аргументы: groupId(Id группы в которую попадет пользователь), name(Имя), userData<br/>
Пример конечной ссылки:
<br/> host/createPerson?groupId=ID_группы&name=Имя_группы&groupData=Описание_группы<br/>
Так же, если передать в агементы image=url_photo, фотография сразу будет привязана к пользователю

### Добавление фотографий к уже имеющимся пользователям ###
GET /addFace
<br/>Аргементы: groupId, personId, image<br/>
Пример конечной ссылки:<br/>
host/addFace?groupId=ID_Группы&personId=Id_пользователя&image=url_image

### Тренировака распознавания ###
GET /train<br/>
Аргументы:groupId<br/>
Пример конечной ссылки:<br/>
host/train?groupId=Id_группы

### Полечение Person по фото ###
GET /getUserByImage<br/>
Аргументы:image, groupId<br/>
Пример конечной ссылки:<br/>
host/getUserByImage?groupId=ID_группы&image=url_image

### Получение всех групп ###
GET /groups<br/>
Аргументы: нет<br/>
Пример конечной ссылки<br/>
host/groups


