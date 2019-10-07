# -*- coding: utf-8 -*-
import scrapy
import json
from hyw_crawl.items import HywCrawlItem

class HySpider(scrapy.Spider):
    name = 'hy'
    allowed_domains = ['haiyingshuju.com']

    def start_requests(self):
        url = "http://www.haiyingshuju.com/wish_2.0/product/list"

        form_data = {"cids": "", "genTimeEnd": "", "genTimeStart": "", "hwc": "", "index": 1, "intervalRatingEnd": "",
                     "intervalRatingStart": "", "maxNumBoughtEnd": "", "maxNumBoughtStart": "", "merchantStatus": 1,
                     "orderColumn": "max_num_bought", "pageSize": 5000, "pb": "", "pid": "", "pidStatus": 1, "pname": "",
                     "pnameStatus": 1, "ratingEnd": "", "ratingStart": "", "sort": "DESC", "token": "",
                     "totalpriceEnd": "", "totalpriceStart": "", "verified": "", "viewRate1End": "",
                     "viewRate1Start": ""}

        yield scrapy.Request(url, body=json.dumps(form_data), method='POST',meta={"param":form_data})

    def parse(self, response):
        try:
            rsp = json.loads(response.text)
            param = response.meta["param"]
            node_list = rsp["data"]
            item = HywCrawlItem()
            for node in node_list:
                item["pname"] = node["pname"]
                item["pid"] = node["pid"]
                item["cids"] = node["cids"]
                item["rating"] = node["rating"]
                item["totalprice"] = node["totalprice"]
                item["price"] = node["price"]
                item["shipping"] = node["shipping"]
                item["feedTileText"] = node["feedTileText"]
                item["numEntered"] = node["numEntered"]
                item["numRating"] = node["numRating"]
                item["viewRate1"] = node["viewRate1"]
                item["viewRateGrowth"] = node["viewRateGrowth"]
                item["intervalRating"] = node["intervalRating"]
                item["maxNumBought"] = node["maxNumBought"]
                item["genTime"] = node["genTime"]
                item["approvedDate"] = node["approvedDate"]
                item["merchant"] = node["merchant"]
                if len(node["cidName"]):
                    for cat in node["cidName"]:
                        item["aid"] = cat["aid"]
                        item["cname"] = cat["cname"]
                        item["level"] = cat["level"]
                        item["lastModiTime"] = cat["lastModiTime"]
                        item["lastCrawTime"] = cat["lastCrawTime"]
                        item["insertTime"] = cat["insertTime"]
                        item["pl1Name"] = cat["pl1Name"]
                        item["pl2Name"] = cat["pl2Name"]
                        item["pl3Name"] = cat["pl3Name"]
                        item["pl4Name"] = cat["pl4Name"]
                        item["pl5Name"] = cat["pl5Name"]
                data = node["viewDay"]["viewData"]
                time = node["viewDay"]["viewTime"]
                item["viewData"] = " ".join('%s' %dat for dat in data) if data else ""
                item["viewTime"] = " ".join('%s' %dat for dat in data) if time else ""
            yield item
            page = param.get("index", None)
            if page:
                param["index"] = page + 1
                yield scrapy.Request("http://www.haiyingshuju.com/wish_2.0/product/list", body=json.dumps(param), method='POST', meta={"param": param})
        except:
            pass
