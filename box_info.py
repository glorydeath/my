import requests
import datetime

def get_box_info():
    movie_boxing_info_dict = {}
    for timedelta in range(60):
        dt = datetime.datetime.now() - datetime.timedelta(timedelta)
        date_time = dt.strftime(('%Y%m%d'))
        URL = 'https://box.maoyan.com/promovie/api/box/second.json?beginDate={}'.format(date_time)

        r = requests.get(url=URL)
        data = r.json()

        box_info_list = data['data']['list']

        for box_info in box_info_list:
            id = box_info['movieId']
            movie_boxing_info = {'movieName':box_info['movieName'],
                                 'boxInfo':box_info['boxInfo'],
                                 'splitBoxInfo':box_info['splitBoxInfo'],
                                 'date':datetime.datetime.strptime(str(date_time), '%Y%m%d').strftime('%Y-%m-%d')}

            # check if id exists
            if id not in movie_boxing_info_dict.keys():
                movie_boxing_info_dict[id] = []
            movie_boxing_info_dict[id].append(movie_boxing_info)

    return movie_boxing_info_dict
