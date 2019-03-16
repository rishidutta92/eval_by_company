
import sys
import json
import unittest
sys.path.append(“../..”)
import new_operations

class TestFunctions(unittest.TestCase):
 “””Test case for the client methods.”””
    def setup(self):
        app.app.config[‘TESTING’] = True
        self.app = app.app.test_client()
        # Test of Output function
        
        def test_output(self):
            with app.test_request_context():
            # mock object
            out = output(‘error’, ‘Test Error’, ‘local_host’)
            # Passing the mock object
            response = [
              {
                     ‘type’: ‘error’,
                     ‘message’: ‘Test Error’,
                     ‘download_link’: ‘local_host’
               }
            ]
            data = json.loads(out.get_data(as_text=True)
            # Assert response
            self.assertEqual(data[‘response’], response)

if __name__ == ‘__main__’:
      unittest.main()