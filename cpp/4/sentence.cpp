/*
    File: sentence.cpp
    Created by: ??
    Creation Date: ??
    Synopsis: ??
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

// FUNCTION PROTOTYPES 
string get_text(string text);

vector<string> extract_words(string sentence);

void output_words(string text, vector<string> words);

void output_articles(vector<string> words);

vector<string> sort_words(vector<string> words);

// MAIN FUNCTION STARTS HERE.
int main()
{
    string sentence;
    vector<string> words;
    sentence = get_text("enter your sentence: ");
    if (sentence.length() > 0)
    {
        words = extract_words(sentence);
        output_words("you entered the word(s): ", words);
        output_articles(words);
        words = sort_words(words);
        output_words("the sorted list is: ", words);
    }
    else
    {
        cout << "you entered no words !" << endl;
    }
    return 0;
}


// FUNCTION DEFINITIONS STARTS HERE.
// Function for getting sentence input
string get_text(string text)
{
    string sentence;
    cout << text << endl;
    getline(cin, sentence);
    return sentence;
}

// Function to extract words from sentence
vector<string> extract_words(string sentence)
{
    string token = " ";
    vector<string> words;
    while (sentence.size())
    {
        int index = sentence.find(token);
        if (index != string::npos)
        {
            words.push_back(sentence.substr(0, index));
            sentence = sentence.substr(index + token.size());
            if (sentence.size() == 0)
            {
                words.push_back(sentence);
            }
        }
        else
        {
            words.push_back(sentence);
            sentence = "";
        }
    }
    return words;
}

// Function for printing extracted output words
void output_words(string text, vector<string> words)
{
    cout << text << "< ";
    for (int i = 0; i < words.size(); i++)
    {
        if (i == words.size() - 1)
        {
            cout << "'" << words.at(i) << "'"
                 << " ";
        }
        else
        {
            cout << "'" << words.at(i) << "'"
                 << ", ";
        }
    }
    cout << ">" << endl;
}

// Function for printing number of each article
void output_articles(vector<string> words)
{
    cout << "Number of each article: " << endl;
    int number_of_a = 0;
    int number_of_an = 0;
    int number_of_the = 0;
    for (auto &it : words)
    {
        if (it == "a")
        {
            number_of_a += 1;
        }
        else if (it == "an")
        {
            number_of_an += 1;
        }
        else if (it == "the")
        {
            number_of_the += 1;
        }
        else
        {
        }
    }
    cout << number_of_a << " "
         << "'a' word(s)." << endl;
    cout << number_of_an << " "
         << "'an' word(s)." << endl;
    cout << number_of_the << " "
         << "'the' word(s)." << endl;
}

// Function for sorting in ascending order
vector<string> sort_words(vector<string> words)
{
    sort(words.begin(), words.end());
    return words;
}