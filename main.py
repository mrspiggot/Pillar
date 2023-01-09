from PyPDF2 import PdfReader


def run(name):
    print(f'Hi, {name}')
    reader = PdfReader("GeoBase_NHNC1_Data_Model_UML_EN.pdf")
    page = reader.pages[0]
    print(page.extract_text())
    for page in reader.pages:
        print(page.extract_text())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('Testing pdf-> text')


