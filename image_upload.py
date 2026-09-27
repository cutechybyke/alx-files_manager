"""Small CLI client for uploading images to the Files Manager API."""

import argparse
import base64
from pathlib import Path
import sys

import requests


def parse_args():
    parser = argparse.ArgumentParser(description='Upload an image to Files Manager.')
    parser.add_argument('file', type=Path, help='Path to the image to upload')
    parser.add_argument('token', help='Authentication token')
    parser.add_argument('parent_id', nargs='?', default='0', help='Parent folder ID')
    parser.add_argument(
        '--api-url',
        default='http://127.0.0.1:5000/files',
        help='Files API endpoint (default: %(default)s)',
    )
    parser.add_argument('--timeout', type=float, default=10.0, help='Request timeout in seconds')
    return parser.parse_args()


def encode_file(file_path):
    if not file_path.is_file():
        raise FileNotFoundError(f'File not found: {file_path}')

    with file_path.open('rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def upload_image(args):
    payload = {
        'name': args.file.name,
        'type': 'image',
        'isPublic': True,
        'data': encode_file(args.file),
        'parentId': args.parent_id,
    }
    headers = {'X-Token': args.token}

    response = requests.post(
        args.api_url,
        json=payload,
        headers=headers,
        timeout=args.timeout,
    )
    response.raise_for_status()
    return response.json()


def main():
    args = parse_args()
    try:
        result = upload_image(args)
    except (OSError, requests.RequestException) as error:
        print(f'Upload failed: {error}', file=sys.stderr)
        return 1

    print(result)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
