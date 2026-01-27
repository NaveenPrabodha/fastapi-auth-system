from dotenv import load_dotenv
from imagekitio import ImageKit
import os

load_dotenv()

imagekit = ImageKit(
    Private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
    Public_key=os.getenv("IMAGEKI_PUBLIC_KEY"),
    url_endpoint=os.getenv("IMAGEKIT_URL_ENDPOINT"),
)