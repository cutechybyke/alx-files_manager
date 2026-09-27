import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import image_upload


class UploadClientTests(unittest.TestCase):
    def test_encode_file_rejects_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            image_upload.encode_file(Path('/definitely/missing/image.jpg'))

    def test_upload_posts_encoded_image_without_root_parent_id(self):
        with tempfile.TemporaryDirectory() as directory:
            image_path = Path(directory) / 'image.jpg'
            image_path.write_bytes(b'image-bytes')
            args = SimpleNamespace(
                file=image_path,
                token='token',
                parent_id=None,
                api_url='http://example.test/files',
                timeout=3.0,
            )

            fake_response = SimpleNamespace(
                raise_for_status=lambda: None,
                json=lambda: {'id': '123'},
            )

            with patch('image_upload.requests.post', return_value=fake_response) as post:
                result = image_upload.upload_image(args)

            self.assertEqual(result, {'id': '123'})
            kwargs = post.call_args.kwargs
            self.assertNotIn('parentId', kwargs['json'])
            self.assertEqual(kwargs['headers']['X-Token'], 'token')
            self.assertEqual(kwargs['timeout'], 3.0)


if __name__ == '__main__':
    unittest.main()
