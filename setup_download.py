import requests
import time

# make the request
url ="https://tunnel1.dlproxy.uk/download/b5NhXsARlAJxFIybx5DkHHbxS3njGxS4PNM089CgEmm2dJBypHff7FXsG29Y1BJHyy7jk3yLimH8c2toPoyZ8pDM_IELJ6knZKOSj-LcYw8ImdpzDdM58erVd-0vvOYjRXI5d2sevqP5oCptpdThor8zpLF-mWv0rlJr8Nwz_J3xEIbiXlVkwi7B6n_kGlw-BxU6t_R1uHe0tGdPX8EHnHCfpi6wc71T6t5zzsmqew-aApaF2ZF3bVDLz2xAgzfZGHx-jNk12BHThq97iadLT5i7nA7kB60GCYK1aXdMD1WLs3oRufoX_laFuB4d9L3BbBf094P7a_EaV3n1t9LWVcqMNxlUjyRWGretAFExco7X0s-tNy6Jbko6Ltyjk5heX645yqoqFvr158gfrwbSU2kNZiugVJVZGuX0Nulvi8UTadaFq4eucIrfaRN08-DO5mMD4c6DLTQD6PFgHWGqzxJ6gYhBQC0pwW1d3QJR1IScbxY3d3AoPJc73oSW9BoOnmHq9gZ04vVbRiXRUypXC40aLpHM4-4Y_5wLX5gxYrYdQ4EVmV3WzZu_pynBIMy0y5UVPvAbFTs02DbLskcWVZDIfDLP3LKD3ba4-e67sic?sig=jtuCCvR9W_2gxziMBEKCpELwwl_KEWCB2-ABAeKZYGI"
headers = {
    "authority": "tunnel1.dlproxy.uk",
    "method": "GET",
    "path": "/download/b5NhXsARlAJxFIybx5DkHHbxS3njGxS4PNM089CgEmm2dJBypHff7FXsG29Y1BJHyy7jk3yLimH8c2toPoyZ8pDM_IELJ6knZKOSj-LcYw8ImdpzDdM58erVd-0vvOYjRXI5d2sevqP5oCptpdThor8zpLF-mWv0rlJr8Nwz_J3xEIbiXlVkwi7B6n_kGlw-BxU6t_R1uHe0tGdPX8EHnHCfpi6wc71T6t5zzsmqew-aApaF2ZF3bVDLz2xAgzfZGHx-jNk12BHThq97iadLT5i7nA7kB60GCYK1aXdMD1WLs3oRufoX_laFuB4d9L3BbBf094P7a_EaV3n1t9LWVcqMNxlUjyRWGretAFExco7X0s-tNy6Jbko6Ltyjk5heX645yqoqFvr158gfrwbSU2kNZiugVJVZGuX0Nulvi8UTadaFq4eucIrfaRN08-DO5mMD4c6DLTQD6PFgHWGqzxJ6gYhBQC0pwW1d3QJR1IScbxY3d3AoPJc73oSW9BoOnmHq9gZ04vVbRiXRUypXC40aLpHM4-4Y_5wLX5gxYrYdQ4EVmV3WzZu_pynBIMy0y5UVPvAbFTs02DbLskcWVZDIfDLP3LKD3ba4-e67sic?sig=jtuCCvR9W_2gxziMBEKCpELwwl_KEWCB2-ABAeKZYGI",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-GB,en;q=0.8",
    "priority": "u=0, i",
    "referer": "https://datanodes.to/",
    "sec-ch-ua": "\"Brave\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "cross-site",
    "sec-fetch-user": "?1",
    "sec-gpc": "1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}
filename = "setup.rar"

try:
    response = requests.get(url=url,stream=True,headers=headers)
    response.raise_for_status()    

    total_size = int(response.headers.get('content-length', 0))

    block_size = 10240 
    downloaded_size = 0

    start_time = time.time()
    with open(f"./download/{filename}", 'wb') as file:
        for data in response.iter_content(block_size):
            file.write(data)
            downloaded_size += len(data)
            elapsed_time = time.time() - start_time
            percentage = (downloaded_size / total_size) * 100 if total_size > 0 else 100
            print(f"\rProgress: {percentage:.2f}% ({downloaded_size // (1024 * 1024):.2f} MB / {total_size // (1024 * 1024):.2f} MB) | Elapsed Time: {elapsed_time:.2f} seconds", end='')
    print("\nDownload complete!")

except requests.exceptions.RequestException as e:
    print(f"Error downloading file: {e}")
except Exception as e:
    print(f"An error occurred during download: {e}")