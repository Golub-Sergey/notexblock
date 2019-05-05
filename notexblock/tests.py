"""
Test outsettingsvalues view.
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.test import Client, RequestFactory, TestCase
from mock import Mock
from notexblock import NoteXBlock
from xblock.fields import ScopeIds
from xblock.runtime import DictKeyValueStore, KvsFieldData
from xblock.test.tools import TestRuntime as Runtime


class TestNoteXblock(TestCase):
    """
    Testing of NotexBlock.
    """

    def setUp(self):
        """
        Create mane instances for all test.
        """
        self.client = Client()
        self.data = {'notes': 'test'}
        self.json_data = json.dumps(self.data)

    def test_student_view(self):
        """
        Test of works url.
        """
        self.client.get('/')
        self.client.get('/scenario/notexblock.0/')
        self.assertEquals(self.client.get('/').status_code, 200)
        request = self.client.get('/scenario/notexblock.0/')
        self.assertEquals(request.status_code, 200)

    def test_add_note_url(self):
        """
        Test current xblock url with parametrs.
        """
        request = RequestFactory().post('scenario/notexblock.0/', self.data)
        self.assertEquals(request.POST['notes'], self.data['notes'])

    def test_add_note_method(self):
        """
        Test xblock method with params.
        """
        scope_ids = Mock(spec=ScopeIds(user_id='student_1', block_type='notexblock',
                                       def_id='notexblock.notexblock.d0', usage_id='notexblock.notexblock.d0.u0'))
        key_store = DictKeyValueStore()
        field_data = KvsFieldData(key_store)
        runtime = Runtime(services={'field-data': field_data})
        block = NoteXBlock(runtime, scope_ids=scope_ids)

        request = RequestFactory().post('scenario/notexblock.0/', json.dumps(self.data), 'application/json')
        result = block.add_note(request)

        self.assertEquals(result.status_code, 200)
