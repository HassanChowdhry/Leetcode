// https://leetcode.com/problems/remove-vowels-from-a-string

bool isVowel(char letter) {
    switch (letter) {
        case 'a':
        case 'e':
        case 'u':
        case 'i':
        case 'o':
        return true;
    default:
        return false;
    }
}

char * removeVowels(char * s){
    // char p[strlen(s)];

    // int j = 0;
    // for (int i = 0; i < strlen(s); i++) {
    //     if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u') {
    //         continue;
    //     }
    //     p[j] = s[i];
    //     j++;
    // }

    // p[j] = '\0';
    // strncpy(s, p, strlen(s));
    // return s;

    char * res = malloc(strlen(s) + 1);

    int j = 0;
    int i = 0;
    for (i = 0; i < strlen(s); i++) {
        if (!isVowel(s[i])) {
            res[j] = s[i];
            j++;
        }
    }

    res[j] = '\0';

    return res;
}