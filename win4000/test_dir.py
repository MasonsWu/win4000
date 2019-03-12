#  _*_ coding:utf-8 _*_
__author__ = 'xmduke'
import os,re


# project_dir = os.path.abspath(os.path.dirname(__file__))
# print(project_dir)
#
# IMAGES_STORE = os.path.join(project_dir,"pics")
# mobile_images = os.path.join(IMAGES_STORE,'mobile')
# if not os.path.exists(IMAGES_STORE):
#     os.mkdir(IMAGES_STORE)
#     if not os.path.exists(mobile_images):
#         os.mkdir(mobile_images)
#     else:
#         mobile_images
# else:
#     IMAGES_STORE

# start_urls =[]
# for page in range(1,5):
#     page = "http://www.win4000.com/mobile_0_0_0_{0}.html".format(page)
#     start_urls.append(page)
# print(start_urls)

url = "http://www.win4000.com/mobile_detail_153916.html"
pic_urls = []
new_url = re.sub(".html","",url)
print(new_url)

for nums in range(2, 9):
    pic_url = new_url + "_{0}.html".format(nums)
    print(pic_url)
    pic_urls.append(pic_url)
    print(pic_urls)






















