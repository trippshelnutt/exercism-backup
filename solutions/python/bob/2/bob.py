def response(hey_bob):
    hey_bob_strip = hey_bob.strip()
    
    is_silence = not hey_bob_strip
    is_question = not is_silence and hey_bob_strip[-1] == "?"
    is_yelling = hey_bob_strip.isupper()

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
