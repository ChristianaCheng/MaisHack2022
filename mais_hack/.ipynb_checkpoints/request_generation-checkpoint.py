import cohere


def request_generation(prompt, key):

    co = cohere.Client('{apiKey}')
    response = co.generate(prompt=prompt)

    return response.generations[0].text
