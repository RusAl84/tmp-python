message = {}
# для сообщения мессенджера (поля никнейм, 
# id пользователя, сообщение и время отсылки сообщения);
message["id"] = 743
message["nickName"] = "RusAl84"
message["messageText"] = "Матлогика это боль"
message["timeStamp"] = "06.12.2023 10:08:54"
print(message)
#{
# 'id': 743, 
# 'nickName': 'RusAl84', 
# 'messageText': 'Матлогика это боль', 
# 'timeStamp': '06.12.2023 10:08:54'
# }
import json
str1 = json.dumps(message, ensure_ascii=False) # Сериализация
print(str1)
# {
# "id": 743, 
# "nickName": "RusAl84", 
# "messageText": "Матлогика это боль", 
# "timeStamp": "06.12.2023 10:08:54"
# }
mess1 =  json.loads(str1) # ДеСериализация
print(mess1['nickName'])
# RusAl84