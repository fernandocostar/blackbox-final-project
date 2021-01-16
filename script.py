import pandas as pd
import aiohttp
import aiofiles
import asyncio
import urllib.request

"""
url: the image's url that is being downloaded
path: the path to where the image will be saved. receives None as default, and this indicates that the file will be saved in the same path as this script

returns True when the download is succeeded, else False
"""
async def download_image(id, url, path=None):
    for _ in range(2):
        try:
            print("started downloading image {}: {}".format(id, url))
            urllib.request.urlretrieve(url, str(id) + ".png")
            print("finished downloading image {}: {}".format(id, url))
            return
        except Exception as err:
            print(err)

"""
path: the dataset file path containing the image urls

returns an array containing the urls as strings
"""
def get_urls(path):
    with open(path, 'r') as csv_file:
        df = pd.read_csv(csv_file, dtype={"Image Url": "string"})
        column = df['Image Url']
        return column

async def main():
    path = '/Users/fernandocr/Documents/uff/tcc/dataset/Data/national-gallery-of-art/national-gallery-art-profiles.csv'
    urls = get_urls(path)
    #    download_image(i, urls[i], '/Users/fernandocr/Documents/uff/tcc/dataset/Data/images/')
    await asyncio.wait([download_image(i, urls[i], '/Users/fernandocr/Documents/uff/tcc/dataset/Data/images/') for i in range(len(urls))])

asyncio.run(main())
