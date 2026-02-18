from PIL import Image, ImageEnhance, ImageOps
import os

# -----------------------------
# SETTINGS
# -----------------------------
TARGET_SIZE = (1024, 512)

SHADOW_COLOR = (0, 0, 255)        # Blue
HIGHLIGHT_COLOR = (248, 207, 0)   # Yellow
CONTRAST_BOOST = 1

SUPPORTED_EXTENSIONS = (
    ".png", ".jpg", ".jpeg", ".webp",
    ".bmp", ".tga", ".gif", ".tiff"
)

# -----------------------------
# GENERATOR
# -----------------------------
def generate_banner_for_image(input_path):

    filename_no_ext = os.path.splitext(os.path.basename(input_path))[0]

    # Skip already generated banners
    if filename_no_ext.endswith("_banner_bkg"):
        return

    output_name = f"{filename_no_ext}_banner_bkg.png"
    output_path = os.path.join(os.path.dirname(input_path), output_name)

    print(f"Processing: {input_path}")

    img = Image.open(input_path).convert("RGB")

    # Resize to 1024x512 (crop-to-fit)
    img = ImageOps.fit(img, TARGET_SIZE, Image.LANCZOS)

    # Duotone
    gray = ImageOps.grayscale(img)
    duotone = ImageOps.colorize(gray, black=SHADOW_COLOR, white=HIGHLIGHT_COLOR)

    # Contrast
    final_img = ImageEnhance.Contrast(duotone).enhance(CONTRAST_BOOST)

    final_img.save(output_path, format="PNG")

    print(f" → Generated: {output_name}\n")


# -----------------------------
# RUN (Auto Folder Mode)
# -----------------------------
def main():
    current_folder = os.path.dirname(os.path.abspath(__file__))

    for file in os.listdir(current_folder):
        if file.lower().endswith(SUPPORTED_EXTENSIONS):
            full_path = os.path.join(current_folder, file)
            generate_banner_for_image(full_path)

    print("Done!")

main()
input("Press Enter to exit...")
