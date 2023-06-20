import json
import random
import string
from datetime import datetime

import responses
from decorator import decorator


@decorator
@responses.activate
def mock_openai(func, *args, **kwargs):
    """
    Mocks a call to OpenAI's chat API endpoint by returning a fixed response.

    Args:
        func (function): The function to be called.

    Returns:
        The result of calling the `func` function with the provided arguments."""

    def request_callback(request):
        letters = string.ascii_letters + string.digits
        random_string = "".join(random.choice(letters) for i in range(29))
        current_time = datetime.now().strftime("%H:%M:%S")
        response_body = {
            "id": "chatcmpl-" + random_string,
            "object": "chat.completion",
            # TODO: get from current time
            "created": current_time,
            "model": "gpt-3.5-turbo",
            # TODO: track usage
            "usage": {"prompt_tokens": 56, "completion_tokens": 31, "total_tokens": 87},
            "choices": [
                {
                    "message": {
                        "role": "assistant",
                        "content": "I am just a computer. Unfortunantely I cannot help you with this issue",
                    },
                    "finish_reason": "stop",
                    "index": 0,
                }
            ],
        }
        return (200, {}, json.dumps(response_body))

    responses.add_callback(
        responses.POST,
        "https://api.openai.com/v1/chat/completions",
        callback=request_callback,
        content_type="application/json",
    )
    return func(*args, **kwargs)
