import os

downloadsFolder = "/Users/Usuario/Downloads/"

imageFolder = "/Users/Usuario/Documents/Organizer/Images/"
AudioFolder = "/Users/Usuario/Documents/Organizer/Audios/"
VideoFolder = "/Users/Usuario/Documents/Organizer/Videos/"
pdfFolder = "/Users/Usuario/Documents/Organizer/PDF/"
xlsFolder = "/Users/Usuario/Documents/Organizer/Files/"


if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            os.rename(downloadsFolder + filename, imageFolder + filename)

        if extension in [".mp4"]:
            os.rename(downloadsFolder + filename, VideoFolder + filename)

        if extension in [".mp3"]:
            os.rename(downloadsFolder + filename, AudioFolder + filename)

        if extension in [".xls",".xlsx",".csv"]:
            os.rename(downloadsFolder + filename, xlsFolder + filename)

        if extension in [".pdf"]:
            os.rename(downloadsFolder + filename, pdfFolder + filename)


