## Image to Text

Uses Tesseract to get text from pdfs. Reads pdfs from a specified directory and outputs text files to another directory. 

### Usage

<code>pdf2txt_r2.py [options] pdf_directory</code>

#### Options:
<pre><code>
  -h, --help            show this help message and exit
  -d DPI, --dpi=DPI     JPEG Resolution in DPI (default: 400)
  -j JPGDIR, --jpgdir=JPGDIR
                        JPEG output directory (default: jpg)
  -t TXTDIR, --textdir=TXTDIR
                        Text output directory (default: text)
  -r, --resume          Resume OCR to Text (default: False)
</code></pre>             

#### Example:
<code>python pdf2txt_r2.py pdf_dir </code>  

The script will be post process all PDF files in 'pdf_dir' directory and save the output text files to the 'text' directory

### License
Scripts are released under the [MIT License](https://github.com/soodoku/Lat-Long-to-Zip/blob/master/License%20for%20Scripts.md).

