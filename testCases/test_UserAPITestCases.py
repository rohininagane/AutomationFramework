import os
import pytest
import requests
import json
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class Test_APITest:
    post_test_data_path = os.path.join(os.path.dirname(__file__), '..', 'TestData', 'CreateUserData.json')
    # Load test data from a JSON file
    with open(post_test_data_path) as f:
        post_test_data = json.load(f)

    put_test_data_path = os.path.join(os.path.dirname(__file__), '..', 'TestData', 'UpdateUserData.json')
    # Load test data from a JSON file
    with open(put_test_data_path) as f:
        put_test_data = json.load(f)
    @pytest.mark.api
    @pytest.mark.sanity
    @pytest.mark.parametrize("user_data", post_test_data)
    def test_create_user(self,user_data):
        """
        Test updating users with the provided test data.
        """
        logger = LogGen.loggen("UserPostAPICall")
        try:
            logger.info("************* Verify create user functionality using post api call **********")
            # Read endpoint from config file
            BASE_URL=ReadConfig.getAPIEndPoint('APIEndPoints','createuser')

            # Load the request template
            request_template_path = os.path.join(os.path.dirname(__file__), '..', 'RequestTemplates', 'CreateUser.json')
            with open(request_template_path) as f:
                request_template = json.load(f)[0]

            # Merge the test data with the request template
            request_payload = {**request_template, **user_data}

            logger.info("************* Create User Post API request sent **********")
            username=request_payload.get('username')
            logger.info("************* Username: %s **********",username)

            # Send a Post request to the API endpoint
            response = requests.post(BASE_URL, json=[request_payload])
            logger.info("************* Create User Post API response received **********")

            # Check the response status code
            assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
            # Check the response JSON body
            response_json = response.json()
            assert response_json['code'] == 200, f"Expected response code 200 but got {response_json.get('code')}"
            assert response_json['message'] == "ok", f"Expected response message 'ok' but got {response_json.get('message')}"
            logger.info("************* Status code:%d **************", response.status_code)
            logger.info("************* Response message:%s **************",response_json.get('message'))

            logger.info("************* Verifying created user using get api call **************")
            BASE_URL = ReadConfig.getAPIEndPoint('APIEndPoints', 'getuser')
            url = f"{BASE_URL}/{username}"
            logger.info("************* Get API call endpoint:%s **************", url)
            logger.info("************* Sending request **************")
            response = requests.get(url)
            assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
            logger.info("************* Status Code:%d **************", response.status_code)
            response_json = response.json()
            assert response_json.get('username') == username, f"got unexpected username {response_json.get('username')}"
            logger.info("************* Verified created user's username: %s **************", response_json.get('username'))
        except Exception as e:
            logger.error("Test Case Failed: %s", e)
            raise

    @pytest.mark.api
    @pytest.mark.sanity
    @pytest.mark.parametrize("user_data", put_test_data)
    def test_update_user(self, user_data):
        """
        Test updating users with the provided test data.
        """
        logger = LogGen.loggen("UserPutAPICall")
        try:
            logger.info("************* Verify update user functionality using put api call **********")
            # Load the request template
            request_template_path = os.path.join(os.path.dirname(__file__), '..', 'RequestTemplates', 'CreateUser.json')
            with open(request_template_path) as f:
                request_template = json.load(f)[0]

            # Merge the test data with the request template
            request_payload = {**request_template, **user_data}
            logger.info("************* Update User Put API request sent **********")
            username = request_payload.get('username')
            email = request_payload.get('email')
            logger.info("************* Username: %s **********", username)

            # Read endpoint from config file
            BASE_URL = ReadConfig.getAPIEndPoint('APIEndPoints', 'updateuser')
            BASE_URL = BASE_URL.rstrip('/')
            url =f"{BASE_URL}/{username}"
            logger.info("************* Baseurl: %s **********", url)
            # Send a Post request to the API endpoint
            response = requests.put(url, json=[request_payload])
            logger.info("************* Update User Put API response received **********")

            # Check the response status code
            assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
            # Check the response JSON body
            response_json = response.json()
            assert response_json['code'] == 200, f"Expected response code 200 but got {response_json.get('code')}"
            assert response_json['message'] == "ok", f"Expected response message 'ok' but got {response_json.get('message')}"
            logger.info("************* Status code:%d **************", response.status_code)
            logger.info("************* Response message:%s **************", response_json.get('message'))

            logger.info("************* Verifying updated fields using get api call **************")
            BASE_URL = ReadConfig.getAPIEndPoint('APIEndPoints', 'getuser')
            url = f"{BASE_URL}/{username}"
            logger.info("************* Get API call endpoint:%s **************", url)

            response = requests.get(url)
            logger.info("************* request sent **************")
            assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
            logger.info("************* Status Code:%d **************", response.status_code)
            response_json = response.json()
            assert response_json.get('username') == username, f"got unexpected username {response_json.get('username')}"
            logger.info("************* Verified updated user's username: %s **************",response_json.get('username'))
            assert response_json.get('email') == email, f"got unexpected username {response_json.get('email')}"
            logger.info("************* Verified updated user's username: %s **************",response_json.get('email'))

        except Exception as e:
            logger.error("Test Case Failed: %s", e)
            raise

    @pytest.mark.api
    @pytest.mark.sanity
    @pytest.mark.parametrize("user_name", ["Jack99"])
    def test_get_user(self,user_name):
        try:
            logger = LogGen.loggen("UserGetAPICall")
            logger.info("************* Verify Get User API call **************")
            BASE_URL=ReadConfig.getAPIEndPoint('APIEndPoints','getuser')
            url = f"{BASE_URL}/{user_name}"
            logger.info("************* Get API call endpoint:%s **************",url)
            logger.info("************* Sending Get call for username:%d **************", user_name)
            response = requests.get(url)
            response_json = response.json()
            assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
            logger.info("************* Status Code:%d **************", response.status_code)
            assert response_json.get('username') == user_name, f"got unexpected username {response_json.get('username')}"
            logger.info("************* Received data successfully for expected username: %s **************",response_json.get('username'))
        except Exception as e:
            logger.error("Test Case Failed : %s", e)
            raise

    def load_json(filepath):
        with open(filepath, 'r') as file:
            data = json.load(file)
        return data

