def response(hey_bob):
    hey_bob_strip = hey_bob.strip()
    is_question = len(hey_bob_strip) > 0 and hey_bob_strip[-1] == "?"
    is_yelling = hey_bob_strip.isupper()
    is_silence = hey_bob_strip.isspace() or hey_bob_strip == ""

    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    elif is_question:
        return "Sure."
    elif is_yelling:
        return "Whoa, chill out!"
    elif is_silence:
        return "Fine. Be that way!"
    else:
        return "Whatever."
