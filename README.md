# HydraMeld
A PolyGlot tool for adding hidden zip archives to files.

## My reasons for this project.
I made this because I was thinking about making an ARG using a polyglot file at some point, but from past experience I knew that almost all methods of making a polyglot with an embeded zip archive would not work with the built in windows zip extraction, so I decided to make this project, I just threw some stuff together and have tested that the basic fundementals work, however, if there are any bugs, or unsupported file types, please notify me so I may be able to add them to the project.

This script has also been made in such a way so that it can be used as a module for other python projects as well, so feel free to incorperate it however you wish!

## Supported file types.
- Image file types:
  - **PNG**
  - **JPEG**
  - **JPG**
  - **GIF**
  - **WebP**
  - **BMP**
  - **TIFF** > (both .tiff and .tif)
  - **ICO**
  - **CUR**
  - **ICNS**
  - **PSD**
- Video file types:
  - **MP4**
  - **MOV**
  - **MKV**
  - **AVI**
  - **WebM**
  - **FLV**
- Audio file types:
  - **MP3**
  - **WAV**
  - **FLAC**
  - **OGG**
  - **M4A**
  - **OPUS**
- Document file types:
  - **PDF**
  - ***TXT*** (Text files will contain the zip archive *but* when opening your text file, you will see a ton of excess from the extra data of the file)
- Executable file types:
  - **EXE**
  - **DLL**
  - **MSI**
  - **ELF**
  - **APK**
- Font format file types:
  - **TTF**
  - **OTF**
  - **WOFF**
  - **WOFF2**
