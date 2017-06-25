#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter

image = Image.open("test.png")
blurryImage = image.filter(ImageFilter.GaussianBlur)
blurryImage.save("test_blurred.png")
blurryImage.show()

