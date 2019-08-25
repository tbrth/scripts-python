from bs4 import BeautifulSoup
import requests
import argparse
import os
import progressbar

directory_path = ""
url = ""
video_urls = []
video_titles = []

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--directory",
                    type=str,
                    default=directory_path,
                    metavar="<directory path>",
                    help="Directory path of where to save the files")
parser.add_argument("-u", "--url",
                    type=str,
                    default=url,
                    metavar="<directory path>",
                    help="Directory path of where to save the files")
parser.add_argument("-v", "--verbose",
                    help="Increase output verbosity",
                    action="store_true")
args = parser.parse_args()

def test_directory_path(directory_path):
    return os.path.exists(directory_path)

def get_xml_data(url):
    global xml_data
    response = requests.get(url)
    xml_data = BeautifulSoup(response.content, "lxml-xml")

def extract_video_url_info(xml_data):
    global video_urls
    global video_titles
    for item in range(len(xml_data.find_all("item"))):
        video_titles.append(xml_data.find_all("itunes:summary")[item].text)
        video_urls.append(xml_data.find_all("guid")[item].text)

def download_video_urls(video_urls, video_titles, directory_path):
    
    bar = progressbar.ProgressBar(max_value=len(video_urls))

    for increment, video_url, video_title in zip(range(len(video_urls)), video_urls, video_titles):
    
        if args.verbose == True:
            print("\nVERBOSE: Downloading: {}\n{}".format(video_title, video_url))

        bar.update(increment)
        
        download_header = requests.head(video_url)

        download = requests.get(download_header.headers['Location'])

        extension = (download_header.headers['Location'])[-4:]

        open(directory_path + video_title + extension, "wb").write(download.content)
        
        if args.verbose == True:
            print("VERBOSE: Done...")

def main():

    if args.directory:
        directory_path = os.path.expanduser(args.directory) + "/"
        if args.verbose == True:
            print("\nVERBOSE: Directory path: {}".format(directory_path))
            print("Directory exists? {}".format(test_directory_path(directory_path)))
    else:
        directory_path = os.getcwd() + "/saved_panopto_videos"
        if args.verbose == True:
            print("\nVERBOSE: Directory path: {}".format(directory_path))
            print("Directory exists? {}".format(test_directory_path(directory_path)))

    if not test_directory_path(directory_path):
        if args.verbose == True:
            print("VERBOSE: Creating directory: {}".format(directory_path))
        os.makedirs(directory_path, exist_ok=True)
    else:
        if args.verbose == True:
            print("VERBOSE: Folder already exists...")

    if args.url:
        url = args.url
        if args.verbose == True:
            print("VERBOSE: URL: {}".format(url))

    get_xml_data(url)

    extract_video_url_info(xml_data)

    download_video_urls(video_urls, video_titles, directory_path)

if __name__ == "__main__":
    main()
