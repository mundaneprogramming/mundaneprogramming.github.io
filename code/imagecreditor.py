from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def caption_image(img, text, text_color = 'black', fill_color = 'white'):
    # Add 30 pixels to the bottom
    txt_offset = img.size[1] + 10
    txt_padding = txt_offset + 20
    # Create new image instance and set fill color to `fill_color`
    capimg = Image.new("RGB", (img.size[0], txt_padding), fill_color)
    # Create a Draw instance
    capdraw = ImageDraw.Draw(capimg)
    # Add text onto the Draw
    capdraw.text((0, txt_offset), text, text_color)
    # Paste the original image onto the capimg instance
    capimg.paste(img, (0, 0))
    return capimg

imgfname = "/tmp/image.jpg"
img = caption_image(Image.open(imgfname), "Hello world")
img.save("/tmp/captioned-image.jpg")





# from PIL import Image
# from PIL import ImageDraw
# from PIL import ImageFont

# commons_sample_url = 'https://commons.wikimedia.org/wiki/Main_Page#/media/File:Detail_of_Mulher_do_chale_verde_by_Cyprien_Eugene_Boulet.jpg'
# wiki_sample_url = 'https://en.wikipedia.org/wiki/San_Francisco#/media/File:San_francisco_in_fog_with_rays.jpg'



# tmpurl = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Detail_of_Mulher_do_chale_verde_by_Cyprien_Eugene_Boulet.jpg/1200px-Detail_of_Mulher_do_chale_verde_by_Cyprien_Eugene_Boulet.jpg?download'

# # http://stackoverflow.com/questions/16373425/add-text-on-image-using-pil



# import requests
# imgdata = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Detail_of_Mulher_do_chale_verde_by_Cyprien_Eugene_Boulet.jpg/1200px-Detail_of_Mulher_do_chale_verde_by_Cyprien_Eugene_Boulet.jpg?download")
# imgdata.status_code
# from io import BytesIO
# b = BytesIO(imgdata.content)
# img = Image.open(b)
# draw = ImageDraw.Draw(img)
# ## first attempt
# draw.text((0,0), "Sample Text", (255,0, 0))
# img.save("/tmp/sample-out.jpg")
# ## second
# draw = ImageDraw.Draw(img)
# whitespaceimg = Image.new("RGB", (img.size[0], img.size[1] + 30), "white")
# whitespaceimg.paste(img, (0,0))
# whitespaceimg.save("/tmp/hello.jpg")
# # third
# # realized I didn't have to do ImageDraw.Draw(img)
# # https://gist.github.com/fabeat/6621507
# wsp = Image.new("RGB", (img.size[0], img.size[1] + 30), "yellow")
# wsdraw = ImageDraw.Draw(wsp)
# wsdraw.text((10, img.size[1] + 10), "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Rerum vel aliquam quam dolore eius laboriosam, distinctio, atque et repellat hic repudiandae, dignissimos", (30, 30, 30))
# wsp.paste(img, (0,0))
# wsp.save("/tmp/captioned.jpg")




