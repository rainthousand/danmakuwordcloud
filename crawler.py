import requests
import json
import chardet
import re
from pprint import pprint
# 1.根据bvid请求得到cid
def get_cid(tempstr):
    url = 'https://api.bilibili.com/x/player/pagelist?bvid='+tempstr+'&jsonp=jsonp'
    res = requests.get(url).text     # 返回json
    json_dict = json.loads(res)      #转化为dict
    return json_dict["data"][0]["cid"]     # return cid

# 2.根据cid请求弹幕，解析弹幕得到最终的数据
def get_data(cid):
    final_url = "https://api.bilibili.com/x/v1/dm/list.so?oid=" + str(cid)
    final_res = requests.get(final_url)
    final_res.encoding = chardet.detect(final_res.content)['encoding']    # detect返回字典，检查编码
    final_res = final_res.text
    # print(":::::::::::::::::::")
    #print(final_res)
    pattern = re.compile('<d.*?>(.*?)</d>')
    data = pattern.findall(final_res)
    # print(":::::::::::::::::::")
    #pprint(final_res)
    return data

# 3.保存弹幕列表
def save_to_file(data):
    with open("danmu.txt", mode="w", encoding="utf-8") as f:
        for i in data:
            f.write(i)
            f.write("\n")

cid = get_cid('BV1YY411V7C7')
data = get_data(cid)
save_to_file(data)


if __name__ == '__main__':
    save_to_file(data)