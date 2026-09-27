# ALX Files Manager

[![Python CLI CI](https://github.com/cutechybyke/alx-files_manager/actions/workflows/python-cli-ci.yml/badge.svg)](https://github.com/cutechybyke/alx-files_manager/actions/workflows/python-cli-ci.yml)

A backend file-management project developed as part of the ALX software engineering curriculum, with a Node.js API and a Python image-upload command-line client.

## Project areas

- File-management API
- Authentication/token-based requests
- File metadata and upload handling
- Python CLI for image uploads
- Input/file validation
- HTTP timeout and failure handling
- Automated Python CLI tests
- GitHub Actions CI

## Python upload client

Install the client dependency:

```bash
pip install -r requirements-cli.txt
```

Upload an image:

```bash
python image_upload.py ./photo.jpg TOKEN
```

An optional parent folder can be supplied:

```bash
python image_upload.py ./photo.jpg TOKEN PARENT_ID
```

The API URL and timeout can also be configured through command-line options.

## Tests

```bash
python -m unittest -v test_image_upload.py
```

Tests cover missing-file validation, base64 upload construction, authentication headers, timeout forwarding and root-folder uploads.

## Engineering improvements

The original upload helper was converted into a proper CLI using argparse, explicit validation, request timeouts, HTTP status handling and meaningful process exit codes. Automated tests and CI now protect that behavior.
