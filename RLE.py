def RLE_encoding(info):
    key = info.freqList.index(min(info.freqList))
    idx = 0
    new_byteArr = []
    while idx < info.fileSize:
        last = info.byteArr[idx]
        new_byteArr.append(last)
        if last == key:
            new_byteArr.append(last)
        idx += 1
        count = 1
        try:
            while last == info.byteArr[idx]:
                idx += 1
                count += 1
        except:
            pass
        if count > 2:
            new_byteArr.append(key)
            new_byteArr.append(count)
        elif count == 2:
            new_byteArr.append(last)
    return key, new_byteArr

def RLE_decoding(key, byteArr):
    new_byteArr = []
    idx = 0
    while idx < len(byteArr):
        last = byteArr[idx]
        try:
            if key == byteArr[idx+1]:
                if key == byteArr[idx+2]:
                    new_byteArr.append
                else:
                    pass
            else:
                new_byteArr.append(last)
        except:
            pass
        
