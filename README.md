# Auto-Convert PDFs to png files
This python tool, which is an application of [PyMuPDF](https://github.com/pymupdf/PyMuPDF) module, could auto convert PDFs to png files. It is easy to use, even you don't know programming at all.

# Usage
*Those Apps could execute independently. If you don't know programming and just want to convert PDFs to png files, pdf2png.exe may be suitable for you. Unfortunately, it always get false positive alert as virus by antivirus software. Adding this App to anti-virus software exclusion list or excluding this App can solve this problem.
*If you are considering about safety, pdf2png.py may be better for you. To use the App, make sure python and 'PyMuPDF' module be installed.
*Put the App and PDFs which you want to convert together, and excute the App. It will ask you how many times build-in DPI you want ([72 DPI](https://github.com/pymupdf/PyMuPDF/issues/181)). You can press Enter as default (4 times) or input any number. Then, it will scan all PDFs of file where the App is located and create new directories which named as PDFs name and save converted png files.

# Licence
This application comply with PyMuPDF's licening model which under open-source AGPL and commercial license agreement. Please read the full text of the AGPL license agreement (which is also included here in file LICENSE) to ensure that your use case complies with the guidelines of this license.

# Contact
Please use the Discussions menu for questions, comments, or asking for help, and submit issues here.