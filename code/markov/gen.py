import markovify

with open("ibos-gpt-mm.json", "r") as f:
    print("Loading Markov Model 🧐")
    model_json = f.read()
    model = markovify.Text.from_json(model_json)

    print("✨Model loaded✨ Enter prompt. Enter 'q' to exit.")
    prompt = input("> ")
    while prompt != "q":
        try:
            print(model.make_sentence_with_start(prompt, strict=False))
        except Exception:
            print("something went wrong 😥")
        prompt = input("> ")

    # for i in range(5):
    #     # print(model.make_sentence())
    #     print(model.make_sentence_with_start("God"))
