from docling.document_converter import DocumentConverter

from utils.sitemap import get_sitemap_urls
from utils.linksFromDiv import get_urls_within_el

converter = DocumentConverter()

# --------------------------------------------------------------
# Basic PDF extraction
# --------------------------------------------------------------

# result = converter.convert("https://arxiv.org/pdf/2408.09869")

# document = result.document
# markdown_output = document.export_to_markdown()
# json_output = document.export_to_dict()

# print(markdown_output)

# --------------------------------------------------------------
# Basic HTML extraction
# --------------------------------------------------------------

# result = converter.convert("https://www.kulturlotse.de/themen/kinder/")

# document = result.document
# markdown_output = document.export_to_markdown()
# print(markdown_output)


# --------------------------------------------------------------
# Scrape multiple pages using links within a div
# --------------------------------------------------------------

def extract_docs_from_url(url: str, selector:str) -> list:
    urls = get_urls_within_el(url, selector)           

    conv_results_iter = converter.convert_all(urls)

    docs = []
    for result in conv_results_iter:
        if result.document:
            document = result.document
            docs.append(document)
    
    return docs

# --------------------------------------------------------------
# Scrape multiple pages using the sitemap
# --------------------------------------------------------------

# sitemap_urls = get_sitemap_urls("https://ds4sd.github.io/docling/")
# one_url = "https://www.kulturlotse.de/themen/kinder/"
# conv_results_iter = converter.convert(one_url)

# docs = []
# for result in conv_results_iter:
#     if result.document:
#         document = result.document
#         docs.append(document)