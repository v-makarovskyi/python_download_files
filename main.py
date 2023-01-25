import requests

img_url = 'img_url'
video_url = 'video_url'

def download_image(url=''):
    try:
        r = requests.get(url)
        with open('r_img.jpeg', 'wb') as f:
            f.write(r.content)
        return('Изображение успеешно загружено!')
    
    except Exception as _ex:
        return('Что-то пошло не так! Проверьте url')



