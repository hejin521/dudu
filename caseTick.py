import requests
import json


def caseTick(caseExecSetId, authOrization, platform, page, perPage):
    """
    caseExecSetId 抓包看下你这次任务的 caseExecSetId
    authOrization cms 的 token，不带 Bean
    platform ios/android
    page 第几页
    perPage 本页查出几条数据
    调用举例 caseTick('EXEC_SET_ST_0e76e1e6b9df43cda007d459da909aa4',
         'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiaGVqaW4iLCJnaXZlbk5hbWUiOiIlRTQlQkQlOTUlRTYlOTklOEIiLCJtYWlsIjoiaGVqaW4lNDBrZWVwLmNvbSIsIm1lbWJlck9mIjoiY249S2VlcC1PcCxvdT1ncm91cCxkYz1nb3Rva2VlcCxkYz1jb20iLCJpYXQiOjE2Njk3OTgxNTUsImV4cCI6MTY3MjM5MDE1NX0.dDztakdGH16AqsssvQqSlgU021FDIneVIUODwf04l0A',
         'ios',
         1, 130)
    """
    Authorization = f'Bearer {authOrization}'
    Url = f'https://proxy.cms.gotokeep.com/api/quality-data/testcase/v1/exec/list'
    Key = {
        'caseExecSetId':caseExecSetId,
        'page': page,
        'perPage': perPage
    }
    Headers = {
        'Host': 'proxy.cms.gotokeep.com',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Authorization': Authorization,
        'Connection': 'keep-alive',
        'Origin': 'https://ark.gotokeep.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }

    responseExecItem = requests.get(Url, params = Key, headers = Headers)
    responseJson = responseExecItem.json()
    # print(responseJson)
    caseExecData = responseJson['data']
    caseExecItem = caseExecData['itemList']
    for caseExecItemList in caseExecItem:
        caseExecId = caseExecItemList['caseExecId']
        Data = json.dumps({"caseExecId": caseExecId,"platform": platform,"result":1})
        urlPost = 'https://proxy.cms.gotokeep.com/api/quality-data/testcase/v1/exec/remark'
        requests.post(urlPost, data=Data, headers = Headers)

caseTick('EXEC_SET_ST_65bce8009bc8450ab09c5a203005f62e',
         'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiaGVqaW4iLCJnaXZlbk5hbWUiOiIlRTQlQkQlOTUlRTYlOTklOEIiLCJtYWlsIjoiaGVqaW4lNDBrZWVwLmNvbSIsIm1lbWJlck9mIjoiY249S2VlcC1PcCxvdT1ncm91cCxkYz1nb3Rva2VlcCxkYz1jb20iLCJpYXQiOjE2NzUxNDQ5MjUsImV4cCI6MTY3NzczNjkyNX0.0Hcf9FjdJj4n-sAhLMxFMdDE7QqAC1wAJ7iiWyEQjUA',
         'ios',
         1, 117)
