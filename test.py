# -*- coding: utf-8 -*-
import pytest
import requests
import json
from app.models import Document
from app import db


class TestClass(object):
    def setup_class(self):
        self.base_url = 'http://127.0.0.1:5000'
        self.headers = {'content-type': 'application/json'}
        self.doc_to_delete = []

        # we create a test document
        doc = Document(text="Look! I'm even testing my code, you should really hire me... ;)")
        db.session.add(doc)
        db.session.commit()
        document = doc.to_dict()

        self.doc_to_delete.append(document['document_id'])
        self.doc_id = document['document_id']

    def teardown_class(self):
        # we delete the useless documents
        for doc_id in self.doc_to_delete:
            doc = db.session.query(Document).get(doc_id)
            db.session.delete(doc)
        db.session.commit()

    def test_get_text(self):
        url = '{}/text/{}'.format(self.base_url, self.doc_id)
        resp = requests.get(url)
        data = resp.json()

        assert len(data.keys()) == 2
        assert isinstance(data['document_id'], int)
        assert isinstance(data['text'], str)

    def test_post_text(self):
        url = '{}/text'.format(self.base_url)
        data = {'text': 'This+is+a+long+text'}

        resp = requests.post(url, data=json.dumps(data), headers=self.headers)
        document_dict = json.loads(resp.text)

        assert len(document_dict.keys()) == 1
        assert isinstance(document_dict['document_id'], int) is True
        assert resp.status_code == 201

        self.doc_to_delete.append(document_dict['document_id'])

    def test_get_summary(self):
        url = '{}/summary/{}'.format(self.base_url, self.doc_id)
        resp = requests.get(url)
        data = resp.json()

        assert len(data.keys()) == 2
        assert isinstance(data['document_id'], int)
        assert data['summary'] == 'This is a summary'  # default value