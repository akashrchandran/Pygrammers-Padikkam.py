from PIL import Image
import os

class Compressor:
    def __init__(self, quality = 30, optimize = True) -> None:
        self.quality = quality
        self.optimize = optimize
        os.makedirs("compressed_images", exist_ok=True)

    def load_files(self, loc):
        if os.path.isfile(loc):
            if loc.endswith(('.png', '.jepg', '.jpg')):
                self.images = [loc]
        elif os.path.isdir(loc):
            self.images =  [
                os.path.join(loc, img)
                for img in os.listdir(loc)
                if img.endswith(('.png', '.jepg', '.jpg'))
            ]
        else:
            raise ValueError("Doesn't seem to be a file nor a directory!!")
        if not self.images:
            raise FileNotFoundError("Cannot find any of the files!!")
    
    def compress(self):
        print()
        for img in self.images:
            pic = Image.open(img)
            size = os.path.getsize(img)
            temp_name = f"compressed_{os.path.basename(img)}"
            pic.save(f"compressed_images/{temp_name}", optimize = self.optimize, quality=self.quality)
            temp_size = os.path.getsize(f"compressed_images/{temp_name}")
            print(f"{temp_name}✅", "[Saved:", '%.3f' % ((size - temp_size)/10**6), "MB]")
        print()
        print("Files saved at: ", os.path.abspath("compressed_images"))