from docxtpl import DocxTemplate

# Opens the DOCX Template and turns it into a object
doc = DocxTemplate('litigation_template.docx')

# Configures the values which will be changed in the Template --> Observation: the keys of the Dictionary
# MUST be the same found the Template document between double brackets I.E.: {{company_name}}
context = {'process_number':15, 'cliente_name': "Gislane Dolores Mendes Cunha", "lawyer_name":"Amiel Dias de Luiz", "company_name":"DELUIZ ltda."}

# Make the changes and generate a new document
doc.render(context)

#saves the new document with the wishing name
doc.save("automatic_generated_litigation.docx")