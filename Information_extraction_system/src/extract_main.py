import json
import http.client

obj = {"str": "李世玺是一名航空航天学院的学生，他在创作一个睡觉系统"}
req_str = json.dumps(obj)

conn = http.client.HTTPSConnection("texsmart.qq.com")
conn.request("POST", "/api", req_str)
response = conn.getresponse()
print(response.status, response.reason)
res_str = response.read().decode('utf-8')
print(res_str)


# 将JSON格式的字符串转换为Python字典
# res_json = json.loads(res_str)
# # 使用json.dumps方法并设置indent参数来格式化输出
# formatted_str = json.dumps(res_json, indent=4, ensure_ascii=False)

# # 打印格式化后的JSON字符串
# print(formatted_str)
# print(res_json["entity_list"])


# print(json.loads(res_str))
