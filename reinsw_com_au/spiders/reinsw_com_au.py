# -*- coding: utf-8 -*-
from scrapy import Spider, Request, FormRequest
from collections import OrderedDict
import random, time, csv, json
import requests, urllib

class reinsw_com_auSpider(Spider):
    name = "reinsw_com_au"

    start_urls = ['https://www.reinsw.com.au/Web/Advice/Find_a_Member/Custom/Find_Agent.aspx?hkey=a713f7a5-6e87-43d9-a301-a095749ded9c']
    # --------------- Get list of proxy-----------------------#
    proxy_text = requests.get('https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt').text
    list_proxy_temp = proxy_text.split('\n')
    use_selenium = True
    # file = open("proxies.txt", "r")
    # # lines =
    # list_proxy = []
    # for key in file.readlines():
    #     list_proxy.append(key.strip())
    total_count = 0

    list_proxy = []
    for line in list_proxy_temp:
        if line.strip() !='' and (line.strip()[-1] == '+' or line.strip()[-1] == '-'):
            ip = line.strip().split(':')[0].replace(' ', '')
            port = line.split(':')[-1].split(' ')[0]
            list_proxy.append('http://'+ip+':'+port)
    #
    # # datas = []


    def start_requests(self):
        for url in self.start_urls:
            proxy = random.choice(self.list_proxy)
            yield Request(url, callback=self.parse, meta={'proxy': proxy}, errback=self.errCall)
            # yield Request(url, callback=self.parse)

        ##test
        # yield Request(self.start_urls[0], callback=self.parse)
    def parse(self, response):
        ClientContext = response.xpath('//input[@id="__ClientContext"]/@value').extract_first()
        CTRLKEY = ''
        SHIFTKEY = ''
        ctl01_ScriptManager1_TSM = response.text.split('_TSM_CombinedScripts_=')[-1].split('"')[0]
        ctl01_ScriptManager1_TSM = urllib.unquote(ctl01_ScriptManager1_TSM).decode('utf8')
        PageInstanceKey = response.xpath('//input[@id="PageInstanceKey"]/@value').extract_first()
        RequestVerificationToken = response.xpath('//input[@id="__RequestVerificationToken"]/@value').extract_first()
        TemplateUserMessagesID = response.xpath('//input[@id="TemplateUserMessagesID"]/@value').extract_first()
        PageIsDirty = 'false'

        IsControlPostBackctl01_HeaderLogo_HeaderLogoSpan_name = 'IsControlPostBackctl01$HeaderLogo$HeaderLogoSpan'
        IsControlPostBackctl01_HeaderLogo_HeaderLogoSpan_val = response.xpath('//input[@id="IsControlPostBackctl01$HeaderLogo$HeaderLogoSpan"]/@value').extract_first()

        IsControlPostBackctl01_SocialNetworking_SocialNetworking_name = 'IsControlPostBackctl01$SocialNetworking$SocialNetworking'
        IsControlPostBackctl01_SocialNetworking_SocialNetworking_val = response.xpath('//input[@id="IsControlPostBackctl01$SocialNetworking$SocialNetworking"]/@value').extract_first()

        IsControlPostBackctl01_SearchField_name = 'IsControlPostBackctl01$SearchField'
        IsControlPostBackctl01_SearchField_val = response.xpath('//input[@id="IsControlPostBackctl01$SearchField"]/@value').extract_first()

        EVENTTARGET = response.xpath('//input[@id="__EVENTTARGET"]/@value').extract_first()
        EVENTARGUMENT = response.xpath('//input[@id="__EVENTARGUMENT"]/@value').extract_first()

        IsControlPostBackctl01_FooterCopyright_FooterSitemap_name = 'IsControlPostBackctl01$FooterCopyright$FooterSitemap'
        IsControlPostBackctl01_FooterCopyright_FooterSitemap_val = response.xpath('//input[@id="IsControlPostBackctl01$FooterCopyright$FooterSitemap"]/@value').extract_first()

        IsControlPostBackctl01_FooterCopyright_Connectwithus_name = 'IsControlPostBackctl01$FooterCopyright$Connectwithus'
        IsControlPostBackctl01_FooterCopyright_Connectwithus_val = response.xpath('//input[@id="IsControlPostBackctl01$FooterCopyright$Connectwithus"]/@value').extract_first()

        IsControlPostBackctl01_FooterCopyright_REINSWPartners_name = 'IsControlPostBackctl01$FooterCopyright$REINSWPartners'
        IsControlPostBackctl01_FooterCopyright_REINSWPartners_val = response.xpath('//input[@id="IsControlPostBackctl01$FooterCopyright$REINSWPartners"]/@value').extract_first()

        IsControlPostBackctl01_FooterCopyright_FooterPartnersStyle_name = 'IsControlPostBackctl01$FooterCopyright$FooterPartnersStyle'
        IsControlPostBackctl01_FooterCopyright_FooterPartnersStyle_val = response.xpath('//input[@id="IsControlPostBackctl01$FooterCopyright$FooterPartnersStyle"]/@value').extract_first()

        VIEWSTATE = response.xpath('//input[@id="__VIEWSTATE"]/@value').extract_first()

        ctl01_lastClickedElementId_name = 'ctl01$lastClickedElementId'
        ctl01_lastClickedElementId_val = 'id|ctl01_TemplateBody_btnSearchFirm'

        form_data = {'__ClientContext': ClientContext,
                    '__CTRLKEY': CTRLKEY,
                    '__SHIFTKEY': SHIFTKEY,
                    'ctl01_ScriptManager1_TSM': ctl01_ScriptManager1_TSM,
                    'PageInstanceKey': PageInstanceKey,
                    '__RequestVerificationToken': RequestVerificationToken,
                    'TemplateUserMessagesID': TemplateUserMessagesID,
                    'PageIsDirty': 'false',
                    'IsControlPostBackctl01$HeaderLogo$HeaderLogoSpan': '1',
                    'IsControlPostBackctl01$SocialNetworking$SocialNetworking': '1',
                    'IsControlPostBackctl01$SearchField': '1',
                    '__EVENTTARGET': '',
                    '__EVENTARGUMENT': '',
                    'NavMenuClientID': 'ctl01_Primary_NavMenu',
                    'IsControlPostBackctl01$FooterCopyright$FooterSitemap': '1',
                    'IsControlPostBackctl01$FooterCopyright$Connectwithus': '1',
                    'IsControlPostBackctl01$FooterCopyright$REINSWPartners': '1',
                    'IsControlPostBackctl01$FooterCopyright$FooterPartnersStyle': '1',
                    '__VIEWSTATE': VIEWSTATE,
                    'ctl01$lastClickedElementId': 'id|ctl01_TemplateBody_btnSearchFirm',
                    'ctl01$ScriptManager1': '',
                    'ctl01$SearchField$SearchTerms': 'Keyword Search',
                    'ctl01_Primary_NavMenu_i0_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i1_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i2_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i3_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i4_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i5_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i6_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i7_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_ClientState': '',
                    'ctl01$TemplateBody$txtFirmName': '',
                    'ctl01$TemplateBody$txtFirmSuburbOrPostCode': '',
                    # ctl01$TemplateBody$chkFirmScopeOfPractice$16: RS
                    'ctl01$TemplateBody$btnSearchFirm.x': '49',
                    'ctl01$TemplateBody$btnSearchFirm.y': '16',
                    'ctl01$TemplateBody$txtSurname':'',
                    'ctl01$TemplateBody$txtAgentSuburbOrPostCode': '',
                    'ctl01_PageSubNavigationPlaceHolder_Secondary_SubNavigationTree_ClientState': '{"expandedNodes":[],"collapsedNodes":[],"logEntries":[],"selectedNodes":[],"checkedNodes":[],"scrollPosition":0}',
                    'ctl01_GenericWindow_ClientState':'',
                    'ctl01_ObjectBrowser_ClientState': '',
                    'ctl01_ObjectBrowserDialog_ClientState':'',
                    'ctl01_WindowManager1_ClientState':'',
                    '__VIEWSTATEGENERATOR': response.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value').extract_first()}


        find_member_firm_checkboxes = response.xpath('//table[@id="ctl01_TemplateBody_chkFirmScopeOfPractice"]/tr/td')
        for find_member_firm_checkbox in find_member_firm_checkboxes:
            find_member_firm_checkbox_name = find_member_firm_checkbox.xpath('./input/@name').extract_first()
            find_member_firm_checkbox_value = find_member_firm_checkbox.xpath('./input/@value').extract_first()
            form_data[find_member_firm_checkbox_name] = find_member_firm_checkbox_value

            search_type = find_member_firm_checkbox.xpath('./label/text()').extract_first()

            yield FormRequest(response.url, method='POST', callback=self.parse_category, dont_filter=True, formdata = form_data, meta={'search_type': search_type})
            break
    def parse_category(self, response):

        ClientContext = response.xpath('//input[@id="__ClientContext"]/@value').extract_first()
        CTRLKEY = ''
        SHIFTKEY = ''
        ctl01_ScriptManager1_TSM = response.text.split('_TSM_CombinedScripts_=')[-1].split('"')[0]
        ctl01_ScriptManager1_TSM = urllib.unquote(ctl01_ScriptManager1_TSM).decode('utf8')
        PageInstanceKey = response.xpath('//input[@id="PageInstanceKey"]/@value').extract_first()
        RequestVerificationToken = response.xpath('//input[@id="__RequestVerificationToken"]/@value').extract_first()
        TemplateUserMessagesID = response.xpath('//input[@id="TemplateUserMessagesID"]/@value').extract_first()

        VIEWSTATE = response.xpath('//input[@id="__VIEWSTATE"]/@value').extract_first()

        table_tr_tags = response.xpath('//table[@id="ctl01_TemplateBody_grdResults"]/tr')

        next_tag = response.xpath('//input[@alt="Next"]')

        form_data = {'__ClientContext': ClientContext,
                    '__CTRLKEY': CTRLKEY,
                    '__SHIFTKEY': SHIFTKEY,
                    'ctl01_ScriptManager1_TSM': ctl01_ScriptManager1_TSM,
                    'PageInstanceKey': PageInstanceKey,
                    '__RequestVerificationToken': RequestVerificationToken,
                    'TemplateUserMessagesID': TemplateUserMessagesID,
                    'PageIsDirty': 'false',
                    'IsControlPostBackctl01$HeaderLogo$HeaderLogoSpan': '1',
                    'IsControlPostBackctl01$SocialNetworking$SocialNetworking': '1',
                    'IsControlPostBackctl01$SearchField': '1',
                    # '__EVENTTARGET': '',
                    '__EVENTARGUMENT': '',
                    'NavMenuClientID': 'ctl01_Primary_NavMenu',
                    'IsControlPostBackctl01$FooterCopyright$FooterSitemap': '1',
                    'IsControlPostBackctl01$FooterCopyright$Connectwithus': '1',
                    'IsControlPostBackctl01$FooterCopyright$REINSWPartners': '1',
                    'IsControlPostBackctl01$FooterCopyright$FooterPartnersStyle': '1',
                    '__VIEWSTATE': VIEWSTATE,
                    # 'ctl01$lastClickedElementId': 'id|ctl01_TemplateBody_btnSearchFirm',
                    'ctl01$ScriptManager1': '',
                    'ctl01$SearchField$SearchTerms': 'Keyword Search',
                    'ctl01_Primary_NavMenu_i0_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i1_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i2_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i3_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i4_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i5_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i6_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i7_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_ClientState': '',
                    'ctl01_PageSubNavigationPlaceHolder_Secondary_SubNavigationTree_ClientState': '{"expandedNodes":[],"collapsedNodes":[],"logEntries":[],"selectedNodes":[],"checkedNodes":[],"scrollPosition":0}',
                    'ctl01_GenericWindow_ClientState':'',
                    'ctl01_ObjectBrowser_ClientState': '',
                    'ctl01_ObjectBrowserDialog_ClientState':'',
                    'ctl01_WindowManager1_ClientState':'',
                    '__VIEWSTATEGENERATOR': response.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value').extract_first()}

        print('item count: ' + str(len(table_tr_tags)))
        for i, table_tr_tag in enumerate(table_tr_tags):
            if i == 0:
                continue
            if next_tag and i == len(table_tr_tags) - 1:
                continue
            titleHeader_href = table_tr_tag.xpath('./td/a[@class="titleHeader"]/@href').extract_first()
            EVENTTARGET = titleHeader_href.split("__doPostBack('")[-1].split("'")[0]
            form_data['__EVENTTARGET'] = EVENTTARGET
            form_data['ctl01$lastClickedElementId'] = 'id|{}'.format(EVENTTARGET)

            yield FormRequest(response.url, method='POST', callback=self.parse_detail, formdata = form_data, dont_filter=True, meta=response.meta)
            # break
        ctl01_TemplateBody_subTotal = response.xpath('//span[@id="ctl01_TemplateBody_subTotal"]/text()').extract_first()
        ctl01_TemplateBody_lblTotalRows = response.xpath('//span[@id="ctl01_TemplateBody_lblTotalRows"]/text()').extract_first()
        try:
            ctl01_TemplateBody_subTotal = int(ctl01_TemplateBody_subTotal)
            ctl01_TemplateBody_lblTotalRows = int(ctl01_TemplateBody_lblTotalRows)
        except:
            return
        if next_tag and ctl01_TemplateBody_lblTotalRows > ctl01_TemplateBody_subTotal:
            form_data = {'__ClientContext': ClientContext,
                    '__CTRLKEY': CTRLKEY,
                    '__SHIFTKEY': SHIFTKEY,
                    'ctl01_ScriptManager1_TSM': ctl01_ScriptManager1_TSM,
                    'PageInstanceKey': PageInstanceKey,
                    '__RequestVerificationToken': RequestVerificationToken,
                    'TemplateUserMessagesID': TemplateUserMessagesID,
                    'PageIsDirty': 'false',
                    'IsControlPostBackctl01$HeaderLogo$HeaderLogoSpan': '1',
                    'IsControlPostBackctl01$SocialNetworking$SocialNetworking': '1',
                    'IsControlPostBackctl01$SearchField': '1',
                    '__EVENTTARGET': '',
                    '__EVENTARGUMENT': '',
                    'NavMenuClientID': 'ctl01_Primary_NavMenu',
                    'IsControlPostBackctl01$FooterCopyright$FooterSitemap': '1',
                    'IsControlPostBackctl01$FooterCopyright$Connectwithus': '1',
                    'IsControlPostBackctl01$FooterCopyright$REINSWPartners': '1',
                    'IsControlPostBackctl01$FooterCopyright$FooterPartnersStyle': '1',
                    '__VIEWSTATE': VIEWSTATE,
                    # 'ctl01$lastClickedElementId': 'id|ctl01_TemplateBody_btnSearchFirm',
                    'ctl01$ScriptManager1': '',
                    'ctl01$SearchField$SearchTerms': 'Keyword Search',
                    'ctl01_Primary_NavMenu_i0_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i1_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i2_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i3_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i4_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i5_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i6_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i7_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_ClientState': '',
                    'ctl01$TemplateBody$txtFirmName': '',
                    'ctl01$TemplateBody$txtFirmSuburbOrPostCode': '',
                    # ctl01$TemplateBody$chkFirmScopeOfPractice$16: RS
                    'ctl01$TemplateBody$grdResults$ctl53$BotNetxButton.x': '49',
                    'ctl01$TemplateBody$grdResults$ctl53$BotNetxButton.y': '16',
                    'ctl01$TemplateBody$txtSurname':'',
                    'ctl01$TemplateBody$txtAgentSuburbOrPostCode': '',
                    'ctl01_PageSubNavigationPlaceHolder_Secondary_SubNavigationTree_ClientState': '{"expandedNodes":[],"collapsedNodes":[],"logEntries":[],"selectedNodes":[],"checkedNodes":[],"scrollPosition":0}',
                    'ctl01_GenericWindow_ClientState':'',
                    'ctl01_ObjectBrowser_ClientState': '',
                    'ctl01_ObjectBrowserDialog_ClientState':'',
                    'ctl01_WindowManager1_ClientState':'',
                    '__VIEWSTATEGENERATOR': response.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value').extract_first()}
            form_data['ctl01$lastClickedElementId'] = 'id|{}'.format(next_tag[0].xpath('./@name').extract_first())

            # yield FormRequest(response.url, method='POST', callback=self.parse_category, formdata = form_data, dont_filter=True, meta=response.meta)

    def parse_detail(self, response):


        ClientContext = response.xpath('//input[@id="__ClientContext"]/@value').extract_first()
        CTRLKEY = ''
        SHIFTKEY = ''
        ctl01_ScriptManager1_TSM = response.text.split('_TSM_CombinedScripts_=')[-1].split('"')[0]
        ctl01_ScriptManager1_TSM = urllib.unquote(ctl01_ScriptManager1_TSM).decode('utf8')
        PageInstanceKey = response.xpath('//input[@id="PageInstanceKey"]/@value').extract_first()
        RequestVerificationToken = response.xpath('//input[@id="__RequestVerificationToken"]/@value').extract_first()
        TemplateUserMessagesID = response.xpath('//input[@id="TemplateUserMessagesID"]/@value').extract_first()

        VIEWSTATE = response.xpath('//input[@id="__VIEWSTATE"]/@value').extract_first()

        form_data = {'__ClientContext': ClientContext,
                    '__CTRLKEY': CTRLKEY,
                    '__SHIFTKEY': SHIFTKEY,
                    'ctl01_ScriptManager1_TSM': ctl01_ScriptManager1_TSM,
                    'PageInstanceKey': PageInstanceKey,
                    '__RequestVerificationToken': RequestVerificationToken,
                    'TemplateUserMessagesID': TemplateUserMessagesID,
                    'PageIsDirty': 'false',
                    'IsControlPostBackctl01$HeaderLogo$HeaderLogoSpan': '1',
                    'IsControlPostBackctl01$SocialNetworking$SocialNetworking': '1',
                    'IsControlPostBackctl01$SearchField': '1',
                    # '__EVENTTARGET': '',
                    '__EVENTARGUMENT': '',
                    'NavMenuClientID': 'ctl01_Primary_NavMenu',
                    'IsControlPostBackctl01$FooterCopyright$FooterSitemap': '1',
                    'IsControlPostBackctl01$FooterCopyright$Connectwithus': '1',
                    'IsControlPostBackctl01$FooterCopyright$REINSWPartners': '1',
                    'IsControlPostBackctl01$FooterCopyright$FooterPartnersStyle': '1',
                    '__VIEWSTATE': VIEWSTATE,
                    # 'ctl01$lastClickedElementId': 'id|ctl01_TemplateBody_btnSearchFirm',
                    'ctl01$ScriptManager1': '',
                    'ctl01$SearchField$SearchTerms': 'Keyword Search',
                    'ctl01_Primary_NavMenu_i0_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i1_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i2_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i3_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i4_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i5_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i6_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_i7_i0_sm0_ClientState': '',
                    'ctl01_Primary_NavMenu_ClientState': '',
                    'ctl01_PageSubNavigationPlaceHolder_Secondary_SubNavigationTree_ClientState': '{"expandedNodes":[],"collapsedNodes":[],"logEntries":[],"selectedNodes":[],"checkedNodes":[],"scrollPosition":0}',
                    'ctl01_GenericWindow_ClientState':'',
                    'ctl01_ObjectBrowser_ClientState': '',
                    'ctl01_ObjectBrowserDialog_ClientState':'',
                    'ctl01_WindowManager1_ClientState':'',
                    '__VIEWSTATEGENERATOR': response.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value').extract_first()}

        primary_contact = response.xpath('//a[@id="ctl01_TemplateBody_linkButtonPrimaryContact"]')
        if primary_contact:
            time.sleep(1)
            titleHeader_href = primary_contact[0].xpath('./@href').extract_first()
            EVENTTARGET = titleHeader_href.split("__doPostBack('")[-1].split("'")[0]

            form_data['__EVENTTARGET'] = EVENTTARGET
            form_data['ctl01$lastClickedElementId'] = 'id|{}'.format(EVENTTARGET)

            yield FormRequest(response.url, method='POST', callback=self.parse_more_detail, formdata = form_data, dont_filter=True, meta=response.meta)


        table_tr_tags = response.xpath('//table[@id="ctl01_TemplateBody_dlOtherMembers"]/tr')
        print('OtherMembers count: ' + str(len(table_tr_tags)))

        for i, table_tr_tag in enumerate(table_tr_tags):
            time.sleep(1)
            titleHeader_href = table_tr_tag.xpath('./td/a[@class="titleHeader"]/@href').extract_first()
            EVENTTARGET = titleHeader_href.split("__doPostBack('")[-1].split("'")[0]
            form_data['__EVENTTARGET'] = EVENTTARGET
            form_data['ctl01$lastClickedElementId'] = 'id|{}'.format(EVENTTARGET)



            yield FormRequest(response.url, method='POST', callback=self.parse_more_detail, formdata = form_data, dont_filter=True, meta=response.meta)
        #     break

    def parse_more_detail(self, response):
        item = OrderedDict()
        item['Search Type'] = response.meta['search_type']
        item['Agent Name'] = response.xpath('//span[@id="ctl01_TemplateBody_lblAgentName"]/text()').extract_first()
        item['Agency'] = ''
        item['Address'] = ''
        item['Telephone'] = ''
        item['Email'] = ''
        item['Fax'] = ''
        item['Web'] = ''

        data_trs = response.xpath('//div[@id="ctl01_TemplateBody_panFirmDetails"]/table/tr')

        for data_tr in data_trs:
            name = data_tr.xpath('./td[@class="PanelTablePrompt"]/text()').extract_first()
            if name:
                name = name.replace(':', '')
                if name == 'Agent Name':
                    continue
                if name == 'Web':
                    item[name] = data_tr.xpath('./td[@class="PanelTableValue"]/span/a/@href').extract_first()
                elif name == 'Agency':
                    item[name] = data_tr.xpath('./td[@class="PanelTableValue"]/a/text()').extract_first()
                else:
                    item[name] = data_tr.xpath('./td[@class="PanelTableValue"]/span/text()').extract_first()
        self.total_count += 1
        print('total count: ' + str(self.total_count))
        yield item

    def errCall(self, response):
        ban_proxy = response.request.meta['proxy']
        if '154.16.' in ban_proxy:
            ban_proxy = ban_proxy.replace('http://', 'http://eolivr4:bntlyy3@')
        if ban_proxy in self.list_proxy:
            self.list_proxy.remove(ban_proxy)
        if len(self.list_proxy) < 1:
            proxy_text = requests.get('https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt').text
            list_proxy_temp = proxy_text.split('\n')
            self.list_proxy = []
            for line in list_proxy_temp:
                if line.strip() !='' and (line.strip()[-1] == '+' or line.strip()[-1] == '-'):
                    ip = line.strip().split(':')[0].replace(' ', '')
                    port = line.split(':')[-1].split(' ')[0]
                    self.list_proxy.append('http://'+ip+':'+port)

        proxy = random.choice(self.list_proxy)
        # response.request.meta['proxy'] = proxy
        print ('err proxy: ' + proxy)
        if not 'errpg' in response.request.url :
            yield Request(response.request.url,
                          callback=self.parse,
                          meta={'proxy': proxy},
                          dont_filter=True,
                          errback=self.errCall)



    def removeSeveralSpace(self, strContent):
        strContent = strContent.replace('\n', '')
        array = []
        for s in strContent.split(' '):
            if s:
                array.append(s)

        return ' '.join(array)
