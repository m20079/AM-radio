from os import path, makedirs, remove
from asyncio import create_subprocess_shell, subprocess
from xml.etree.ElementTree import parse
from pypdf import PdfReader, PdfWriter
from .crop_pdf import crop_pdf_file
from platform import system


async def convert_to_pdf(input_file: str, output_folder: str):
    if not path.exists(input_file):
        print("Input file does not exist")
        return
    if not path.exists(output_folder):
        makedirs(output_folder)
    basename = path.splitext(path.basename(input_file))[0]
    print(f"Converting {input_file} to {output_folder}{basename}.pdf")
    process = await create_subprocess_shell(
        cmd=f"{'draw.io' if system() == 'Darwin' else 'draw.io.exe'} -xrf pdf -o {output_folder} {input_file}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    await process.wait()


def get_diagram_name(input_file: str):
    tree = parse(input_file)
    root = tree.getroot()
    return [diagram.attrib["name"] for diagram in root.iter("diagram")]


def split_pdf_file(input_file: str, output_folder: str, name: list[str]):
    print(f"Splitting {input_file}")
    reader = PdfReader(input_file)
    for i in range(len(reader.pages)):
        pdf = reader.pages[i]
        writer = PdfWriter()
        writer.add_page(pdf)
        with open(f"{output_folder}/{name[i]}.pdf", "wb") as fp:
            writer.write(fp)


async def make_diagram(input_file: str, output_folder: str):
    await convert_to_pdf(input_file, output_folder)
    basename = path.splitext(path.basename(input_file))[0]
    await crop_pdf_file(input_file=f"{output_folder}/{basename}.pdf")
    name = get_diagram_name(input_file)
    split_pdf_file(f"{output_folder}/{basename}.pdf", output_folder, name)
    remove(f"{output_folder}/{basename}.pdf")
