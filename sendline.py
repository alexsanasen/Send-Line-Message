#Program: Send Line Message
#Date: 2023.09.25

#Message
def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload)

#Sticker
#URL: https://developers.line.biz/en/docs/messaging-api/sticker-list/
def notifySticker(stickerID,stickerPackageID):
    payload = {'message':" ",'stickerPackageId':stickerPackageID,'stickerId':stickerID}
    return _lineNotify(payload)

#Image
def notifyPicture(url):
    payload = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
    return _lineNotify(payload)

#Notification
def _lineNotify(payload,file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = 'qa1OII0d4mrbIKQSHsXr5VtxiEvpcYxVgAkbAVNg2rg'
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data = payload, files=file)

mymessage = "Hello World"

lineNotify(mymessage)
notifySticker(11088016,6370)
#notifyPicture("ที่อยู่รูปภาพ")