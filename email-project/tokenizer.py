import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4o-mini")


def show_tokenization(text: str):
    token_ids = encoding.encode(text)
    # Decode each token ID individually so we can see the actual text pieces
    token_pieces = [encoding.decode([tid]) for tid in token_ids]

    print(f"TEXT: {text!r}")
    print(f"Token count: {len(token_ids)}")
    print(f"Token IDs: {token_ids}")
    print(f"Token pieces: {token_pieces}")
    print("-" * 60)


if __name__ == "__main__":
    show_tokenization("I don't have that information.")
    show_tokenization("strawberry")
    show_tokenization("unbelievable")
    show_tokenization("supercalifragilisticexpialidocious")
    show_tokenization("def add(a, b): return a + b")  # code tokenizes differently than prose
