from threading import Thread
import imgkit
import argparse
from urllib.parse import urlparse

def main():
    try:
        with open(args.list.split("=")[1]) as subs:
            for url in subs:
                t = Thread(target=generate_image,args=(url,))
                t.start()
    except Exception as e:
        print('Error opening subs file')
        print(e.with_traceback)
    return

def generate_image(url):
    try:
        if str(url).startswith("https://") or str(url).startswith("http://"):
            print("Parsable with urlparse")
        else:
            url_for_extract = "https://"+ url
        sub_hostname = urlparse(url_for_extract).hostname
        object_name = sub_hostname +'.jpg'
        image_path = 'media/'+ object_name
        imgkit.from_url(url, image_path)
    except Exception as e:
        print(e.with_traceback)
        print("Error generating image for url: {}".format(url))
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process required inputs.')
    parser.add_argument('list', type=str, help='List of hosts/subdomains.')
    args = parser.parse_args()
    main()