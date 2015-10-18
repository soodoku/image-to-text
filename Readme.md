### Image to Text

The script uses [Tesseract](https://github.com/tesseract-ocr) to get text from pdfs. It reads pdfs from a specified directory and outputs text files to another directory. Tesseract works well for documents with simple structure and fonts that are easily parsed but generally struggles with more complex layout. To fix errors in the recovered text, you may want to use [Edit Distance Based Search and Replace](https://github.com/soodoku/search-and-replace), exploiting the fact that errors in OCR tend of systematic. 

Rather than use Tesseract, you can also use [Abbyy FineReader](https://github.com/soodoku/abbyyR) or [Captricity](https://github.com/soodoku/captr). And to estimate the error rate of OCR, you may want to use [recognize](https://github.com/soodoku/recognize).

For a general overview of how to convert paper to digitial and how to optimize that process, see [A Quick Scan: From Paper to Digital] (http://gbytes.gsood.com/2014/05/28/a-quick-scan-from-paper-to-digital-data/)

#### Usage

`pdf2txt.py [options] pdf_directory`

#### Command Line Options:
```
  -h, --help            show this help message and exit
  -d DPI, --dpi=DPI     JPEG Resolution in DPI (default: 400)
  -j JPGDIR, --jpgdir=JPGDIR
                        JPEG output directory (default: jpg)
  -t TXTDIR, --textdir=TXTDIR
                        Text output directory (default: text)
  -r, --resume          Resume OCR to Text (default: False)
```            

#### Example:
`python pdf2txt.py pdf_dir`

The script will be post process all PDF files in `pdf_dir` directory and save the output text files to the `text` directory

### License
Scripts are released under the [MIT License](https://opensource.org/licenses/MIT).
