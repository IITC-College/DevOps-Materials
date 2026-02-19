import requests

def trigger_jenkins_job(jenkins_url: str, job_name: str, auth_token: str) -> bool:
    """
    Triggers a Jenkins job by making an authenticated POST request.

    Args:
        jenkins_url (str): The base URL of the Jenkins server.
        job_name (str): The name of the job to trigger.
        auth_token (str): The authentication token.

    Returns:
        bool: True if the job was triggered successfully (status 201), False otherwise.
    
    Raises:
        ValueError: If any argument is an empty or invalid string.
    """

    # Input validation
    if not isinstance(jenkins_url, str) or not jenkins_url.strip():
        raise ValueError("jenkins_url must be a non-empty string")

    if not isinstance(job_name, str) or not job_name.strip():
        raise ValueError("job_name must be a non-empty string")

    if not isinstance(auth_token, str) or not auth_token.strip():
        raise ValueError("auth_token must be a non-empty string")

    # Construct URL
    url = f"{jenkins_url.rstrip('/')}/job/{job_name}/build"

    # Headers
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    try:
        response = requests.post(url, headers=headers)
    except requests.exceptions.RequestException:
        # Network error handling
        return False

    # Return True only for 201 Created
    return response.status_code == 201
