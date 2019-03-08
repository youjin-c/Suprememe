# Suprememe bot
[Instagram account](https://www.instagram.com/suprememebot/)<br/>
Suprememe is an automated Instagram bot, which generates product and T-shirt images of  Supreme aesthetics.<br/>
It collects random product, garment images and detects objects in the images to put the Supreme box logo or graphics on them.<br/>
From collecting images, detecting objects, compositing, to posting to the Instagram account, every step is automated.<br/>
## How it works
[Selenium](https://www.seleniumhq.org/), [ImageAI](https://github.com/OlafenwaMoses/ImageAI/tree/master/imageai/Detection), [InstagramAPI](https://github.com/LevPasha/Instagram-API-python), [Pillow](https://pillow.readthedocs.io/en/stable/#)<br>
{image 14}<br>
1. It grabs images from websites: a product image from Alibaba, a white T-shirt image from Google, a graphic image from Instagram(#glitch). All images are chosen randomly.<br>
2. It detects objects in a product image, or a T-shirt image, and choose one object among them.<br>
3. It puts the Supreme box logo if the chosen object is a product image or a T-shirt image, or it puts a graphic image on the chosen T-shirt image.<br>
4. It posts the composited image to the Instagram account.<br>
