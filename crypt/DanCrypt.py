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


def get_position_character_and_position_at_right(char, value_position):
    i_letter = 0
    for a in list_ascii_table:
        if a == char:
            letter = list_ascii_table[i_letter + value_position]
            i_letter += value_position
            return i_letter, letter
        i_letter += 1
    return 0, ""


def get_position_character_and_position_at_left(char, value_position):
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


class DanCrypt:
    def d_crypt(self, text_to_decrypt):
        iteration = int(len(str(text_to_decrypt)) / 2)
        i_final = 0
        str_e1 = ""
        for c in str(text_to_decrypt):
            if i_final >= iteration:
                p, l = get_position_character_and_position_at_right(c, 1)
                str_e1 += l
            else:
                str_e1 += c
            i_final += 1

        str_final = str_e1[len(str_e1)::-1]

        str_d = ""

        for cd in str_final:
            p, l = get_position_character_and_position_at_left(cd, 3)
            str_d += l

        return str_d

    def e_crypt(self, text_to_encrypt):
        str_final = ""
        for c in text_to_encrypt:
            p, l = get_position_character_and_position_at_right(c, 3)
            str_final += l

        str_final = str_final[len(str_final)::-1]

        str_crypt = ""
        iteration = int(len(str(str_final)) / 2)
        i_final = 0
        for s in str(str_final):
            if i_final >= iteration:
                p, l = get_position_character_and_position_at_left(s, 1)
                str_crypt += l
            else:
                str_crypt += s
            i_final += 1

        return str_crypt


if __name__ == "__main__":
    msg = "Hello, Universe!"

    msg_crypt = e_crypt(msg)  # Crypt the message
    msg_decrypt = d_crypt(msg_crypt)  # Decrypt the message
