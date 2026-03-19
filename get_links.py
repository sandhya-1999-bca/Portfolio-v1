import PyPDF2
with open("public/resume.pdf", "rb") as f:
    reader = PyPDF2.PdfReader(f)
    for page in reader.pages:
        if "/Annots" in page:
            for annot_ref in page["/Annots"]:
                annot = annot_ref.get_object()
                if annot.get("/Subtype") == "/Link":
                    action = annot.get("/A")
                    if action and "/URI" in action:
                        print(action["/URI"])
