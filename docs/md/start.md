---
layout: nodes.liquid
section: developer
date: Last Modified
title: "Getting Started"
permalink: "docs/getting_started/"
excerpt: "Smart Contracts and Chainlink"
metadata:
title: "Getting Started"
description: "Learn the basic concepts about what smart contracts are and, how to write them, and how Chainlink oracles work with smart contracts."
---

# Quickstart / Installation

This tutorial walks you through how to set up [glitter-sdk-py](https://github.com/blockved/glitter-sdk-py) for local development.

## Installing the Driver

Now you can install the Glitter Python Driver [glitter-sdk-py](https://github.com/blockved/glitter-sdk-py) using:

``` sh
    pip install glitter-sdk-py
    OR
    pip3 install glitter-sdk-py
```


## Installation Guide for Developers

1. Fork the [glitter-sdk-py](https://github.com/blockved/glitter-sdk-py) repo on GitHub.
2. Clone your fork locally and enter into the project::
``` sh
    git clone git@github.com:your_name_here/glitter-sdk-py.git
    cd glitter-sdk-py/
```
3. Create a branch for local development::
``` sh
    git checkout -b name-of-your-bugfix-or-feature
```
Now you can make your changes locally.

4. Commit your changes and push your branch to GitHub::
``` sh
    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature
```

# Basic Usage Examples

For the examples on this page,
we assume you're using a Python 3 version of IPython (or similar),
you've :doc:`quickstart <quickstart>`,
of the node or cluster you want to connect to.


## Getting Started

We begin by creating an object of class GlitterClient:

``` python
    from glitter_driver import GlitterClient
    url = 'http://127.0.0.1:26659'  # Use YOUR Glitter Root URL here
```
If the Glitter node or cluster doesn't require authentication tokens, you can do:

```python
    glitter_client = GlitterClient(url)
```

If it *does* require authentication tokens, you can do put them in a dict like so:

```python
    tokens = {'access_token': 'my_token'}
    glitter_client = GlitterClient(url, headers=tokens)
```


## List All Schema

``` python

    res = glitter_client.db.list_schema()
    print(res)
       {
          "code": 200,
          "message": "ok",
          "data": {
            "lib_gen": "{\"mappings\":{\"_source\":{\"includes\":[],\"excludes\":[]},\"properties\":{\"author\":{\"type\":\"text\",\"analyzer\":\"ik_max_word\",\"search_analyzer\":\"ik_max_word\"},\"issn\":{\"type\":\"keyword\"},\"language\":{\"type\":\"keyword\"},\"publisher\":{\"type\":\"text\"},\"series\":{\"type\":\"text\"},\"md5\":{\"type\":\"keyword\"},\"title\":{\"type\":\"text\",\"analyzer\":\"ik_max_word\",\"search_analyzer\":\"ik_max_word\"},\"tags\":{\"type\":\"keyword\"},\"ipfs_cid\":{\"type\":\"keyword\",\"index\":false}}}}",
            "magnet": "{\"mappings\":{\"_source\":{\"includes\":[],\"excludes\":[]},\"properties\":{\"doc_id\":{\"type\":\"keyword\"},\"status\":{\"type\":\"short\",\"index\":\"false\"},\"data_create_time\":{\"type\":\"long\",\"index\":\"false\"},\"update_time\":{\"type\":\"long\",\"index\":\"false\"},\"file_name\":{\"type\":\"text\",\"analyzer\":\"ik_max_word\",\"search_analyzer\":\"ik_max_word\"},\"creator\":{\"type\":\"keyword\"},\"category\":{\"type\":\"keyword\"},\"extension\":{\"type\":\"keyword\"},\"file_size\":{\"type\":\"long\",\"index\":\"false\"},\"current_count\":{\"type\":\"long\",\"index\":\"false\"},\"total_count\":{\"type\":\"long\",\"index\":\"false\"},\"cid\":{\"type\":\"keyword\"},\"pin_status\":{\"type\":\"text\",\"index\":\"false\"}}}}",
            "sci": "{\"mappings\":{\"_source\":{\"includes\":[],\"excludes\":[]},\"properties\":{\"author\":{\"type\":\"text\",\"analyzer\":\"ik_max_word\",\"search_analyzer\":\"ik_max_word\"},\"md5\":{\"type\":\"keyword\"},\"doi\":{\"type\":\"keyword\"},\"title\":{\"type\":\"text\",\"analyzer\":\"ik_max_word\",\"search_analyzer\":\"ik_max_word\"},\"ipfs_cid\":{\"type\":\"keyword\",\"index\":false},\"file_name\":{\"type\":\"keyword\",\"index\":false}}}}"
          }
        }
```

## Put Document to Glitter
define a document and put it to glitter
For example:

```python
 libgen_doc = {
    "title": "Mechanical Modelling and Computational Issues in Civil Engineering",
    "series": ["Lecture Notes in Applied and Computational Mechanics 23"],
    "author": ["Michel Fremond (editor)", " Franco Maceri (editor)"],
    "publisher": "Springer",
    "language": ["English"],
    "md5": "2fac9c0079cea4f63862d8c30e6e8b29",
    "tags":["Vibration, Dynamical Systems, Control","Civil Engineering","Mechanics","Numerical Analysis"],
    "issn": "1613-7736",
    "ipfs_cid": "bafykbzacedq5bhvqpbuyd4lkop7fpv7wutjzjvzzdkprfgkecbyucrb4sz6io",
    "extension": "pdf"
}
 res = glitter_client.db.put_doc("sci",  libgen_doc)
 print(res)
 {
    'code': 200,
    'message': 'ok',
    'tx_hash': 'DC6128F7801993319C91EFACA2A19F0AA73AF3769D0711DA876D10E6E0EF8979',
    'data': ''
}
```


## Check Whether the Document Exists
Query by document id.

``` python
    doc_ids = ["2fac9c0079cea4f63862d8c30e6e8b29"]
    res = glitter_client.db.get_docs("libgen", doc_ids)
    print(res)
    {
       'code': 200,
       'message': 'ok',
       'data': {
           'Total': 1,
            Hits': {'my_token_2fac9c0079cea4f63862d8c30e6e8b29': {
               'doc_id': '2fac9c0079cea4f63862d8c30e6e8b29', 'title': 'Mechanical Modelling and Computational Issues in Civil Engineering', 'series': [''], 'author': ['Michel Fremond (editor)'], 'publisher': 'Springer', 'language': ['English'], 'tags': ['Vibration, Dynamical Systems, Control','Civil Engineering','Mechanics','Numerical Analysis'], 'ipfs_cid': 'bafykbzacedq5bhvqpbuyd4lkop7fpv7wutjzjvzzdkprfgkecbyucrb4sz6io', 'extension': 'pdf'}
               }
            }
    }
```


## Simple Search without Filter Condition
Search document by publisher

```python
    res = glitter_client.db.simple_search("libgen", "Springer")
    print(res)
    {
        "code": 200,
        "message": "ok",
        "data": {
            "search_time": 4,
            "index": "libgen",
            "meta": {
                "page": {
                    "current_page": 1,
                    "total_pages": 6,
                    "total_results": 5,
                    "size": 1,
                    "sorted_by": ""
                }
            },
            "items": [{
                "highlight": {
                    "publisher": ["<span>Springer</span>"]
                },
                "data": {
                    "doc_id": "1753c32af92fa2f8de5a62fbc3805d95",
                    "title": "Mechanical Modelling and Computational Issues in Civil Engineering",
                    "series": [""],
                    "author": ["Michel Fremond (editor)"],
                    "publisher": "Springer",
                    "language": ["Latin", "English"],
                    "md5": "1753c32af92fa2f8de5a62fbc3805d95",
                    "tags": ["Vibration, Dynamical Systems, Control", "Civil Engineering", "Mechanics",
                             "Numerical Analysis"
                             ],
                    "ipfs_cid": "bafykbzacedq5bhvqpbuyd4lkop7fpv7wutjzjvzzdkprfgkecbyucrb4sz6io",
                    "extension": "pdf"
                }
            }],
            "sorted_by_field": [{
                "field": "extension",
                "type": "term"
            }, {
                "field": "author",
                "type": "term"
            }],
            "facet": {
                "issn": [],
                "language": [{
                    "type": "term",
                    "field": "language",
                    "value": "English",
                    "from": 0,
                    "to": 0,
                    "doc_count": 4
                },
                    {
                        "type": "term",
                        "field": "language",
                        "value": "Latin",
                        "from": 0,
                        "to": 0,
                        "doc_count": 1
                    }
                ],
                "tags": [{
                    "type": "term",
                    "field": "tags",
                    "value": "",
                    "from": 0,
                    "to": 0,
                    "doc_count": 3
                },
                    {
                        "type": "term",
                        "field": "tags",
                        "value": "Mechanics",
                        "from": 0,
                        "to": 0,
                        "doc_count": 2
                    }
                ]
            }
        }
    }
```

## Complex Search with Filter Condition

```python
    filter_cond = [{"type": "term", "field": "language", "value": "English", "from": 0.9, "to": 1, "doc_count": 100}]
    res = glitter_client.db.complex_search("libgen", "Springer", filter_cond)
    print(res)
    {
        "code": 200,
        "message": "ok",
        "data": {
            "search_time": 10,
            "index": "libgen",
            "meta": {
                "page": {
                    "current_page": 1,
                    "total_pages": 1,
                    "total_results": 5,
                    "size": 10,
                    "sorted_by": ""
                }
            },
            "items": [{
                "highlight": {
                    "publisher": ["<span>Springer</span>"]
                },
                "data": {
                    "doc_id": "1753c32af92fa2f8de5a62fbc3805d95",
                    "title": "Mechanical Modelling and Computational Issues in Civil Engineering",
                    "series": [""],
                    "author": ["Michel Fremond (editor)"],
                    "publisher": "Springer",
                    "language": ["Latin", "English"],
                    "md5": "1753c32af92fa2f8de5a62fbc3805d95",
                    "tags": ["Vibration, Dynamical Systems, Control", "Civil Engineering", "Mechanics",
                             "Numerical Analysis"
                             ],
                    "ipfs_cid": "bafykbzacedq5bhvqpbuyd4lkop7fpv7wutjzjvzzdkprfgkecbyucrb4sz6io",
                    "extension": "pdf"
                }
            }],
            "sorted_by_field": [{
                "field": "extension",
                "type": "term"
            }, {
                "field": "author",
                "type": "term"
            }],
            "facet": {
                "issn": [],
                "language": [{
                    "type": "term",
                    "field": "language",
                    "value": "English",
                    "from": 0,
                    "to": 0,
                    "doc_count": 4
                },
                    {
                        "type": "term",
                        "field": "language",
                        "value": "Latin",
                        "from": 0,
                        "to": 0,
                        "doc_count": 1
                    }
                ],
                "tags": [{
                    "type": "term",
                    "field": "tags",
                    "value": "",
                    "from": 0,
                    "to": 0,
                    "doc_count": 3
                },
                    {
                        "type": "term",
                        "field": "tags",
                        "value": "Mechanics",
                        "from": 0,
                        "to": 0,
                        "doc_count": 2
                    }
                ]
            }
        }
    }
```

## Search Transaction
You can search transaction by transaction height, transaction hash, or token.

``` python
    #res = glitter_client.chain.tx_search(query="update_doc.token='my_token'")
    #res = glitter_client.chain.tx_search(query="tx.hash='ACB6696C22B601D544FE05C8899090B4C1E98EF87636AA07EBCD63548786B561'")
    res = glitter_client.chain.tx_search(query="tx.height=460844")
    print(res)
    {
     "jsonrpc": "2.0",
     "id": -1,
     "result": {
       "txs": [
         {
           "hash": "ACB6696C22B601D544FE05C8899090B4C1E98EF87636AA07EBCD63548786B561",
           "height": "460844",
           "index": 0,
           "tx_result": {
             "code": 0,
             "data": null,
             "log": "",
             "info": "",
             "gas_wanted": "0",
             "gas_used": "0",
             "events": [
               {
                 "type": "update_doc",
                 "attributes": [
                   {
                     "key": "dG9rZW4=",
                     "value": "bXlfdG9rZW4=",
                     "index": true
                   }
                 ]
               }
             ],
             "codespace": ""
           },
           "tx": "CghteV90b2tlbhrRBxIGbGliZ2VuGiA1MTczMjc1ZjAyOWE3ZjBiNzhiZGNhY2EzNGE2ZGFjYyKkB3sidGl0bGUiOiAiXHUwNDFjXHUwNDM1XHUwNDM2XHUwNDM0XHUwNDQzXHUwNDNkXHUwNDMwXHUwNDQwXHUwNDNlXHUwNDM0XHUwNDNkXHUwNDMwXHUwNDRmIFx1MDQzMFx1MDQzZFx1MDQzMFx1MDQ0Mlx1MDQzZVx1MDQzY1x1MDQzOFx1MDQ0N1x1MDQzNVx1MDQ0MVx1MDQzYVx1MDQzMFx1MDQ0ZiBcdTA0M2RcdTA0M2VcdTA0M2NcdTA0MzVcdTA0M2RcdTA0M2FcdTA0M2JcdTA0MzBcdTA0NDJcdTA0NDNcdTA0NDBcdTA0MzAgKFBhcmlzaWFuYSBub21pbmEgYW5hdG9taWNhKSIsICJzZXJpZXMiOiBbIiJdLCAiYXV0aG9yIjogWyJcdTA0MWNcdTA0MzhcdTA0NDVcdTA0MzBcdTA0MzlcdTA0M2JcdTA0M2VcdTA0MzIgXHUwNDIxLlx1MDQyMS4gKFx1MDQ0MFx1MDQzNVx1MDQzNC4pIl0sICJwdWJsaXNoZXIiOiAiXHUwNDFjXHUwNDM1XHUwNDM0XHUwNDM4XHUwNDQ2XHUwNDM4XHUwNDNkXHUwNDMwIiwgImxhbmd1YWdlIjogWyJSdXNzaWFuIl0sICJtZDUiOiAiIiwgInRhZ3MiOiBbIlx1MDQxMVx1MDQzOFx1MDQzZVx1MDQzYlx1MDQzZVx1MDQzM1x1MDQzOFx1MDQ0N1x1MDQzNVx1MDQ0MVx1MDQzYVx1MDQzOFx1MDQzNSBcdTA0MzRcdTA0MzhcdTA0NDFcdTA0NDZcdTA0MzhcdTA0M2ZcdTA0M2JcdTA0MzhcdTA0M2RcdTA0NGIiLCAiXHUwNDEwXHUwNDNkXHUwNDMwXHUwNDQyXHUwNDNlXHUwNDNjXHUwNDM4XHUwNDRmIiwgIlx1MDQyMVx1MDQzYlx1MDQzZVx1MDQzMlx1MDQzMFx1MDQ0MFx1MDQzOCBcdTA0MzggXHUwNDQwXHUwNDMwXHUwNDM3XHUwNDMzXHUwNDNlXHUwNDMyXHUwNDNlXHUwNDQwXHUwNDNkXHUwNDM4XHUwNDNhXHUwNDM4Il0sICJpc3NuIjogIiIsICJpcGZzX2NpZCI6ICJiYWZ5a2J6YWNlZGptMjd5bWFwdDRqdDRoMnVlanJveWkydmw2cW4zcW9lMm9zcWUzamphN2E3bzZsbmtseSIsICJleHRlbnNpb24iOiAiZGp2dSJ9",
           "proof": {
             "root_hash": "711715C5DD2D929F5FA6128E73E63690C4CE876D92BE120040F379B50897E567",
             "data": "CghteV90b2tlbhrRBxIGbGliZ2VuGiA1MTczMjc1ZjAyOWE3ZjBiNzhiZGNhY2EzNGE2ZGFjYyKkB3sidGl0bGUiOiAiXHUwNDFjXHUwNDM1XHUwNDM2XHUwNDM0XHUwNDQzXHUwNDNkXHUwNDMwXHUwNDQwXHUwNDNlXHUwNDM0XHUwNDNkXHUwNDMwXHUwNDRmIFx1MDQzMFx1MDQzZFx1MDQzMFx1MDQ0Mlx1MDQzZVx1MDQzY1x1MDQzOFx1MDQ0N1x1MDQzNVx1MDQ0MVx1MDQzYVx1MDQzMFx1MDQ0ZiBcdTA0M2RcdTA0M2VcdTA0M2NcdTA0MzVcdTA0M2RcdTA0M2FcdTA0M2JcdTA0MzBcdTA0NDJcdTA0NDNcdTA0NDBcdTA0MzAgKFBhcmlzaWFuYSBub21pbmEgYW5hdG9taWNhKSIsICJzZXJpZXMiOiBbIiJdLCAiYXV0aG9yIjogWyJcdTA0MWNcdTA0MzhcdTA0NDVcdTA0MzBcdTA0MzlcdTA0M2JcdTA0M2VcdTA0MzIgXHUwNDIxLlx1MDQyMS4gKFx1MDQ0MFx1MDQzNVx1MDQzNC4pIl0sICJwdWJsaXNoZXIiOiAiXHUwNDFjXHUwNDM1XHUwNDM0XHUwNDM4XHUwNDQ2XHUwNDM4XHUwNDNkXHUwNDMwIiwgImxhbmd1YWdlIjogWyJSdXNzaWFuIl0sICJtZDUiOiAiIiwgInRhZ3MiOiBbIlx1MDQxMVx1MDQzOFx1MDQzZVx1MDQzYlx1MDQzZVx1MDQzM1x1MDQzOFx1MDQ0N1x1MDQzNVx1MDQ0MVx1MDQzYVx1MDQzOFx1MDQzNSBcdTA0MzRcdTA0MzhcdTA0NDFcdTA0NDZcdTA0MzhcdTA0M2ZcdTA0M2JcdTA0MzhcdTA0M2RcdTA0NGIiLCAiXHUwNDEwXHUwNDNkXHUwNDMwXHUwNDQyXHUwNDNlXHUwNDNjXHUwNDM4XHUwNDRmIiwgIlx1MDQyMVx1MDQzYlx1MDQzZVx1MDQzMlx1MDQzMFx1MDQ0MFx1MDQzOCBcdTA0MzggXHUwNDQwXHUwNDMwXHUwNDM3XHUwNDMzXHUwNDNlXHUwNDMyXHUwNDNlXHUwNDQwXHUwNDNkXHUwNDM4XHUwNDNhXHUwNDM4Il0sICJpc3NuIjogIiIsICJpcGZzX2NpZCI6ICJiYWZ5a2J6YWNlZGptMjd5bWFwdDRqdDRoMnVlanJveWkydmw2cW4zcW9lMm9zcWUzamphN2E3bzZsbmtseSIsICJleHRlbnNpb24iOiAiZGp2dSJ9",
             "proof": {
               "total": "1",
               "index": "0",
               "leaf_hash": "cRcVxd0tkp9fphKOc+Y2kMTOh22SvhIAQPN5tQiX5Wc=",
               "aunts": []
             }
           }
         }
       ],
       "total_count": "1"
     }
    }
```

## Search Block
You can search block by block_search , or fetch the latest block.

``` python
    res = glitter_client.chain.block_search(query="block.height = 1000")
    print(res)
    {
     "jsonrpc": "2.0",
     "id": -1,
     "result": {
       "blocks": [
         {
           "block_id": {
             "hash": "10AB4DBCC0E8BA06381A6580197AAB68EAACDEA64BBAB50FB36B00F99A8191CB",
             "parts": {
               "total": 1,
               "hash": "1734A94A2C210C9EE19B1DB15D116666CF9B68FB1DCE69883E27DA935712D449"
             }
           },
           "block": {
             "header": {
               "version": {
                 "block": "11",
                 "app": "1"
               },
               "chain_id": "chain-LNTnFa",
               "height": "1000",
               "time": "2022-02-19T12:44:25.390486401Z",
               "last_block_id": {
                 "hash": "DDEC58156107A30971C4A5BAF87C9CDD807597E686BEE1E344F477DD09C73DFB",
                 "parts": {
                   "total": 1,
                   "hash": "6CCC27C8A8BCA4C0E47F38B88D6E3FC4DE714380A9ABED1B498F8DB3FF18DE15"
                 }
               },
               "last_commit_hash": "601649850FBE9681EB9C1A2F294BA841321BD0E2D7826244B6540C435FFDABD7",
               "data_hash": "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855",
               "validators_hash": "E49055092750BE7A2533BD17E226E80A5E030A105E068D063D9BF46E6AED504F",
               "next_validators_hash": "E49055092750BE7A2533BD17E226E80A5E030A105E068D063D9BF46E6AED504F",
               "consensus_hash": "048091BC7DDC283F77BFBF91D73C44DA58C3DF8A9CBC867405D8B7F3DAADA22F",
               "app_hash": "",
               "last_results_hash": "6E340B9CFFB37A989CA544E6BB780A2C78901D3FB33738768511A30617AFA01D",
               "evidence_hash": "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855",
               "proposer_address": "E54A63CD67AA32386894EDE5839767F4CD6EC121"
             },
             "data": {
               "txs": []
             },
             "evidence": {
               "evidence": []
             },
             "last_commit": {
               "height": "999",
               "round": 0,
               "block_id": {
                 "hash": "DDEC58156107A30971C4A5BAF87C9CDD807597E686BEE1E344F477DD09C73DFB",
                 "parts": {
                   "total": 1,
                   "hash": "6CCC27C8A8BCA4C0E47F38B88D6E3FC4DE714380A9ABED1B498F8DB3FF18DE15"
                 }
               },
               "signatures": [
                 {
                   "block_id_flag": 2,
                   "validator_address": "1F690E3E9C072133F3B897B358C0F2F127F16704",
                   "timestamp": "2022-02-19T12:44:25.390486401Z",
                   "signature": "2Zw73NO8ZDiujWHWg4mIKquf1q+aWlE1pMZp9xQ32QZNkG8++XnNin7gQRfmPIjeTnVGSvYtyxXArb2LDKnUAQ=="
                 },
                 {
                   "block_id_flag": 2,
                   "validator_address": "7CE3A03CBCDD77187D9AFD0C242ED0AB910B6ACD",
                   "timestamp": "2022-02-19T12:44:25.391515882Z",
                   "signature": "xauumFCrfeGClZnZuEEnGKu65L4gHj/S1wI+RZF74RaFB4QVz72GLdeEv5GJ1gkWH5GwCt9nnBSMsvaPAzOxCA=="
                 },
                 {
                   "block_id_flag": 2,
                   "validator_address": "88839061A231E8A1C8285B67EF8BCBE97C3D94BF",
                   "timestamp": "2022-02-19T12:44:25.39137696Z",
                   "signature": "UWmIjOSplfmUGbbbv9v0VXJIK+qypiMahC0YHCGgNjJm1rmJ43IXMD9jDttgjpn/qCkGcjCcmzVuEmxgG2YvCA=="
                 },
                 {
                   "block_id_flag": 2,
                   "validator_address": "8A380491EEC814F390C113E622258F5FA46B2765",
                   "timestamp": "2022-02-19T12:44:25.390398641Z",
                   "signature": "68WuIwIggTlpuJWzQBT8/76e9WvooeAyuRWvZ/raTHrQEiiXEA8KU2u7/H3EjKXSOWGtvXwY1vtsviSeBvfdDA=="
                 },
                 {
                   "block_id_flag": 2,
                   "validator_address": "E54A63CD67AA32386894EDE5839767F4CD6EC121",
                   "timestamp": "2022-02-19T12:44:25.390518133Z",
                   "signature": "E5M9LRCeONpiM+NRu/x6UuGelcE+EYN3MvfUYw6DRdAS33WEsUDGeZ6B3BYlw/ehd3ecclg/sCShVRk2xHoGDA=="
                 }
               ]
             }
           }
         }
       ],
       "total_count": "1"
     }
   }
```

```python
 res = glitter_client.chain.block()
```


## Fetch Validator Status
Get validator set at a specified height

``` python
res = glitter_client.admin.validators()
{
     "jsonrpc": "2.0",
     "id": -1,
     "result": {
       "block_height": "468323",
       "validators": [
         {
           "address": "1F690E3E9C072133F3B897B358C0F2F127F16704",
           "pub_key": {
             "type": "tendermint/PubKeyEd25519",
             "value": "NLmuSxM3ajCX1qNyiwZVXwv16KfFa2I2TRXGuWaAt0w="
           },
           "voting_power": "1",
           "proposer_priority": "-2"
         },
         {
           "address": "7CE3A03CBCDD77187D9AFD0C242ED0AB910B6ACD",
           "pub_key": {
             "type": "tendermint/PubKeyEd25519",
             "value": "ijED7uyHJH4dc3uF7PJM1//b7L+EcAP8E0NOrk6aDdA="
           },
           "voting_power": "1",
           "proposer_priority": "-2"
         },
         {
           "address": "88839061A231E8A1C8285B67EF8BCBE97C3D94BF",
           "pub_key": {
             "type": "tendermint/PubKeyEd25519",
             "value": "tV6rC04s6/EQU6e7J/wFH+g/jSblGSnaDUhTHCHzBEI="
           },
           "voting_power": "1",
           "proposer_priority": "-2"
         },
         {
           "address": "8A380491EEC814F390C113E622258F5FA46B2765",
           "pub_key": {
             "type": "tendermint/PubKeyEd25519",
             "value": "fBqygqcjcMoYIyHHsWeWYnP9jUkY+6PZPmJRGzzJRX0="
           },
           "voting_power": "1",
           "proposer_priority": "3"
         },
         {
           "address": "E54A63CD67AA32386894EDE5839767F4CD6EC121",
           "pub_key": {
             "type": "tendermint/PubKeyEd25519",
             "value": "3yyODkAeja03IIz37bp2ufmSau8CQ5oqc2qrKxo3YlA="
           },
           "voting_power": "1",
           "proposer_priority": "3"
         }
       ],
       "count": "5",
       "total": "5"
     }
   }
   ```

If no height is provided, it will fetch validator set which corresponds to the latest block.


```python
res = glitter_client.admin.validators(height=100000)
```



## Update Validator
----------------------------
Update validator pow.

```python
    pub_key = "xxx"
    res = glitter_client.admin.update_validator(pub_key, 1)
    print(res)
``` 