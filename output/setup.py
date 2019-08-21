import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='pear-audio',
     version='0.1',
     scripts=['pear-audio'] ,
     author="Steve Boby George",
     author_email="stevebobygeorge@gmail.com",
     description="A simple Youtube video to mp3 converter using youtube-dl and ffmpeg",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/Esquire-2000",
     packages=setuptools.find_packages(),
     install_requires=['colorama','youtube-dl','requests','urllib3'],

     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
