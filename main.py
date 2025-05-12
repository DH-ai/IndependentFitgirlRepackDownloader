import beautiful
import time 

urls =[
    "https://fuckingfast.co/svhlko6l8r8k#Days_Gone_--_fitgirl-repacks.site_--_.part47.rar"

]
# print(urls)

##TODO
"""
    0. Solve this error. 
    Error:
        Error fetching URL: 
        HTTPSConnectionPool(host='fuckingfast.co', port=443): Max retries exceeded with url: /tkjquo8nd3u7 (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x0000026903549370>: Failed to resolve 'fuckingfast.co' ([Errno 11001] getaddrinfo failed)"))
    1. Adding multi-threading for concurrent downloads.
    2. Adding a failsafe mechanism that restarts the download of a file that fails for any reason.
    3. Adding a pause and resume feature for handling internet loss.
    4. Implementing a progress bar to show the download progress for each file.
    5. Logging errors and download statuses to a file for debugging and tracking.
    6. Adding a feature to limit the number of concurrent downloads to avoid overloading the network.
    7. Verifying file integrity after download using checksums (if available).
    8. Allowing the user to specify a custom download directory.
    9. Adding support for retrying failed downloads with exponential backoff.
    10. Providing a summary report of all downloads (successes and failures) at the end.

"""
for url in urls:
    # Extract the filename from the URL fragment
    extracted_filename = beautiful.extract_filename_from_url(url)
    if extracted_filename:
        print(f"Extracted filename: {extracted_filename}")
        # Find the download URL
        base_url = url.split('#')[0]
        download_link = beautiful.find_download_url(base_url)
        if download_link:
            print(f"Found download link: {download_link}")
            # Download the file
            beautiful.download_file(download_link, extracted_filename)
        else:
            print("Download URL not found on the page.")
    else:
        print("Filename not found in the URL fragment.")


