def hangman():
    word = "python"
    guessed_letters = []
    tries = 6

    while tries > 0:
        guess = input("文字を入力してください: ").lower()

        if guess in guessed_letters:
            print("もうその文字は入力しています。")
        elif guess in word:
            print("正解です！")
            guessed_letters.append(guess)
        else:
            print("間違いです。")
            guessed_letters.append(guess)
            tries -= 1
        
        display_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
        print(f"単語: {display_word}")
        
        if display_word.replace(" ", "") == word:
            print("おめでとうございます！ハングマンに勝ちました！")
            break
    else:
        print(f"残念！ハングマンで負けました。正しい単語は {word} でした。")

hangman()
