import requests
from lxml.html import etree

class GameskyLogin(object):
    def __init__(self):
        self.url = "http://i.gamersky.com/u/7023870/"
        self.headers = {
            'Cookie':'Hm_lvt_dcb5060fba0123ff56d253331f28db6a=1672478133; ASP.NET_SessionId=1ypjyymhmqpjkdd5hng0rxjz; BAIDU_SSP_lcr=https://www.google.com/; __bid_n=185677734f896339404207; FEID=v10-45ea0bb6fd64cbebdd3e15d6d995cddf3c276539; __xaf_fpstarttimer__=1672478143811; FPTOKEN=og/n/X+DVuCU7tlknFyZyFbljr6yAple4ORDsu7u7qZYbdo/D0wI1NjGEML9WDmilOq3RBUGt8g+nvrMQKrwQfZz4ox66c3eVlk3bDhLtlaC6AWmTfnaz7gM60/EMaJ7Ko/zmQdReB5Y+PrwYwlJfSNiJYS+Pn9XH2vnk4gBOM4Ig3C2//aqG3fG0FvalKXeNOPw3o/yvUI623OX9W6+nBtaosf9nTS8jsXduMLimHPs3mR2Ni3InsR8r57xRuSbKbSpOCZLGRJxxnE+ysMkTxa5pvSuTenmGUUELTyHHx8hnnk3K2eYMWRgLVKCYDRiOBDmV7pT+laJKxgj18Jo+csUWFvE/jyKfaqVtwGENSR6uAiS2kTeCq1hgm8es3klEC19pTbYkM278/ioySkgNA==|ned4nXhu6kQOP+68WbAn2zo7WmdC20Kg4is8KLeO/Ls=|10|211fd96737037f601817afbc0045f5a1; __xaf_fptokentimer__=1672478145615; __xaf_thstime__=1672478146233; .ASPXAUTH=85F8E71ADD8195C351033B60F128BACEF29888105E065388824A3C847E2677A40261A4D75BEA400A60DF6D4641DE912EFE6B4C020616E66975F17708AC1244DECC47924FAC7A7C7E17A63813E7C42054F0E5A63410CCC0E07ABB2591D2D720220D6C4E48F9D94C7313BA166F7ED934D0A5260AE570C286AD70F3CFA30F535858F9343DC782D68E367042C908F352DEE042881E8C94182926A59BC5D35A33ED75645331C05472746CF6250A13EFBF281552FBD745C8DB864616CC207380CBDA93AAC51CEF5D827C61B3E408C1EF5A5BFB1277771C990E622F7F1D2364021E23C93A265C7AE06C7A85BE9C7E65814EB6862DAEA65967DBFAD871BDD7B25D08B3AB124825AAEB49C5BF521FEA7F43107233D177F8D60BA7CD4EC4A0AA27A2C9D96E3B0CDDE244A77CFD05E7DD7D56B7709452A4426A30D6D3EF9878B22C92703161E6251643D7C5627D45D1F86180F3154D33BC2E238E65FAF8C3F953A43FBF9C7271DA9674B8E9534B285A083771577FE3D3F5A0E79DC6180A765C50D8B297C070215A99316363AB2AF6CB51E1C16DF4FAB05110DA82BD1EC2B60D32287D1DCBBB7B7567186C11C0C3F3D45E0C29B733F9AF90675C4B4D501FA9DB35A9FDECF189A3B5B59D4F053EF617FE03296923E1C1327E18A03034FB413E9E16713873575B8593A34AED5BF802C9E79D16B8F3994B16A55D15; isCheck=true; UserCookie={"status":"ok","username":"浩初茜玲","usergroup":4,"email":"","userid":7023870,"logintimes":2,"phonenumber":"18994081531","phonenumberconfirmed":true,"emailconfirmed":false,"userface":"https://image.gamersky.com/avatar/original/movie/movie043.jpg","modifitime":"2022-12-31T17:22:35.0233843+08:00","token":"67e50003bab25093dbf4b2002d9f1c53","guId":"bdce31d7-0b30-4d5e-b1cd-39ae1f93ed02","idcard":0,"qqClass":"no","sinaClass":"no","weixinClass":"no","emailClass":"no","phoneClass":"ok","articleUrl":"http://i.gamersky.com/article/7023870","iscolumn":false,"homeurl":"http://i.gamersky.com/u/7023870/","isUpdateImage":0}; Hm_lpvt_dcb5060fba0123ff56d253331f28db6a=1672645831',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }

    def get_html(self, url, headers):
        res = requests.get(url=url, headers=headers)
        html = res.text
        self.parse_html(html)

    def parse_html(self, html):
        p = etree.HTML(html)
        user_name = p.xpath('//div[@class="tuser-tit"]/span/text()')
        print(user_name)
        regtime = p.xpath('//div[@class="regtime"]/text()')
        print(regtime)

    def run(self):
        self.get_html(self.url, self.headers)

if __name__ == '__main__':
    agent = GameskyLogin()
    agent.run()