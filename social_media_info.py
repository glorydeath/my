import requests
import datetime
from box_info import get_box_info

end_time = datetime.datetime.now().strftime('%Y-%m-%d')
weibo_URL = 'https://piaofang.maoyan.com/movie/{}/promption-ajax?method=change&type=weibo&startDate=2018-01-01&endDate=' + end_time
weixin_URL = 'https://piaofang.maoyan.com/movie/{}/promption-ajax?type=wechat&method=changeAccountChart&startDate=2018-01-01&endDate=' + end_time
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def get_social_media_info():
    box_info_dict = get_box_info()
    for movie_id in box_info_dict.keys():
        movie_url = weibo_URL.format(movie_id)

        r = requests.get(url=movie_url, headers=headers)

        data = r.json()
        if 'error' in data:
            print('error. movie id:{}, movie url: {}'.format(movie_id, movie_url))
            continue
        weibo_data_list = data['data']
        for weibo_data in weibo_data_list:
            date = weibo_data['date']
            box_info_list = box_info_dict[movie_id]
            # print(box_info_list)
            for box_info in box_info_list:
                if box_info['date'] == date:
                    box_info.update(weibo_data)

        movie_url = weixin_URL.format(movie_id)

        r = requests.get(url=movie_url, headers=headers)

        data = r.json()
        # print(data)
        if 'error' in data:
            print('error. movie id:{}, movie url: {}'.format(movie_id, movie_url))
            continue
        weixin_data_list = data['data']
        for weixin_data in weixin_data_list:
            date = weixin_data['date']
            box_info_list = box_info_dict[movie_id]
            for box_info in box_info_list:
                if box_info['date'] == date:
                    box_info.update(weixin_data)

    return box_info_dict



if __name__ == '__main__':
    print(get_social_media_info())

