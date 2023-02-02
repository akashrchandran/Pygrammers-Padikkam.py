from compress import Compressor

print("Image Compressor")
print("PS: Supports only PNG, JPEG, JPG Images")
# Max quality 100 may upscale the file instead of compressing
# Optimize may give max compression without quality loss
# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#jpeg-saving
compressor = Compressor(quality=10, optimize=True)
file_path = input("Enter the file or folder path: ")
compressor.load_files(file_path)
compressor.compress()