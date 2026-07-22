import sys
import subprocess
import importlib.util


def ensure_pypdf():
    if importlib.util.find_spec("pypdf") is None:
        print("pypdf is not installed. Installing...")
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "pypdf"]
            )
            print("pypdf installed successfully.\n")
        except subprocess.CalledProcessError:
            print("Failed to install pypdf.")
            sys.exit(1)


ensure_pypdf()

from pypdf import PdfWriter

merger = PdfWriter()

n = int(input("How many PDFs do you have? : "))

lst = []

for i in range(1, n + 1):
    pdf_name = input(f"\nEnter PDF #{i} name: ")
    lst.append(pdf_name)

    print("\nCurrent List:")
    for item in lst:
        print(item)

final = input("\nName the output PDF (e.g., merged.pdf): ")

for pdf in lst:
    merger.append(pdf)

merger.write(final)

print(f"\nPDFs merged successfully into '{final}'")
