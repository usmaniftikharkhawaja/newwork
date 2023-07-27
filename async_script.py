import time
import asyncio
import requests


async def function1():
    print("func 1")
    URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    response = requests.get(URL)
    open("instagram.ico", "wb").write(response.content)

    return "Harry"


async def function2():
    print("func 2")
    URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
    response = requests.get(URL)
    open("instagram2.jpg", "wb").write(response.content)


async def function3():
    print("func 3")
    URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
    response = requests.get(URL)
    open("instagram3.ico", "wb").write(response.content)


async def main():
    # await function1()
    # await function2()
    # await function3()
    # return 3
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)
    # task = asyncio.create_task(function1())
    # # await function1()
    # await function2()
    # await function3()


# Use the traditional way to set up and run the event loop
if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:  # If the event loop is already running
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
