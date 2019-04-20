'''
Python Implementation of an algorithm to enable pagination in a messaging system
A user message can be longer than what can be sent at a time, hence splitting the message into smaller and efficient
chunks(160 characters or less) is necessary.
Some words like 'to'/'is' must be treated as a whole word when they appear as the last item in the chunk list and should not be splitted.
Otherwise if the last word in the list is for example 'possible' and the 160th character is at 'poss', the 'poss' will be in the first chunk
but the remaining 'ible' will be sent to the next chunk as the first item. when done we rejoin the two and create a chunk which shall
be pushed into our final intended array(list).

::OFTEN move the last word of the chunk to the next chunk since there is no guarantee it would be complete
'''


def processMessage(message):
    '''Checks if the user message is not more than 1440 characters,
     if the message is 160 characters or less, it will be sent as it is without further formatting'''
    if len(message) < 1 or len(message) > 1440:
        return "Message must be between 1-1440 characters"

    if len(message) <= 160:
        '''return the message without further formating but as a list'''
        return [message]
    '''text is longer than 160,  set the counter and split into smaller chunks as required::
    processing of long texts is done here
    '''
    n = 160
    chunks = []
    last_words = []
    next_chunks = []
    '''Exclude the following one-word(s) when recreating the chunks'''
    helpers = ['is', 'was', 'to', 'the', 'why', 'it', 'on', 'in', 'of']

    for i in range(0, len(message), n):
        chunk = message[i:i + n]
        # create a mini-list for words in the chunk so we can tell the last n next words per chunk
        word_list = chunk.split(' ')

        last_chars = ''
        next_word = ''
        next_chars = ''
        if ' '.join(word_list) not in chunks:
            if len(chunks) == 0:
                '''insert the first item into the list, but take care of the last word in the list'''
                if word_list[-1].lower() not in helpers:
                    last_chars = word_list.pop(-1)
                    last_words.append(last_chars)
                chunks.append(' '.join(word_list))
            else:
                '''work on the next chunk for list of the chunks'''
                # Extract the next first word of the next chunk only if the last words list from the previous chunk
                # not empty
                if len(last_words)>0:
                    next_chunk_list = word_list
                    next_chars = next_chunk_list.pop(0)
                    if next_chars not in helpers:
                        next_chunks.append(next_chars)
                        print('next chunks',next_chunks)
                # get the last item in the main list
                last_text = chunks[-1] if len(chunks) > 0 else ''
                if len(last_text) >= 160:
                    chunk_list = last_text.split(' ')
                    last_chars = chunk_list.pop(-1)
                    if len(last_chars) > 0 and last_chars not in helpers:  # skip empty strings and words listed as exceptions
                        last_words.append(last_chars)
                    print('test: ', last_chars + next_chars)
                # create the next first word/item for the next chunk
                if len(last_words) > 0 and len(next_chunks) > 0:
                    next_word = last_words.pop(0) + next_chunks.pop(0)
                    print(next_word)
                    # push this into the next chunk as the first item
                    word_list.insert(0, next_word)
                chunks.append(' '.join(word_list))

        print('last_word: ', last_chars)
        print('next_first_word: ', next_word)
        print('last words ', last_words)
        print('next words ', next_chunks)

    return chunks

# LET'S test the code
if __name__ == '__main__':
    message = input('Enter your message:\n')

    processed = processMessage(message)
    print(processed)

'''TESTED WITH THE FOLLOWING LONG TEXTS AND RESULTS WERE OK::
As a reminder, you have an appointment with Dr. Smith tomorrow at 3:30pm. If you are unable to make this appointment, please call our customer service line at least 1 hour before your scheduled appointment time .'''
'''A company has hired you as a consultant to develop software that can be used for sending SMS to their end-users.
 Currently, the maximum number of characters possible for one message is 160.
The company has expressed concerns that when sending messages in different chunks 
there is no guarantee that the messages will be delivered to the end-user’s phone in order.'''
