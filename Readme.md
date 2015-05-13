## Image to Text

The script uses Tesseract to get text from pdfs. It reads pdfs from a specified directory and outputs text files to another directory. 

The text that is recovered can have lots of errors. To fix some of these errors, you may want to use this [Turbo Search And Replace](https://github.com/soodoku/search-and-replace). 

A more general overview of how to convert paper to digitial carrying more thoughts on optimizing the process can be read here: [A Quick Scan: From Paper to Digital] (http://gbytes.gsood.com/2014/05/28/a-quick-scan-from-paper-to-digital-data/)

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

