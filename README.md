tstore
======

Table-oriented storage for python

A table corresponds to a record type. From there you can
get/create/update/delete/list records.

Each record type should have an id field and metadata fields.
Metadata fields _creator, _updater, _creation_date, and _update_date
are set automatically.

Tests require the current user to have access to a DB named test
via unix socket and no password.
