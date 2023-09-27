#Program: Send Line Message
#Date: 2023.09.25

#Message Function
def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload)

#Sticker Function
#URL: https://developers.line.biz/en/docs/messaging-api/sticker-list/
def notifySticker(stickerID,stickerPackageID):
    payload = {'message':" ",'stickerPackageId':stickerPackageID,'stickerId':stickerID}
    return _lineNotify(payload)

#Image Function
#URL: https://uppic.cloud
def notifyPicture(url):
    payload = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
    return _lineNotify(payload)

#Notification Function
def _lineNotify(payload,file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = 'qa1OII0d4mrbIKQSHsXr5VtxiEvpcYxVgAkbAVNg2rg'
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data = payload, files=file)

#Sending Message
mymessage = "สวัสดีวันอังคาร"
lineNotify(mymessage)
notifySticker(11088016,6370)
#notifyPicture("Image URL")