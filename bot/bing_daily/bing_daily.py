import requests

def bing_daily():
    # URL to fetch the Bing daily image JSON
    image_api_url = "https://bing.com/HPImageArchive.aspx?format=js&n=1&mkt=zh-CN"
    try:
        # Send GET request to fetch the image JSON
        response = requests.get(image_api_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()
            # Extract image URL and title
            image_data = data['images'][0]
            image_url = "https://bing.com" + image_data['url']
            image_title = image_data['title']

            # Download the image
            image_response = requests.get(image_url)
            # Check if the request was successful
            if image_response.status_code == 200:
                # Save the image to a file
                image_filename = f"image_bing_wallpaper.jpg"  # Use title as filename
                with open(image_filename, 'wb') as f:
                    f.write(image_response.content)
                # Print success message
                print(f"Image '{image_title}' downloaded and saved as '{image_filename}'")
                # Return the filename of the saved image and the image title
                return image_filename, image_title
            else:
                # If the request to download the image failed, print the error message
                print("Error downloading image:", image_response.status_code)
                return None, None
        else:
            # If the request to fetch JSON failed, print the error message
            print("Error fetching JSON:", response.status_code)
            return None, None
    except Exception as e:
        # Print the exception message if an error occurs
        print("Exception:", e)
        return None, None