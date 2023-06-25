from openai_python_mocks import mock_openai
import openai


@mock_openai
def test_chat_gpt():
    openai.api_key = "cewdwecws"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a talking cat and should respond as such. Be sure to say 'meow' often.",
            },
            {"role": "user", "content": "Do you want a treat?"},
        ],
    )

    assert (
        response["choices"][0]["message"]["content"]
        == "I am just a computer. Unfortunantely I cannot help you with this issue"
    )
    assert type(response["created"]) == int
    assert len(str(response["created"])) == 10
