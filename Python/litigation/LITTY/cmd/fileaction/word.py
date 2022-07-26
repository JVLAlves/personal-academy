from docxtpl import DocxTemplate
import LITTY.cmd.fileaction.excel as xl
import LITTY.glob.globals as glob

def GenerateFileFromDefaultDocx(context:dict, template:xl.File, path:str, file_header:str=None):
    # Opens the DOCX Template and turns it into an object
    doc = DocxTemplate(template.path) # Always needs to be a Path

    # Make the changes and generate a new document
    doc.render(context)

    # saves the new document with the wishing name
    #TODO: Custom place of saving -- custom header
    if file_header is not None:
        doc.save(f"{path + '/' + template.filename}({file_header})_{glob.FILE_WATERMARK}{glob.FILE_EXTENSION}")
    else:
        doc.save(f"{path + '/' + template.filename}{glob.FILE_WATERMARK}{glob.FILE_EXTENSION}")

