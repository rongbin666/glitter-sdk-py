---
layout: nodes.liquid
section: developer
date: Last Modified
title: "Python SDK"
permalink: "docs/py-sdk/"
excerpt: "Smart Contracts and Chainlink"
metadata:
title: "python sdk"
description: "Learn the basic concepts about what smart contracts are and, how to write them, and how Chainlink oracles work with smart contracts."
---

# Table of Contents

* [glitter\_driver.driver](#glitter_driver.driver)
  * [GlitterClient](#glitter_driver.driver.GlitterClient)
    * [\_\_init\_\_](#glitter_driver.driver.GlitterClient.__init__)
    * [nodes](#glitter_driver.driver.GlitterClient.nodes)
    * [transport](#glitter_driver.driver.GlitterClient.transport)
    * [chain](#glitter_driver.driver.GlitterClient.chain)
    * [admin](#glitter_driver.driver.GlitterClient.admin)
    * [db](#glitter_driver.driver.GlitterClient.db)
  * [NamespacedDriver](#glitter_driver.driver.NamespacedDriver)
    * [\_\_init\_\_](#glitter_driver.driver.NamespacedDriver.__init__)
  * [DataBase](#glitter_driver.driver.DataBase)
    * [list\_schema](#glitter_driver.driver.DataBase.list_schema)
    * [put\_doc](#glitter_driver.driver.DataBase.put_doc)
    * [get\_docs](#glitter_driver.driver.DataBase.get_docs)
    * [simple\_search](#glitter_driver.driver.DataBase.simple_search)
    * [complex\_search](#glitter_driver.driver.DataBase.complex_search)
  * [Chain](#glitter_driver.driver.Chain)
    * [status](#glitter_driver.driver.Chain.status)
    * [tx\_search](#glitter_driver.driver.Chain.tx_search)
    * [block\_search](#glitter_driver.driver.Chain.block_search)
    * [block](#glitter_driver.driver.Chain.block)
    * [health](#glitter_driver.driver.Chain.health)
    * [net\_info](#glitter_driver.driver.Chain.net_info)
    * [blockchain](#glitter_driver.driver.Chain.blockchain)
    * [header](#glitter_driver.driver.Chain.header)
    * [header\_by\_hash](#glitter_driver.driver.Chain.header_by_hash)
    * [block\_by\_hash](#glitter_driver.driver.Chain.block_by_hash)
  * [Admin](#glitter_driver.driver.Admin)
    * [update\_validator](#glitter_driver.driver.Admin.update_validator)
    * [validators](#glitter_driver.driver.Admin.validators)

<a id="glitter_driver.driver"></a>

# glitter\_driver.driver

<a id="glitter_driver.driver.GlitterClient"></a>

## GlitterClient Objects

```python
class GlitterClient()
```

A :class: `driver.GlitterClient` is python client  for glitter.

<a id="glitter_driver.driver.GlitterClient.__init__"></a>

#### \_\_init\_\_

```python
def __init__(*nodes, *, headers=None, transport_class=Transport, timeout=20)
```

Initialize a :class:`~driver.GlitterClient` driver instance.

**Arguments**:

  *nodes:(list of (str or dict)): Glitter nodes to connect to.
- `headers` _dict_ - Optional headers that will be passed with each request
- `transport_class` - Optional transport class to use.
- `timeout` _int_ - Optional timeout in seconds that will be passed to each request.

<a id="glitter_driver.driver.GlitterClient.nodes"></a>

#### nodes

```python
@property
def nodes()
```

:obj:`tuple` of :obj:`str`:
URLs of connected nodes.

<a id="glitter_driver.driver.GlitterClient.transport"></a>

#### transport

```python
@property
def transport()
```

:class:`~driver.Transport`:
Object responsible for forwarding requests to a :class:`~driver.Connection` instance (node).

<a id="glitter_driver.driver.GlitterClient.chain"></a>

#### chain

```python
@property
def chain()
```

:class:`~driver.Chain`:
query block or transaction info.

<a id="glitter_driver.driver.GlitterClient.admin"></a>

#### admin

```python
@property
def admin()
```

:class:`~driver.Admin`:
Exposes functionalities of the ``'/admin'`` endpoint.

<a id="glitter_driver.driver.GlitterClient.db"></a>

#### db

```python
@property
def db()
```

:class:`~driver.DataBase` put or search doc from glitter.

<a id="glitter_driver.driver.NamespacedDriver"></a>

## NamespacedDriver Objects

```python
class NamespacedDriver()
```

Base class for creating endpoints (namespaced objects) that can be added
under the :class:`~driver.GlitterClient` driver.

<a id="glitter_driver.driver.NamespacedDriver.__init__"></a>

#### \_\_init\_\_

```python
def __init__(driver)
```

Initializes an instance of
:class:`~GlitterClient_driver.driver.NamespacedDriver` with the given
driver instance.

**Arguments**:

- `driver` _GlitterClient_ - Instance of
  :class:`~GlitterClient_driver.driver.GlitterClient`.

<a id="glitter_driver.driver.DataBase"></a>

## DataBase Objects

```python
class DataBase(NamespacedDriver)
```

Exposes the data of glitter db.

<a id="glitter_driver.driver.DataBase.list_schema"></a>

#### list\_schema

```python
def list_schema()
```

**Arguments**:

  - headers(dict): http header
  

**Returns**:

  - :obj:`dic`: list all schema.

<a id="glitter_driver.driver.DataBase.put_doc"></a>

#### put\_doc

```python
def put_doc(schema_name, doc_value)
```

Put document to glitter.

**Arguments**:

  - schema_name(str): the name of schema. (e.g.: ``'sci','libgen','magnet'``).
  - doc_value(:obj:`dic`):doc content.
  

**Returns**:

  - :obj:`dic`: transaction id.

<a id="glitter_driver.driver.DataBase.get_docs"></a>

#### get\_docs

```python
def get_docs(schema_name, doc_ids)
```

Get documents from glitter by doc ids.

**Arguments**:

- `schema_name(str)` - the name of schema. (e.g.: ``'sci','libgen','magnet'``).
  doc_id(list of str): main key of document,must be uniq.
- `header(:obj:`dic`)` - http header, must contain access_token key.
  

**Returns**:

  :obj:`dic`:

<a id="glitter_driver.driver.DataBase.simple_search"></a>

#### simple\_search

```python
def simple_search(index, query, order_by="", limit=10, page=1)
```

search from glitter

**Arguments**:

- `index(str)` - index name (e.g.: ``'libgen','sci','magnet'``).
- `query(str)` - query word
- `order_by(str)` - order by field (e.g.: ``'update_time'``).
- `limit(int)` - limit
- `page(int)` - page number,begin from 1
  

**Returns**:

- `:obj:`dic`` - the documents match query words.

<a id="glitter_driver.driver.DataBase.complex_search"></a>

#### complex\_search

```python
def complex_search(index, query, filters, order_by="", limit=10, page=1, header=None)
```

search from glitter,with more args.

**Arguments**:

- `index(str)` - index name (e.g.: ``'libgen','sci','magnet'``).
- `query(str)` - query word
  filters(:obj:`list` of :obj:`dic`): filter condition, examples:[{"type":"term","field":"language","value":"english","from":0.5,"to":1,"doc_count":100}] this affect score only.
- `order_by(str)` - order field
- `limit(int)` - limit
- `page(int)` - page number,begin from 1
- `header(:obj:`dic`)` - http header
  

**Returns**:

- `:obj:`dic`` - the documents match query words.

<a id="glitter_driver.driver.Chain"></a>

## Chain Objects

```python
class Chain(NamespacedDriver)
```

<a id="glitter_driver.driver.Chain.status"></a>

#### status

```python
def status()
```

Get Tendermint status including node info, pubkey, latest block hash, app hash, block height, current max peer height, and time.

**Returns**:

  :obj:`json`:Details of the HTTP API provided by the tendermint server.

<a id="glitter_driver.driver.Chain.tx_search"></a>

#### tx\_search

```python
def tx_search(query, page=1, per_page=30, order_by="\"desc\"", prove=True)
```

Search for transactions their results

**Arguments**:

- `query(str)` - query words. (e.g: ``tx.height=1000, tx.hash='xxx', update_doc.token='eliubin'``)
- `page(int)` - page number
- `per_page(int)` - number of entries per page (max: 100)
- `order_by(str)` - Order in which transactions are sorted ("asc" or "desc"), by height & index. If empty, default sorting will be still applied.
- `prove(bool)` - Include proofs of the transactions inclusion in the block
- `headers(:obj:`dic`)` - http header
  

**Returns**:

- `:obj"`json`` - transaction info

<a id="glitter_driver.driver.Chain.block_search"></a>

#### block\_search

```python
def block_search(query, page=1, per_page=30, order_by="\"desc\"")
```

Search for blocks by BeginBlock and EndBlock events

**Arguments**:

- `query(str)` - query condition. (e.g: ``block.height > 1000 AND valset.changed > 0``)
- `page(int)` - page number
- `per_page(int)` - number of entries per page (max: 100)
- `order_by(str)` - order in which blocks are sorted ("asc" or "desc"), by height. If empty, default sorting will be still applied.

**Returns**:

- `:obj:`json`` - block info

<a id="glitter_driver.driver.Chain.block"></a>

#### block

```python
def block(height=None)
```

Get block at a specified height

**Arguments**:

- `height(int)` - height
  

**Returns**:

  :obj:`json`:height to return. If no height is provided, it will fetch the latest block.

<a id="glitter_driver.driver.Chain.health"></a>

#### health

```python
def health()
```

Get node health.

**Returns**:

  Details of the HTTP API provided by the tendermint server, empty result (200 OK) on success, no response - in case of an error.

<a id="glitter_driver.driver.Chain.net_info"></a>

#### net\_info

```python
def net_info()
```

Get network info.

**Returns**:

  Details of the HTTP API provided by the tendermint server.

<a id="glitter_driver.driver.Chain.blockchain"></a>

#### blockchain

```python
def blockchain(min_height=1, max_height=20)
```

Get block headers for minHeight <= height maxHeight.
If maxHeight does not yet exist, blocks up to the current height will be returned. If minHeight does not exist (due to pruning), earliest existing height will be used.
At most 20 items will be returned. Block headers are returned in descending order (highest first).

**Arguments**:

- `min_height(int)` - Minimum block height to return
- `max_height(bool)` - Maximum block height to return
  

**Returns**:

  Block headers, returned in descending order (highest first).

<a id="glitter_driver.driver.Chain.header"></a>

#### header

```python
def header(height=1)
```

Retrieve the block header corresponding to a specified height.

**Arguments**:

- `height(int)` - height to return. If no height is provided, it will fetch the latest height.
  

**Returns**:

  Header information.

<a id="glitter_driver.driver.Chain.header_by_hash"></a>

#### header\_by\_hash

```python
def header_by_hash(header_hash)
```

Retrieve the block header corresponding to a block hash.

**Arguments**:

- `header_hash(str)` - header hash

<a id="glitter_driver.driver.Chain.block_by_hash"></a>

#### block\_by\_hash

```python
def block_by_hash(*, header_hash)
```

Get block by hash

**Arguments**:

- `header_hash(str)` - block hash. example: "0xD70952032620CC4E2737EB8AC379806359D8E0B17B0488F627997A0B043ABDED"
  

<a id="glitter_driver.driver.Admin"></a>

## Admin Objects

```python
class Admin(NamespacedDriver)
```

Exposes functionality of the ``'/admin'`` endpoint.

<a id="glitter_driver.driver.Admin.update_validator"></a>

#### update\_validator

```python
def update_validator(pub_key, power=0, headers=None)
```

update validator set

**Arguments**:

- `pub_key` _str_ - public key
- `power` _int_ - power
- `headers` _dict_ - http header
  

**Returns**:

  :obj:`dic`:

<a id="glitter_driver.driver.Admin.validators"></a>

#### validators

```python
def validators(height=None, page=1, per_page=100)
```

Get validator set at a specified height

**Arguments**:

- `height` _str_ - height to return. If no height is provided, it will fetch validator set which corresponds to the latest block.
- `page` _int_ - Page number (1-based)
- `per_page` _int_ - Number of entries per page (max: 100)
  

**Returns**:

- `:obj:`json`` - Validators. Validators are sorted first by voting power (descending), then by address (ascending).

