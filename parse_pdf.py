import sys
try:
    import PyPDF2
    with open(sys.argv[1], 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            print(page.extract_text())
except Exception as e:
    try:
        from pdfminer.high_level import extract_text
        print(extract_text(sys.argv[1]))
    except Exception as e2:
        print("Both PyPDF2 and pdfminer failed.")
        import subprocess
        subprocess.run(["pdftotext", sys.argv[1], "-"])
