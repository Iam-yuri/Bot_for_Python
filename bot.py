import re
import long_responsive as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    #Calculando a quantidade de palavras que aparecem na sua mensagem
    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    #Responsividade-----------------------------------------------------
    response('Olá', ['Olá', 'Oi', 'Opá', 'Eai'], single_response=True)
    response('Estou bem, e você?', ['Como', 'você', 'está'], required_words=['Como'])
    response('Obrigado', ['Seu', 'cabelo', 'está', 'lindo', 'hoje'], required_words=['cabelo', 'lindo'])

    response(long.R_EATING, ['O', 'que', 'você', 'gosta', 'de', 'comer'], required_words=['você', 'comer'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


#Testando a responsividade do sistema
while True:
    print('Bot: ' + get_response(input('Você: ')))