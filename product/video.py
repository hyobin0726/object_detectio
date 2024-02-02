import pyzbar.pyzbar as pyzbar
import cv2
import requests
import json, urllib.request
global BAR_CD_output


n = 1

while(n<5):
    img=cv2.imread('/home/pi/capture/capture_%d.jpg' % n)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    decoded=pyzbar.decode(img)
    if not decoded:
        text = "0"
        n = n+1
    else:
        for d in decoded:
            x, y, w, h = d.rect
            barcode_data = d.data.decode("utf-8")
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            text = '%s' % (barcode_data)
            cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
        break

def BRCD_CD(apikey, startRow, endRow, BAR_BRCD_CD):
    output_list = []

    keyId = ''

    url = 'http://openapi.foodsafetykorea.go.kr/api/' + apikey + '/' + keyId + '/json/' + str(startRow) + '/' + str(
        endRow) + '/BRCD_NO=' + BAR_BRCD_CD

    data = urllib.request.urlopen(url).read()
    output = json.loads(data)
    output = output[keyId]

    try:
        output = output['row']
        output_1 = output[0]

        output_list.append(output_1['PRDLST_NM'])

        return output_list
    except:
        return 'no data'

#########################################

def BAR_CD(apikey, startRow, endRow, BAR_BRCD_CD):
    output_list = []

    keyId = ''

    url = 'http://openapi.foodsafetykorea.go.kr/api/' + apikey + '/' + keyId + '/json/' + str(startRow) + '/' + str(
        endRow) + '/BAR_CD=' + BAR_BRCD_CD

    data = urllib.request.urlopen(url).read()
    output = json.loads(data)

    output = output[keyId]

    try:
        output = output['row']
        output_1 = output[0]

        output_list.append(output_1['PRDLST_NM'])

        return output_list
    except:
        return 'no data'

#########################################


apikey = ''

startRow = 1
endRow = 1
BAR_BRCD_CD = text


BRCD_CD_output = BRCD_CD(apikey, startRow, endRow, BAR_BRCD_CD)
BAR_CD_output = BAR_CD(apikey, startRow, endRow, BAR_BRCD_CD)

def main():
    global name
    if BAR_CD_output != 'no data':
        print(BAR_CD_output)
        name = BAR_CD_output.pop(0)
        print(name)
    else:
        print(0)
        
if __name__=="__main__":
    main()


