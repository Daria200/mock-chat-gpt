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
    responses.add(
        responses.POST,
        "https://api.openai.com/v1/chat/completions",
        json={
            # TODO: generate random string
            "id": "chatcmpl-6p9XYPYSTTRi0xEviKjjilqrWU2Ve",
            "object": "chat.completion",
            # TODO: get from current time
            "created": 1677649420,
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
        },
        content_type="application/json",
    )
    return func(*args, **kwargs)
