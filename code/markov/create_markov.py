import markovify

with open("ibos-cleaned.txt", "r") as ib:
    with open("corpus.txt", "r") as f:
        text = f.read()
        gpt_model = markovify.NewlineText(text, state_size=3)

        ibos = ib.read()
        ibos_model = markovify.NewlineText(ibos, state_size=3)

        text_model = markovify.combine([gpt_model, ibos_model], [1.5, 1.0])
        text_model = text_model.compile()

        model_json = text_model.to_json()

        with open("ibos-gpt-mm.json", "w") as out:
            out.write(model_json)
