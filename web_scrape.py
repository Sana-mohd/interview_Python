from bs4 import BeautifulSoup  
import requests
import json
url="https://www.boohoo.com/womens/skirts"
u1=requests.get(url)
# print(u1.text)
u2=BeautifulSoup(u1.text,"html.parser")
u3=u2.find("div",id="main",role="main",class_="clearfix")
u4=u3.find("div",class_="clearfix search-results-main")
u5=u4.find("div",class_="search-results-container")
u6=u5.find("div",id="primary",class_="primary-content")
u7=u6.find("div",class_="search-result-content js-search-result-content")
u8=u7.find("ul",id="search-result-items",class_="search-result-items tiles-container hide-compare")
# l2=l1.find("div",class_="product-tile-name",itemprop="name")
# l3=l2.find("div",class_="product-pricing")
# l4=l3.find("div",class_="product-pricing-flex-inner",itemprop="offers", itemscope itemtype ="https://schema.org/offer")
# l5=l4.find("product-sales-price",title="Sale Price")
# print(l5.get_text())
list_name=[]
list_price=[]
list_color=[]
main_list=[]
l1=u8.find_all("li",class_="grid-tile")
def main():
    for li in l1:
        local_dict={}
        n=li.find("div",class_="product-tile-name",itemprop="name").get_text().strip()
        n1=li.find("div",class_="product-pricing")
        n2=n1.find("div",class_="product-pricing-flex-inner",itemprop="offers")
        n3=n2.find("span",class_="product-sales-price",title="Sale Price").get_text()
        list_name.append(n)
        list_price.append(n3)
        c=li.find("div",class_="product-swatches")
        local_dict["Name"]=n
        local_dict["Price"]=n3
        dress_one=[]
        if c!=None:
            c1=c.find("ul",class_="swatch-list js-swatch-list")
            c2=c1.find_all("li",class_="product-swatch-item")
            for li in c2:
                b=li.find("a")
                s=b["title"]
                dress_one.append(s)
                list_color.append(dress_one)
                # local_dict["Name"]=n
                # local_dict["Price"]=n3
            local_dict["Color"]=dress_one
        main_list.append(local_dict)
    return main_list

#     print(list_name)
#     print(list_price)
#     print(list_color)
print(main())

f=open("dress.json","w+")
json.dump(main_list,f,indent=4)
f.close()



       