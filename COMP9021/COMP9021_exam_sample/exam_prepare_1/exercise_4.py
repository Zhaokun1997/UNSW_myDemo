from collections import defaultdict
import string


def words(text):
    new_text = ""
    for letter in text:
        if letter in string.punctuation:
            continue
        else:
            new_text += letter
    word_map = defaultdict(set)
    # print(new_text)
    word_list = new_text.split(' ')
    # print(word_list)
    for word in word_list:
        word_map[len(word)].add(word.lower())
    result_dic = {}
    for key, value in word_map.items():
        result_dic[key] = sorted(list(value), reverse=False)
    map2 = sorted(result_dic, reverse=False)
    for length in map2:
        print(f'Words of length {length} : ')
        print(f'\t{result_dic[length]}')


string1 = 'Twelve will, believe me, be quite enough for your purpose.'

string2 = 'What was that? What does the Bishop mean?'

string3 = 'You must not fall into the common error of mistaking these simpletons ' \
          'for liars and hypocrites. They believe honestly and sincerely that their ' \
          'diabolical inspiration is divine. Therefore you must be on your guard against ' \
          'your natural compassion. You are all, I hope, merciful men: how else could you ' \
          'have devoted your lives to the service of our gentle Savior? You are going ' \
          'to see before you a young girl, pious and chaste; for I must tell you, gentlemen, ' \
          'that the things said of her by our English friends are supported by no evidence, ' \
          'whilst there is abundant testimony that her excesses have been excesses of religion ' \
          'and charity and not of worldliness and wantonness.'

words(string1)
words(string2)
words(string3)
