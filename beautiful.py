import requests
from bs4 import BeautifulSoup
import re
import os
from urllib.parse import urlparse
import time



def extract_filename_from_url(url):
    """
    Extracts the filename from the fragment part of a URL.

    Args:
        url (str): The URL containing the filename in the fragment.

    Returns:
        str or None: The filename if found in the fragment, otherwise None.
    """
    if '#' in url:
        return url.split('#', 1)[1]
    return None

def find_download_url(url):
    """
    Goes to the specified URL, extracts the download URL from the JavaScript function,
    and returns it.

    Args:
        url (str): The URL to visit.

    Returns:
        str or None: The download URL if found, otherwise None.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the <script> tag containing the download function
        script_tags = soup.find_all('script')
        for script in script_tags:
            if 'function download()' in script.text:
                # Extract the URL from the window.open call
                match = re.search(r'window\.open\("([^"]+)"', script.text)
                if match:
                    return match.group(1)
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None
    except Exception as e:
        print(f"An error occurred while parsing the page: {e}")
        return None



def download_file(url, filename):
    """
    Downloads a file from the given URL and displays the download progress.

    Args:
        url (str): The URL of the file to download.
        filename (str): The name to save the file as.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()


        total_size = int(response.headers.get('content-length', 0))
        # print(response.headers)
        # exit()
        block_size = 10240 
        downloaded_size = 0

        print(f"Downloading '{filename}' from '{url}'...")

        start_time = time.time()

        with open(f"./download/{filename}", 'wb') as file:
            for data in response.iter_content(block_size):
                file.write(data)
                downloaded_size += len(data)
                elapsed_time = time.time() - start_time
                percentage = (downloaded_size / total_size) * 100 if total_size > 0 else 100
                print(f"\rProgress: {percentage:.2f}% ({downloaded_size // (1024 * 1024):.2f} MB / {total_size // (1024 * 1024):.2f} MB) | Elapsed Time: {elapsed_time:.2f} seconds", end='')
        print("\nDownload complete!")
        start_time = time.time()
        print(f"\rWait 15 seconds. Cool down time to now overload the network!")
        while True:
            time_left = 15 - (time.time()-start_time)
            if time_left<0:
                break
            print(f"\rWait {time_left:.2f} seconds",end=' ')

        print("Wait Complete!")


    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
    except Exception as e:
        print(f"An error occurred during download: {e}")



def download_file_threading(urls):
    pass



if __name__ == "__main__":
    target_url_with_filename = input("Enter the URL (e.g., https://fuckingfast.co/e2izzpmkcxcn#filename.rar): ")
    extracted_filename = extract_filename_from_url(target_url_with_filename)
    if extracted_filename:
        print(f"Extracted filename: {extracted_filename}")
        base_url = target_url_with_filename.split('#')[0]
        download_link = find_download_url(base_url)

        if download_link:
            print(f"Found download link: {download_link}")
            download_file(download_link, extracted_filename)
        else:
            print("Download URL not found on the page.") #
    else:

        print("Filename not found in the URL fragment.")

        