
import glob, getpass
from PIL import Image

VERBOSE = False
JPG_QUALITY = 90

if __name__ == "__main__":

    appdata_path = glob.os.getenv('APPDATA') # AppData Roaming dir
    library_path = glob.os.path.join(appdata_path, r'Playnite\library\files')
    
    if glob.os.path.exists(library_path):
        # Get all JPG files inside Playnite's library path
        # PNG files are usually used on smaller images, so are ignored
        image_files = glob.glob(glob.os.path.join(library_path, '**', '*.jpg'), recursive=True)
        image_files.extend(glob.glob(glob.os.path.join(library_path, '**', '*.png'), recursive=True))
        for file in image_files:
            if VERBOSE: print("PROCESSING: {0}".format(file))
            if glob.os.path.getsize(file) == 0:
                if VERBOSE: print("ERROR: File size is 0: {0}".format(file))
                continue
            try:
                with Image.open(file) as im:
                    if im.format == "JPEG":
                        im.save(file, "JPEG", quality=JPG_QUALITY)
                    elif im.format == "PNG":
                        new_filename = glob.os.path.splitext(file)[0] + '.jpg'
                        im.save(new_filename, "JPEG", quality=JPG_QUALITY)
                        glob.os.remove(file)
                    else:
                        if VERBOSE: print("ERROR: Invalid image format {0} for file: {1}".format(im.format, file))
            except OSError:
                print("Cannot process: {0}".format(file))
    else:
        print("ERROR: Path {0} doesn't exist. Either the Playnite is not installed or \
               the user running this script isn't the one that installed Playnite".format(library_path))

