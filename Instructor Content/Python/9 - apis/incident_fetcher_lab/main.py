import requests
from typing import List, Optional

def get_incident_summary(api_url: str, api_key: str, service_id: str) -> Optional[List[str]]:
    # Input validation
    for value in (api_url, api_key, service_id):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("All arguments must be non-empty strings")

    url = f"{api_url.rstrip('/')}/incidents"

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    params = {
        "service_ids[]": service_id,
        "statuses[]": "triggered"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        return None

    data = response.json()
    incidents = data.get("incidents", [])

    if not incidents:
        return []

    summary = []

    for incident in incidents:
        urgency = incident.get("urgency", "").upper()
        incident_id = incident.get("id", "")
        title = incident.get("title", "")
        summary.append(f"[{urgency}] {incident_id}: {title}")

    return summary