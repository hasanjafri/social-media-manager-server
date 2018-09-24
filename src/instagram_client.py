from instapy_cli import api
import requests
import os
from auth import instagram_user, instagram_password

class Instagram_Handler(object):
    def __init__(self):
        self.instagramSession = api.InstapySession()

    def upload_photo(self):
        self.instagramSession.login(instagram_user, instagram_password)
        filename = 'temp.jpg'
        request = requests.get('https://media.licdn.com/dms/image/C5603AQF8kuwkEMxQ0A/profile-displayphoto-shrink_800_800/0?e=1543449600&v=beta&t=EJOGr81rKHEcia7tGvdvN-AJB-IX0PKZJF5j0a9HRHA', stream=True)
        if request.status_code == 200:
            with open(filename, 'wb') as image:
                for chunk in request:
                    image.write(chunk)

            try:
                photo_res = self.instagramSession.upload_photo(filename)
                self.instagramSession.configure_photo(photo_res, 'Looking for full-time opportunities.')
                os.remove(filename)
            except Exception as e:
                return("Error! Failed to upload photo to Instagram! \n %s" % (e))

            return "You uploaded a photo on Instagram!"
        else:
            return "Error! Unable to download image"