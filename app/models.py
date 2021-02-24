from app import db


class Document(db.Model):
    __tablename__ = 'document'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    summary = db.Column(db.Text, default='This is a summary')

    def to_dict(self):
        document_dict = {
            'document_id': self.id,
            'text': self.text,
            'summary': self.summary
        }
        return document_dict

    def __repr__(self):
        return '<Document {} {} {}>'.format(self.id, self.summary, self.text)
