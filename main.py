import requests

img_url = 'img_url'
video_url = 'video_url'

def download_image(url=''):
    try:
        r = requests.get(url)
        with open('r_img.jpeg', 'wb') as f:
            f.write(r.content)
        return 'Изображение успеешно загружено!'
    
    except Exception as _ex:
        return 'Что-то пошло не так! Проверьте url'


def download_video(url=''):
    try:
        r = requests.get(url)
        with open('r_video.mp4', 'wb') as f:
            for chunk in r.iter_content(chunk_size=1200 * 768):
                f.write(chunk)

        return 'Видео успешно загружено!'
    
    except Exception as _ex:
        return 'Что-то пошло не так! Проверьте url' 


def main():
    print(download_image(url=img_url))
    print(download_video(url=video_url))

if __name__=='__main__':
    main()