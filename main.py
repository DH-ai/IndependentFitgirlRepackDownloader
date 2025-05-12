import beautiful
import time 

urls =[
    "https://fuckingfast.co/cimfabbtjgok#Days_Gone_--_fitgirl-repacks.site_--_.part21.rar", 
    "https://fuckingfast.co/mlozmi7kgtlz#Days_Gone_--_fitgirl-repacks.site_--_.part22.rar", 
    "https://fuckingfast.co/n45hlztv64d9#Days_Gone_--_fitgirl-repacks.site_--_.part23.rar", 
    "https://fuckingfast.co/oa7wfj32ssrs#Days_Gone_--_fitgirl-repacks.site_--_.part24.rar", 
    "https://fuckingfast.co/wfxc1jla8o03#Days_Gone_--_fitgirl-repacks.site_--_.part25.rar", 
    "https://fuckingfast.co/1ss0jpa93h3u#Days_Gone_--_fitgirl-repacks.site_--_.part26.rar", 
    "https://fuckingfast.co/4h0uvomaypi3#Days_Gone_--_fitgirl-repacks.site_--_.part27.rar", 
    "https://fuckingfast.co/182qvnk8919v#Days_Gone_--_fitgirl-repacks.site_--_.part28.rar", 
    "https://fuckingfast.co/l4sh9fbdioxi#Days_Gone_--_fitgirl-repacks.site_--_.part29.rar", 
    "https://fuckingfast.co/cfi0lpu20485#Days_Gone_--_fitgirl-repacks.site_--_.part30.rar", 
    "https://fuckingfast.co/dh0fm5lzdo85#Days_Gone_--_fitgirl-repacks.site_--_.part31.rar", 
    "https://fuckingfast.co/pzeo2yj9d3ul#Days_Gone_--_fitgirl-repacks.site_--_.part32.rar", 
    "https://fuckingfast.co/5y76icihypbh#Days_Gone_--_fitgirl-repacks.site_--_.part33.rar", 
    "https://fuckingfast.co/nwuoignm1yib#Days_Gone_--_fitgirl-repacks.site_--_.part34.rar", 
    "https://fuckingfast.co/tt3o7dk4ys8i#Days_Gone_--_fitgirl-repacks.site_--_.part35.rar", 
    "https://fuckingfast.co/fn24nwxp9m4i#Days_Gone_--_fitgirl-repacks.site_--_.part36.rar", 
    "https://fuckingfast.co/af0j3f02bo0m#Days_Gone_--_fitgirl-repacks.site_--_.part37.rar", 
    "https://fuckingfast.co/ssbyuqyv1ju5#Days_Gone_--_fitgirl-repacks.site_--_.part38.rar", 
    "https://fuckingfast.co/jn2i8kcbswrs#Days_Gone_--_fitgirl-repacks.site_--_.part39.rar", 
    "https://fuckingfast.co/pyer62ppwomq#Days_Gone_--_fitgirl-repacks.site_--_.part40.rar", 
    "https://fuckingfast.co/2qzzbpkhu4cl#Days_Gone_--_fitgirl-repacks.site_--_.part41.rar", 
    "https://fuckingfast.co/r6jqzyaal0lp#Days_Gone_--_fitgirl-repacks.site_--_.part42.rar", 
    "https://fuckingfast.co/d0im9o19mij4#Days_Gone_--_fitgirl-repacks.site_--_.part43.rar", 
    "https://fuckingfast.co/9kcfuxp1l61w#Days_Gone_--_fitgirl-repacks.site_--_.part44.rar", 
    "https://fuckingfast.co/w461peir9ch4#Days_Gone_--_fitgirl-repacks.site_--_.part45.rar", 
    "https://fuckingfast.co/w1h4p9b9x52v#Days_Gone_--_fitgirl-repacks.site_--_.part46.rar", 
    "https://fuckingfast.co/svhlko6l8r8k#Days_Gone_--_fitgirl-repacks.site_--_.part47.rar", 
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


