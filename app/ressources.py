from flask_restful import reqparse, abort, Resource
from app.models import Document

from app import db, app

parser = reqparse.RequestParser()
parser.add_argument('text')
parser.add_argument('document_id', type=int)


class TextEditApi(Resource):
    """Create a new document, store the text sent in parameter, return the document_id created"""
    def post(self):
        args = parser.parse_args()
        try:
            text_arg = args['text']
            doc = Document(text=text_arg)
            db.session.add(doc)
            db.session.commit()
            text = doc.to_dict()
            app.logger.info('Text added in db: {}'.format(text_arg))
            code = 201
        except Exception as e:
            text = {}
            app.logger.error('Text not added in db: {}'.format(text_arg))
            code = 500
        return {'document_id': text['document_id']}, code


class SummaryListApi(Resource):
    """Return the document summary and its id"""
    def get(self, document_id):
        try:
            document = Document.query.get(document_id).to_dict()
            document.pop('text', None)
            app.logger.info('List summary for document_id={}'.format(document_id))
            code = 200
        except AttributeError as e:
            document = {}
            app.logger.warning('Document not found document_id={}'.format(document_id))
            code = 404
        except Exception as e:
            document = {}
            app.logger.error('Error while trying to get summary document_id={}'.format(document_id))
            code = 500
        return document, code


class DocumentListApi(Resource):
    """Not asked, for debugging purposes only, returns all the documents created in db"""
    def get(self):
        try:
            documents = Document.query.all()
            document_list = [d.to_dict() for d in documents]
            app.logger.info('List documents')
            code = 200
        except Exception as e:
            document_list = []
            app.logger.error('Error while trying to list documents: {}'.format(e))
            code = 500
        return document_list, code


class TextListApi(Resource):
    def get(self, document_id):
        """Return the text of the document identified with the document_id sent in parameter."""
        try:
            document = Document.query.get(document_id).to_dict()
            document.pop('summary', None)
            app.logger.info('List text for document_id={}'.format(document_id))
            code = 200
        except AttributeError as e:
            document = {}
            app.logger.warning('Document not found document_id={}'.format(document_id))
            code = 404
        except Exception as e:
            document = {}
            app.logger.error('Error while trying to get text: {}'.format(e))
            code = 500
        return document, code
