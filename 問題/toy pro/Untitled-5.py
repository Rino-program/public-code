"""
問題1: 単語の頻度カウント（書籍データ解析）
与えられたテキストファイル内の各単語の出現頻度をカウントし、
結果を頻度の高い順にソートして表示するプログラムを書いてください。

入力例：
In the beginning, the universe was created. This has made a lot of people very angry and has been widely regarded as a bad move.
The universe, as observed today, is vast and incredibly complex. Galaxies, stars, planets, and countless other celestial bodies are scattered across the cosmos.
Humankind has always been fascinated by the night sky, seeking to understand the mysteries of space.
Ancient civilizations observed the stars and created constellations, weaving stories and myths around them. These stories were passed down through generations, shaping cultures and belief systems.
In the modern era, the study of astronomy has advanced significantly. Telescopes and spacecraft allow us to explore the universe in ways that were once thought impossible.
Scientists have discovered exoplanets orbiting distant stars, black holes with immense gravitational pull, and cosmic phenomena that challenge our understanding of physics.
Despite our advancements, many questions about the universe remain unanswered. What is the nature of dark matter and dark energy? How did the universe begin, and how will it end?
The quest for knowledge continues, driving human exploration and curiosity. As we look to the future, we are reminded that the universe holds many secrets yet to be discovered.
Each new discovery adds to our understanding, revealing a cosmos more wondrous and mysterious than we could have ever imagined.
"""
#code
txt = """In a quaint village nestled between rolling hills and a shimmering lake, there lived a young girl named Emily. Every morning, she would wake up with the first light of dawn, stretching her arms and breathing in the crisp, fresh air. The village was small, but it was filled with charm and warmth. The cobblestone streets were lined with ancient trees, their leaves rustling gently in the breeze. Birds chirped merrily, creating a symphony of natural sounds that resonated throughout the day.

Emily loved exploring the woods that surrounded her village. Each day was a new adventure, with hidden paths, secret glades, and enchanting clearings waiting to be discovered. She would often come across deer grazing peacefully, their eyes filled with curiosity and grace. Rabbits would dart across her path, quick and elusive, while squirrels chattered from the branches above.

One day, as she wandered deeper into the forest, she stumbled upon an old, weathered map. The map was tattered and faded, but it showed a path leading to a hidden treasure. Her heart raced with excitement as she followed the clues, navigating through dense undergrowth and over babbling brooks. After what felt like hours, she arrived at a clearing where an ancient oak tree stood. Its branches spread wide, casting a protective shadow over a small, moss-covered chest.

With trembling hands, Emily opened the chest to find it filled with sparkling gems and coins from a time long past. But more valuable than the treasure itself was the sense of wonder and discovery that filled her heart. She knew that this adventure was just the beginning, and that the world held countless mysteries waiting to be uncovered.

Emily returned to her village, her eyes sparkling with excitement and her heart brimming with stories to share. From that day on, she became known as the village explorer, inspiring others to venture beyond the familiar and embrace the wonders of the unknown. And so, the village thrived, filled with tales of adventure, discovery, and the unending beauty of the world around them."""
txt = txt.replace(".", "").replace(",", "").replace("\n", "")
txt = txt.split(" ")

# 各単語の出現回数をカウント
word_count = {}
for word in txt:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# 出現回数でソート
sorted_word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

# 結果を表示
for word, count in sorted_word_count:
    print(f"{word}: {count}")