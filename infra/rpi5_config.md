# rpi5 configuration
Each crate typically has a [raspberry pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) as a [housekeeper](http://fixme).

 is a [django](https://www.djangoproject.com/) application

## Initial Configuration Steps
1. Create an image using the [raspberry pi imager](https://www.raspberrypi.com/news/raspberry-pi-imager-imaging-utility/).  Currently this is "Raspberry Pi OS (64 bit)" which is a port of "Debian Bookworm" released 2023-12-05.
1. Configuration as a housekeeper requires:
    1.  SSH enabled (because housekeeper is usually headless).
        1. Do this as part of creating the image
    1.  WiFi enabled (because housekeeper provides WiFi bridge).
        1. Associate a WAP as part of creating the image.
    1.  Create a user account.
        1. Via image creation.
    1.  Wired ethernet enabled (for mellow-net).
        1. After image creation.
    1.  Add applications
        1. After image creation.

##


