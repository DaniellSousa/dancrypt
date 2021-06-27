# coding=utf-8

list_ascii_table = [".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A",
                    " ", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", "A", "B", "C", "D", "E", "F",
                    "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                    "[", "\\", "]", "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                    "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~",
                    "á", "â", "ã", "à", "ç", "é", "ê", "í", "ó", "ô", "õ", "ú",
                    "Á", "Â", "Ã", "À", "Ç", "É", "Ê", "Í", "Ó", "Ô", "Õ", "Ú"]

list_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y", "z"]


class DanCrypt:
    def decrypt_text(self, text_to_decrypt):
        str_final = get_text_with_half_one_position_right_in_ascci(text_to_decrypt)

        str_final = get_inverse_fo_text(str_final)

        str_final = get_text_shift_position_left_ascii(str_final, 3)

        return str_final

    def encrypt_text(self, text_to_encrypt):
        str_final = get_text_shift_position_right_ascii(text_to_encrypt, 3)

        str_final = get_inverse_fo_text(str_final)

        str_final = get_text_with_half_one_position_left_in_ascci(str_final)

        return str_final


def get_text_with_half_one_position_right_in_ascci(text):
    str_crypt = ""
    iteration = int(len(str(text)) / 2)
    i_final = 0
    for s in str(text):
        if i_final >= iteration:
            p, l = get_position_character_and_position_at_right_ascii(s, 1)
            str_crypt += l
        else:
            str_crypt += s
        i_final += 1

    return str_crypt


def get_text_with_half_one_position_left_in_ascci(text):
    str_crypt = ""
    iteration = int(len(str(text)) / 2)
    i_final = 0
    for s in str(text):
        if i_final >= iteration:
            p, l = get_position_character_and_position_at_left_ascii(s, 1)
            str_crypt += l
        else:
            str_crypt += s
        i_final += 1

    return str_crypt


def get_inverse_fo_text(text):
    return text[len(text)::-1]


def get_text_shift_position_right_ascii(text_to_encrypt, position):
    str_final = ""
    for c in text_to_encrypt:
        p, l = get_position_character_and_position_at_right_ascii(c, position)
        str_final += l

    return str_final


def get_text_shift_position_left_ascii(text_to_encrypt, position):
    str_final = ""
    for c in text_to_encrypt:
        p, l = get_position_character_and_position_at_left_ascii(c, position)
        str_final += l

    return str_final


def get_position_character_and_position_at_right_ascii(char, value_position):
    i_letter = 0
    for a in list_ascii_table:
        if a == char:
            letter = list_ascii_table[i_letter + value_position]
            i_letter += value_position
            return i_letter, letter
        i_letter += 1
    return 0, ""


def get_position_character_and_position_at_left_ascii(char, value_position):
    i_letter = 0
    for a in list_ascii_table:
        if a == char:
            letter = list_ascii_table[i_letter - value_position]
            i_letter -= value_position
            return i_letter, letter
        i_letter += 1
    return 0, ""


def is_letter(char):
    for l in list_letters:
        if str(char).upper() == str(l).upper():
            return True

    return False


if __name__ == "__main__":
    dan_c = DanCrypt()

    msg = "Hello, Universe!"

    msg_crypt = dan_c.encrypt_text(msg)
    msg_decrypt = dan_c.decrypt_text(msg_crypt)

    print("Mensagem: " + str(msg))
    print("Msg cripitografada: " + str(msg_crypt))
    print("Msg descripitografada: " + str(msg_decrypt))

    # tem erro no uso de vírgula
