#!/usr/bin/python3
# -*- coding: utf8 -*-

import core.stop_word as stop_word


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
        text_raw = text.split("==")
        text_list = self.change_type(text_raw[2])
        text_list_raw_p = self.remove_letter(text_list, self.stop_wiki)
        text_list_raw_s = self.remove_space(text_list_raw_p)
        text_str = " ".join(text_list_raw_s)
        text_list = self.change_type(text_str)

        return text_list

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
        for word in text_raw :
            if word != "":
                text_finish.append(word)
        return text_finish

    @staticmethod
    def remove_special(text):
        return text
