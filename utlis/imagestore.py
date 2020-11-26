# -*- coding: utf-8 -*-
from qiniu import Auth, put_file, etag,put_data
# 需要填写你的 Access Key 和 Secret Key
access_key = 'QlEswdbGycco2hDPrsEN0GLCPputgdZhxhAbpqJW'
secret_key = 'SsxDKtVdZjEHUIreq7EyCao_UJi4Jsb7ZKMAGNlV'

def images(file_data):

    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    # 要上传的空间
    bucket_name = 'wyqtest'

    # 上传后保存的文件名
    # key = 'my-python-logo.png'

    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, None, 3600)

    # 要上传文件的本地路径
    # localfile = './sync/bbb.jpg'

    ret, info = put_data(token, None, file_data)
    print(info)
    print('*'*50)
    print(ret)
    if info.status_code==200:
        # 表示上传蔡成功
        return ret.get('key')
    else:
        # 上传失败
        # return -1
        raise Exception('上传图片失败')

if __name__ == '__main__':
    with open('./1.png','rb') as f:
        t=f.read()
        images(t)