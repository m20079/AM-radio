from os import path
from glob import glob
from asyncio import gather, create_subprocess_shell, subprocess


async def crop_pdf_folder(input_folder: str):
    if not path.exists(input_folder):
        print(f"{input_folder} does not exist")
        return
    files = glob(input_folder + "/*.pdf")
    await gather(*[crop_pdf_file(file) for file in files])


async def crop_pdf_file(input_file: str):
    if not path.exists(input_file):
        print(f"{input_file} does not exist")
        return
    print("Cropping " + input_file)
    process = await create_subprocess_shell(
        cmd=f"pdfcrop '{input_file}' '{input_file}'",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    await process.wait()
