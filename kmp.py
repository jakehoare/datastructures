_author_ = 'jake'
_project_ = 'datastructures'

def failure_function(word):
    """
    failure[i] is the length of the longest proper prefix of word[:i] that is also a proper suffix of word[:i].
    Proper prefixes of word[:i] cannot include word[i-1], proper suffixes cannot include word[0].
    Time complexity is O(n) since for every iteration either pos or pos-candidate increases, so runtime is at most 2n.
    :param word: string
    :return: failure[i] is the index in word where we can restart trying to match the text if word[i] does not match..
    """
    failure = [-1] + [0 for _ in range(len(word)-1)]
    pos = 2             # the next index of failure table to be computed
    candidate = 0       # the last index in word of proper prefix that may match a suffix

    while pos < len(word):

        if word[pos-1] == word[candidate]:  # prefix/suffix of word[:i] extends the previous prefix/suffix by 1 char
            failure[pos] = candidate + 1
            candidate += 1
            pos += 1
        elif candidate > 0:                 # no extension, update candidate since prefix/suffix of w[:candidate]
            candidate = failure[candidate]  # is also a suffix of w[:pos], keep pos same
            failure[pos] = 0
        else:   # candidate == 0
            failure[pos] = 0
            pos += 1

    return failure


def kmp_match(word, text):

    failure = failure_function(word)
    m = 0       # start index in text of current match
    i = 0       # current index in word

    while m + i < len(text):

        if word[i] == text[m + i]:  # matched char
            if i == len(word)-1:    # whole word matched
                return m
            i += 1

        else:
            if failure[i] != -1:
                m += i - failure[i]
                i = failure[i]
            else:
                m += 1
                #i = 0

    return -1


