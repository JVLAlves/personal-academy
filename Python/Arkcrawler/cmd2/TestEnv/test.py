from PIL import Image

from images.imgs import *
pil_image = Image.open(kaltsit_application_icon)
basewidth =235
wpercent = (basewidth / float(pil_image.size[0]))
hsize = int(float(pil_image.size[1]) * float(wpercent))
pil_image = pil_image.resize((basewidth, hsize))
pil_image.save(kaltsit_application_icon+"small", format="PNG")