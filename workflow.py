import os
from extract import extract_docs_from_url


docs = extract_docs_from_url("https://www.kulturlotse.de/themen/kinder/", ".foundEvents")

output_dir: str = './output_mds'
os.makedirs(output_dir, exist_ok=True)

for idx, doc in enumerate(docs):
    file_name: str = f'{output_dir}/{idx}.md'
    with open(file_name, 'w', encoding="utf-8") as file: 
        print(file_name)
        file.write(doc.export_to_markdown())