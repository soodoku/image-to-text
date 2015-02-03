Aim: Get text from 'non-searchable' pdf via tesseract

Usage: pdf2txt_r2.py [options] <pdf directory>

Options:
  -h, --help            show this help message and exit
  -d DPI, --dpi=DPI     JPEG Resolution in DPI (default: 400)
  -j JPGDIR, --jpgdir=JPGDIR
                        JPEG output directory (default: jpg)
  -t TXTDIR, --textdir=TXTDIR
                        Text output directory (default: text)
  -r, --resume          Resume OCR to Text (default: False)
                        
USAGE EXAMPLE :-
    python pdf2txt_r2.py pdf
   
    The script will be post process all PDF files in 'pdf' directory and save
    the output text files to the 'text' directory
