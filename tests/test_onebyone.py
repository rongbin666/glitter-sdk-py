# rename to test_driver.py

# Copyright 2022-present glitter, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Test the Glitter driver module."""

import unittest
from glitter_sdk import GlitterClient


class GlitterClientUnitTest(unittest.TestCase):
    glitter_client: GlitterClient
    schema_name = "sample"

    @classmethod
    def setUpClass(cls):
        url = 'http://sg1.testnet.glitter.link:26659'
        cls.glitter_client = GlitterClient()

    def test_create_schema(self):
        # change the create schema with Addressbook {user_id, user_name, email_address}.
        # also the index is not specified for ipfs_cid field.
        fields = [
            {
                "name": "doi",
                "type": "string",
                "primary": "true",
                "index": {
                    "type": "keyword"
                }
            },
            {
                "name": "title",
                "type": "string",
                "index": {
                    "type": "text"
                }
            },
            {
                "name": "ipfs_cid",
                "type": "string",
                "index": {
                    "index": "false"
                }
            }
        ]
        res = self.glitter_client.db.create_schema(self.schema_name, fields)
        # do not print, please use assert especially for the tx field.
        # also try to create schema with different type of fields, not only string. 
        # (This would be optional if it takes too much time) 
        print(res)

    def test_get_schema(self):
        res = self.glitter_client.db.get_schema(self.schema_name)
        # Assert.
        print(res)

    def test_list_schema(self):
        res = self.glitter_client.db.list_schema()
        self.assertEqual(res['code'], 0)
        self.assertIsNotNone(res['data'].get('demo'))
        print(res)

    def test_put_doc(self):
        demo_doc = {
            "doi": "10.1002/(sci)1099-1697(199803/04)7:2<65::aid-jsc357>3.0.c",
            "title": "British Steel Corporation: probably the biggest turnaround story in UK industrial history",
            "ipfs_cid": "bafybeibxvp6bawmr4u24vuza2vyretip4n7sfvivg7hdbyolxrvbodwlte"
        }

        res = self.glitter_client.db.put_doc(self.schema_name, demo_doc)
        self.assertEqual(res['code'], 0)
        self.assertIsNotNone(res['tx'])
        print(res)

    def test_get_docs(self):
        primary_key = "10.1002/(sci)1099-1697(199803/04)7:2<65::aid-jsc357>3.0.c"
        res = self.glitter_client.db.get_docs(self.schema_name, [primary_key])
        print(res)
        # self.assertEqual(res["code"], 0)
        # self.assertGreaterEqual(res["data"]["Total"], 1)
        # self.assertEqual(res["data"]["hits"][primary_key]["doc_id"], primary_key)
        # print(res)

    def test_search(self):
        query_word = "British Steel Corporation"
        query_field = ["doi", "title"]
        res = self.glitter_client.db.search("xx", query_word, query_field)
        print(res)
        # self.assertEqual(res["code"], 0)
        # self.assertGreaterEqual(res["data"]["meta"]["page"]["size"], 1)

    def test_search_with_xxx(self):
        # let's cover everything you have dnoe for this complex search and assert them. If it times long, 
        # just delete the whole test.
        ''' First, put  documents:
            {
                "doi": "doi_1",
                "title": "British Steel Corporation: probably the biggest turnaround story in UK industrial history",
                "ipfs_cid": "bafybeibxvp6bawmr4u24vuza2vyretip4n7sfvivg7hdbyolxrvbodwlte",
                "publish_year": 1992
            }
            {
                "doi": "doi_2",
                "title": "British Steel Corporation: probably the biggest turnaround story in UK industrial history",
                "ipfs_cid": "bafybeibxvp6bawmr4u24vuza2vyretip4n7sfvivg7hdbyolxrvbodwlte",
                "publish_year": 2022
            }

        '''
        query_field = ["doi", "title"]

        # range query, 1990 <= publish_year <= 2000
        # range_conds = [{"type": "range", "field": "publish_year", "from": 1990, "to": 2000}]
        # res = self.glitter_client.db.search(self.schema_name, "British Steel Corporation",query_field, range_conds )

        term_conds = [{"type": "term", "field": "publish_year", "value": 1992}]
        res = self.glitter_client.db.search(self.schema_name, "British Steel Corporation",query_field, term_conds)
        print(res)
        # self.assertEqual(res["code"], 0)
        # self.assertGreaterEqual(res["data"]["meta"]["page"]["size"], 1)

    def test_app_status(self):
        res = self.glitter_client.db.app_status()
        self.assertEqual(res['code'], 0)
        print(res)

    def test_block(self):
        res = self.glitter_client.chain.block()
        print(res)

    def test_block(self):
        res = self.glitter_client.chain.block_search(query="block.height = 17835")
        print(res)

    def test_exception?(self):
        # res = self.glitter_client.db.search("sample", "Content Indexing Network")
        # print(res)
        for i in range(1, 100):
            try:
                res = self.glitter_client.db.get_schema(self.schema_name)
                print(res)
            except Exception as e:
                print(e)
                continue


if __name__ == '__main__':
    unittest.main()
