import beautiful
import time
import os



urls = ["https://fuckingfast.co/820vu2kleznl#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part01.rar",
    "https://fuckingfast.co/l7cgt0ieyjxi#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part02.rar",
    "https://fuckingfast.co/dn14eg1wsnkl#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part03.rar",
    "https://fuckingfast.co/7hp2cz7ekf8v#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part04.rar",
    "https://fuckingfast.co/fe575br7kfvg#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part05.rar",
    "https://fuckingfast.co/zm8qul6ok66x#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part06.rar",
    "https://fuckingfast.co/9cpzup6x08mv#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part07.rar",
    "https://fuckingfast.co/60ggracg2p2d#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part08.rar",
    "https://fuckingfast.co/n6unndipwlob#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part09.rar",
    "https://fuckingfast.co/rhm5slv52xfc#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part10.rar",
    "https://fuckingfast.co/qph3lyb6t6c0#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part11.rar",
    "https://fuckingfast.co/84l7wxd9edif#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part12.rar",
    "https://fuckingfast.co/lzdzdjucpo46#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part13.rar",
    "https://fuckingfast.co/m07xt3uqn4kq#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part14.rar",
    "https://fuckingfast.co/qnhzvsqbgxmj#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part15.rar",
    "https://fuckingfast.co/lbw2la7a7d2m#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part16.rar",
    "https://fuckingfast.co/pdgmtjlyne1b#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part17.rar",
    "https://fuckingfast.co/s5jkquw56zp2#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part18.rar",
    "https://fuckingfast.co/sg6ywyx7lefj#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part19.rar",
    "https://fuckingfast.co/rezvmwm4pwl2#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part20.rar",
    "https://fuckingfast.co/j1j9tpf706jb#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part21.rar",
    "https://fuckingfast.co/7phwign5ggjn#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part22.rar",
    "https://fuckingfast.co/32z1whn7ivzm#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part23.rar",
    "https://fuckingfast.co/h51m5mecn9gx#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part24.rar",
    "https://fuckingfast.co/9msf2245mk9y#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part25.rar",
    "https://fuckingfast.co/22sgr610wim0#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part26.rar",
    "https://fuckingfast.co/zhn278jphefn#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part27.rar",
    "https://fuckingfast.co/xstscmfr35yq#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part28.rar",
    "https://fuckingfast.co/xy8748p1b3sy#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part29.rar",
    "https://fuckingfast.co/2nj40on6orql#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part30.rar",
    "https://fuckingfast.co/vun3uq93dcbz#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part31.rar",
    "https://fuckingfast.co/bw1yr1jk1oe3#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part32.rar",
    "https://fuckingfast.co/qgtz0otxkth4#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part33.rar",
    "https://fuckingfast.co/xnupu6w51thl#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part34.rar",
    "https://fuckingfast.co/tjqk4aor9g7e#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part35.rar",
    "https://fuckingfast.co/4bj81enmxswi#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part36.rar",
    "https://fuckingfast.co/rmy7zo53fr67#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part37.rar",
    "https://fuckingfast.co/5085xt62o4f8#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part38.rar",
    "https://fuckingfast.co/0a7n5egttlsb#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part39.rar",
    "https://fuckingfast.co/zudcj4dwnmet#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part40.rar",
    "https://fuckingfast.co/oy9hvl6frz09#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part41.rar",
    "https://fuckingfast.co/o8brtmv7b0zb#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part42.rar",
    "https://fuckingfast.co/0ue6y25c73z2#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part43.rar",
    "https://fuckingfast.co/jomts47rcaml#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part44.rar",
    "https://fuckingfast.co/efvlg8j6b54d#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part45.rar",
    "https://fuckingfast.co/cshtm2fuhy64#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part46.rar",
    "https://fuckingfast.co/37ptitfkq5jh#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part47.rar",
    "https://fuckingfast.co/zm9g9xcl3xjy#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part48.rar",
    "https://fuckingfast.co/o2zh1ztg6fo3#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part49.rar",
    "https://fuckingfast.co/v4kur1vcuy9p#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part50.rar",
    "https://fuckingfast.co/t61rjzlh6m67#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part51.rar",
    "https://fuckingfast.co/i2om0wgxvzln#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part52.rar",
    "https://fuckingfast.co/00zgnpuu4dhs#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part53.rar",
    "https://fuckingfast.co/51amshxwy3fa#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part54.rar",
    "https://fuckingfast.co/kwxnqis2ine4#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part55.rar",
    "https://fuckingfast.co/mxpekb0lcim3#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part56.rar",
    "https://fuckingfast.co/ziswwqi2p8pj#Ghost_of_Tsushima_DC_--_fitgirl-repacks.site_--_.part57.rar",
]

# print(urls)
def check_file_existence(urls):
    for url in urls:
        filename = url.split('#')[1]
        # //check if the file already exists write code hereonly no function and return the name of the file that no exidt
        if not os.path.exists(filename):
            print(filename)
        exit()
# check_file_existence(urls)

# TODO
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
start_time = time.time()

# Your existing code here


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

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Total time elapsed: {elapsed_time:.2f} seconds")