#!/usr/bin/python3
# -*- coding: utf8 -*-

import core.stop_word as stop_word
import wikitextparser


class Parser:
    def __init__(self):
        self.stop_word = stop_word.STOP_WORD
        self.address = stop_word.ADDRESS
        self.punctuation = stop_word.PUNCTUATION
        self.stop_wiki = stop_word.PARSER_WIKI
        self.text_list = self.raw_text = []
        self.research = ""

    def research_extractor(self, text):
        """
        Research_extractor extracts the search keyword from the phrase
        :param text: str
        :return: text (str)
        """
        text_list = self.change_type(text)
        text_list_raw_p = self.remove_letter(text_list, self.punctuation)
        text_list_raw_s = self.remove_space(text_list_raw_p)
        self.text_list = self.remove_stop_word(text_list_raw_s, self.stop_word)
        index = self.find_index_research(self.text_list, self.address)
        if index == "NONE":
            self.research = self.text_list
        else:
            self.research = self.text_list[(index + 1) :]

        return " ".join(self.research)

    def text_wiki(self, text):
        """
        the text_wiki method searches for the text to display from the return of the wikipedia API
        :param text: str
        :return: str
        """
        # découpe le fichier apres les ==
        text_raw = text.split("==")
        # sélectionne le texte n°2
        index_section = 2

        text_list = self.change_type(text_raw[index_section])
        text_list_raw_p = self.remove_letter(text_list, self.stop_wiki)
        text_list_raw_s = self.remove_space(text_list_raw_p)
        text_str = " ".join(text_list_raw_s)
        text_list = self.change_type(text_str)
        text_list_raw = self.remove_special(text_list)
        text_list = self.arranger_punctuation(text_list_raw)
        text_finish = " ".join(text_list)
        if text_finish != "":
            return text_finish
        else:
            text_list = self.change_type(text_raw[index_section + 2])
            text_list_raw_p = self.remove_letter(text_list, self.stop_wiki)
            text_list_raw_s = self.remove_space(text_list_raw_p)
            text_str = " ".join(text_list_raw_s)
            text_list = self.change_type(text_str)
            text_list_raw = self.remove_special(text_list)
            text_list = self.arranger_punctuation(text_list_raw)
            text_finish = " ".join(text_list)
        return text_finish

    @staticmethod
    def change_type(text):
        """
        The Change_type method changes the type of text to a list of words
        :param text: str
        :return: text_list (list)
        """
        text_list = text.split(" ")

        return text_list

    @staticmethod
    def remove_stop_word(text, stop_word_list):
        """
        The Remove_stop_word method removes the stop word from the list and makes removes all caps
        :param text: list
        :param stop_word_list: list
        :return: text_finish (list)
        """
        text_finish = [word for word in text if not word.lower() in stop_word_list]

        return text_finish

    @staticmethod
    def find_index_research(text, address_word_list):
        """
        The find_index_research method searches for a keyword contained in the list address_word_list
        :param text: list
        :param address_word_list: list
        :return: index_address (int or "NONE")
        """
        index_address = "NONE"
        for word_text in text:
            for word_address in address_word_list:
                if word_address == word_text:
                    index_address = text.index(word_address)

        return index_address

    @staticmethod
    def remove_letter(text, letter_list):
        """
        The remove_letter method removes the characters contained in the letter_list
        :param text: list
        :param letter_list: list
        :return: text_finish (list)
        """
        text_finish = []
        for word in text:
            word_list = []
            for letter in word:
                if letter in letter_list:
                    word_list.append(" ")
                else:
                    word_list.append(letter)
            if word_list != [" "]:
                text_finish.append("".join(word_list))

        return text_finish

    @staticmethod
    def remove_space(text):
        """
        The remove_space method removes the space in the text and in the word
        :param text: list
        :return: text_finish (list)
        """
        text_finish = []
        text_raw = []
        for word in text:
            if " " in word:
                word_list = word.split(" ")
                for i in word_list:
                    text_raw.append(i)
            else:
                text_raw.append(word)
        for word in text_raw:
            if word != "":
                text_finish.append(word)
        return text_finish

    @staticmethod
    def remove_special(text):
        """
        The remove_special method removes the word type ..., {{word, word, word}}, ...
        :param text: list
        :return: text (list)
        """
        # TODO prendre en compte si une "|" est présent pour l'ajouter au texte
        index_start = []
        index_end = []
        index = 0
        for word in text:
            if "{{" in word:
                index_start.append(index)
            if "}}" in word:
                index_end.append(index)
            index += 1

        index_start.reverse()
        index_end.reverse()

        if len(index_start) == len(index_end):
            nb_index = len(index_start)
            for i in range(0, nb_index):
                if index_start[i] == index_end[i]:
                    del text[index_start[i]]
                else:
                    del text[index_start[i] : index_end[i] + 1]

        return text

    @staticmethod
    def arranger_punctuation(text):
        """
        The arranger_punctuation method arranges the punctuation
        :param text: list
        :return: text (list)
        """

        punctuation = [".", ","]
        index_word = []
        index = 0
        for word in text:
            if word in punctuation:
                if len(word) == 1:
                    index_word.append(index)
            index += 1

        index_word.reverse()

        for i in index_word:
            word = text[i - 1] + text[i]
            text[i - 1] = word
            del text[i]

        return text
