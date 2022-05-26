from docxtpl import DocxTemplate
import excel as xl

def GenerateFileFromDefaultDocx(template:str, context:dict):
    try:
        open(template, "r")
    except:
        raise Exception("File does not exists")
    else:
        pass

    # Opens the DOCX Template and turns it into a object
    doc = DocxTemplate(template)

    # Make the changes and generate a new document
    doc.render(context)

    # saves the new document with the wishing name
    doc.save(f"{context['cliente_fullname'].replace(' ', '')}_litigation.docx")



# Configures the values which will be changed in the Template --> Observation: the keys of the Dictionary
# MUST be the same found the Template document between double brackets I.E.: {{company_name}}
def GenerateContext(pDict:dict):
    splitname = pDict["CLIENTE"].split(" ")
    social_name = [splitname[0], splitname[-1]]
    socialname = " ".join(social_name).title()

    Context =  {
        'process_number': pDict["# PROCESSO"],
        'cliente_socialname': socialname,
        'cliente_fullname': pDict["CLIENTE"].title(),
        'lawyer_fullname': pDict["ADVOGADO ENCARREGADO"].title(),
        "expected_value": float(pDict["VALOR ESPERADO"]),
        "wishing_value": float(pDict["VALOR PEDIDO"]),
        "lawyer_cost": float(pDict["RETORNO DO ADVOGADO"])
        }
    return Context

if __name__ == "__main__":

    processes = xl.getAllProcesses("litigation_template.xlsx")
    for process in processes:
        ctxt = GenerateContext(process)
        GenerateFileFromDefaultDocx("litigation_template.docx", ctxt)
