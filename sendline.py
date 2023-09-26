#Program: Send Line Message
#Date: 2023.09.25

def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload)

#Send Message
def _lineNotify(payload,file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = 'qa1OII0d4mrbIKQSHsXr5VtxiEvpcYxVgAkbAVNg2rg'
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data = payload, files=file)

#Send Sticker
def notifySticker(stickerID,stickerPackageID):
    payload = {'message':" ",'stickerPackageId':stickerPackageID,'stickerId':stickerID}
    return _lineNotify(payload)

#Send Image
def notifyPicture(url):
    payload = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
    return _lineNotify(payload)

lineNotify('Hello World')
notifySticker(11,1)
#notifyPicture("ที่อยู่รูปภาพ")
