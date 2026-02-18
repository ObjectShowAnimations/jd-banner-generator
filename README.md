# 🎵 Just Dance Banner Generator

A Python tool that automatically converts any image into a Just Dance–style banner background.

## The script:
 - Resizes images to 1024×512
 - Applies a blue/yellow duotone effect
 - Enhances contrast
 - Automatically names the output
 - Saves as PNG
 - Works with random image filenames
 - Batch processes all supported images in the folder

## 📦 Features
 - ✅ Automatic filename detection
 - ✅ Output format always .png
 - ✅ Output size always 1024x512
 - ✅ Crops to fit (no stretching)
 - ✅ Ignores already generated _banner_bkg.png files
 - ✅ Supports multiple image formats

## 🖼 Supported Input Formats
 - .png
 - .jpg
 - .jpeg
 - .webp
 - .bmp
 - .tga
 - .gif
 - .tiff

 ## 📐 Output Format
If your input file is:
```
youkissme.jpg
```

The output will be:
```
youkissme_banner_bkg.png
```

Saved in the same folder as the input image.

## 🛠 Requirements
Install Python 3.10+ (recommended).

Install Pillow:
```
pip install pillow
```

## 🚀 How to Use
1. Place the script in a folder.
2. Put your image files in the same folder.
3. Run the script:

```
python main.py
```
4. Generated banners will appear automatically.

## 🎨 Customization
Inside the script, you can modify:

```
TARGET_SIZE = (1024, 512)

SHADOW_COLOR = (0, 0, 255)        # Blue
HIGHLIGHT_COLOR = (248, 207, 0)   # Yellow
CONTRAST_BOOST = 1
```

You can:
 - Change the banner resolution
 - Adjust colors
 - Increase contrast
 - Add blur or tint effects

 ## 📂 Example Folder Structure
 ```
 jdbanner/
│
├── main.py
├── youkissme.jpg
├── danceparty.png
│
├── youkissme_banner_bkg.png
└── danceparty_banner_bkg.png
```

## 🧠 How It Works
 - Loads the image
 - Crops and resizes to 1024×512
 - Converts to grayscale
 - Applies a duotone color effect
 - Enhances contrast
 - Saves as PNG

## 🔥 Future Improvements (Optional Ideas)
 - Add Gaussian blur for authentic JD look
 - Add subtle red accent tint
 - Add vignette
 - GUI version
 - Drag-and-drop support
 - Folder recursion support

## ⚠ Disclaimer

This project is a fan-made utility inspired by the visual style of the Just Dance franchise. It is not affiliated with Ubisoft.
