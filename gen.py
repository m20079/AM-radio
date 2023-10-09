import os
import glob
import subprocess
import xml.etree.ElementTree as ET
import pypdf
from concurrent.futures import ProcessPoolExecutor


def drawio_to_pdf(input_file: str, output_folder: str):
    if not os.path.exists(input_file):
        print("Input file does not exist")
        return
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    basename = os.path.splitext(os.path.basename(input_file))[0]
    print(f"Converting {input_file} to {output_folder}{basename}.pdf")
    subprocess.run(
        args=[f"draw.io.exe -xrf pdf -o {output_folder} {input_file}"],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    print(f"Cropping {output_folder}{basename}.pdf")
    subprocess.run(
        args=[f"pdfcrop {output_folder}/{basename}.pdf {output_folder}/{basename}.pdf"],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    print(f"Splitting {output_folder}{basename}.pdf")
    tree = ET.parse(input_file)
    root = tree.getroot()
    name = [diagram.attrib["name"] for diagram in root.iter("diagram")]
    reader = pypdf.PdfReader(f"{output_folder}/{basename}.pdf")
    for i in range(len(reader.pages)):
        pdf = reader.pages[i]
        writer = pypdf.PdfWriter()
        writer.add_page(pdf)
        with open(f"{output_folder}/{name[i]}.pdf", "wb") as fp:
            writer.write(fp)
    os.remove(f"{output_folder}/{basename}.pdf")


def crop_process(file: str):
    print("Cropping " + file)
    subprocess.run(
        args=["pdfcrop " + file + " " + file],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def crop_pdf(folder: str):
    if not os.path.exists(folder):
        print("Folder does not exist")
        return
    files = glob.glob(folder + "/*.pdf")
    with ProcessPoolExecutor() as executor:
        executor.map(crop_process, files)


drawio_to_pdf("fig/fig.drawio", "fig")
