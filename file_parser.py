import sys
from pathlib import Path

JPEG_IMAGES = []
PNG_IMAGES = []
JPG_IMAGES = []
SVG_IMAGES = []

AVI_VIDEOS = []
MP4_VIDEOS = []
MOV_VIDEOS = []
MKV_VIDEOS = []

DOC_DOCS = []
DOCX_DOCS = []
TXT_DOCS = []
PDF_DOCS = []
XLSX_DOCS = []
PPTX_DOCS = []

MP3_AUDIOS = []
OGG_AUDIOS = []
WAV_AUDIOS = []
AMR_AUDIOS = []

ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []

MY_OTHER = []

REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,

    'AVI': AVI_VIDEOS,
    'MP4': MP4_VIDEOS,
    'MOV': MOV_VIDEOS,
    'MKV': MKV_VIDEOS,

    'DOC': DOC_DOCS,
    'DOCX': DOCX_DOCS,
    'TXT': TXT_DOCS,
    'PDF': PDF_DOCS,
    'XLSX': XLSX_DOCS,
    'PPTX': PPTX_DOCS,

    'MP3': MP3_AUDIOS,
    'OGG': OGG_AUDIOS,
    'WAV': WAV_AUDIOS,
    'AMR': AMR_AUDIOS,
 
    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES,
    'TAR': TAR_ARCHIVES,
}

FOLDERS = []
EXTENSION = set()
UNKNOWN = set()

def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()  # перетворюємо розширення файлу на назву папки jpg -> JPG

def scan(folder: Path) -> None:
    for item in folder.iterdir():
        # Якщо це папка то додаємо її до списку FOLDERS і переходимо до наступного елемента папки
        if item.is_dir():
            # перевіряємо, щоб папка не була тією в яку ми складаємо вже файли
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                # скануємо вкладену папку
                scan(item)  # рекурсія
            continue  # переходимо до наступного елементу в сканованій папці

        #  Робота з файлом
        ext = get_extension(item.name)  # беремо розширення файлу
        fullname = folder / item.name  # беремо шлях до файлу
        if not ext:  # якщо файл немає розширення то додаєм до невідомих
            MY_OTHER.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSION[ext]
                EXTENSION.add(ext)
                container.append(fullname)
            except KeyError:
                # Якщо ми не зареєстрували розширення у REGISTER_EXTENSION, то додаємо до невідомих
                UNKNOWN.add(ext)
                MY_OTHER.append(fullname)


if __name__ == "__main__":
    folder_to_scan = sys.argv[1]
    print(f'Start in folder {folder_to_scan}')
    scan(Path(folder_to_scan))
    print(f'JPEG images: {JPEG_IMAGES}')
    print(f'PNG images: {PNG_IMAGES}')
    print(f'JPG images: {JPG_IMAGES}')
    print(f'SVG images: {SVG_IMAGES}')

    print(f'AVI videos: {AVI_VIDEOS}')
    print(f'MP4 videos: {MP4_VIDEOS}')
    print(f'MOV videos: {MOV_VIDEOS}')
    print(f'MKV videos: {MKV_VIDEOS}')

    print(f'DOC documents: {DOC_DOCS}')
    print(f'DOCX documents: {DOCX_DOCS}')
    print(f'TXT documents: {TXT_DOCS}')
    print(f'PDF documents: {PDF_DOCS}')
    print(f'XLSX documents: {XLSX_DOCS}')
    print(f'PPTX documents: {PPTX_DOCS}')

    print(f'MP3 audios: {MP3_AUDIOS}')
    print(f'OGG audios: {OGG_AUDIOS}')
    print(f'WAV audios: {WAV_AUDIOS}')
    print(f'AMR audios: {AMR_AUDIOS}')

    print(f'ZIP archives: {ZIP_ARCHIVES}')
    print(f'GZ archives: {GZ_ARCHIVES}')
    print(f'TAR archives: {TAR_ARCHIVES}')

    print(f'Types of files in folder: {EXTENSION}')
    print(f'Unknown files of types: {UNKNOWN}')
    print(f'MY_OTHER: {MY_OTHER}')

    print(FOLDERS)