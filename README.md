**Introduction:**

Thank you for checking out this project! The objective of this script is to enable
mass downloading of pictures from the website https://www.hanime.tv. The script allows
you to pick whatever types of pictures you want from the options provided on the site.
The main part of this program is Selenium, a module that allows python to operate a web browser
(in this case chrome) and fetch important data (in this case pictures). The websites Selenium 
navigates to will not show up in your internet history. I also recommend that you use an IDE with
Python 3 to run this code (like PyCharm or Anaconda) Take at a look at the requirements 
before starting. This code will only work on a Mac.

**Requirements**

Make sure you have Chrome version 83 installed (so that the driver works properly)

Then open this project up with your IDE of choice and use the terminal in the IDE
to install the required modules with the following command

`pip3 install -r requirements.txt`

After that, all you have to do is run the code and input your
choices as you are asked. The pictures scraped from the site will 
be saved in the hanime_images folder within the project directory.

NOTE: Every time the code is run, the hanime_images folder will be cleared.