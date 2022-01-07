# Mangafreak Downloader

- Enables automatic download of manga chapters from mangafreak

## Guide
- `pip install -r requirements.txt`
- Edit data.json
    - The key is the name of the resulting cbz file (e.g. "Dragon Ball.cbz")
    - part of url slug from mangafreak, e.g. for https://w12.mangafreak.net/Manga/My_Hero_Academia, it's `My_Hero_Academia`
    - `last_chapter` is the last chapter you've downloaded,
        0 means it's completely new, start downloading until latest chapter available
        10 means start downloading from chapter 11 onwards to latest chapter available
- Run `python3 mangafreak-dl.py`
- After it's done it will automatically update the last_chapter in data.json