from app import api
from app.ressources import TextEditApi, TextListApi, SummaryListApi, DocumentListApi

api.add_resource(TextEditApi, '/text')
api.add_resource(TextListApi, '/text/<string:document_id>')
api.add_resource(SummaryListApi, '/summary/<string:document_id>')
api.add_resource(DocumentListApi, '/document')
